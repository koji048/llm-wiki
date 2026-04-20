#!/usr/bin/env python3
import subprocess, json, os, sys, tempfile, math

WORK_DIR = '/root/llm-wiki'
os.chdir(WORK_DIR)

OR_KEY = open('/root/.openrouter_api_key').read().strip()

# Git pull
subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True)

transcripts = [f for f in os.listdir('raw/transcripts') if f.endswith('.txt')]
for fname in transcripts:
    basename = fname[:-4]  # strip only .txt from end
    transcript_path = f'raw/transcripts/{fname}'
    entity_path = f'entities/{basename}.md'
    print(f'Processing: {basename}')

    with open(transcript_path) as f:
        content = f.read()

    def call_llm(prompt, model='anthropic/claude-opus-4.7', timeout=600):
        payload = {
            'model': model,
            'messages': [
                {'role': 'system', 'content': prompt[0]},
                {'role': 'user', 'content': prompt[1]}
            ]
        }
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            json.dump(payload, tmp)
            tmp_path = tmp.name
        try:
            result = subprocess.run(
                ['curl', '-s', '--request', 'POST',
                 '--url', 'https://openrouter.ai/api/v1/chat/completions',
                 '--header', f'Authorization: Bearer {OR_KEY}',
                 '--header', 'Content-Type: application/json',
                 '--data', f'@{tmp_path}'],
                capture_output=True, text=True, timeout=timeout
            )
        finally:
            os.unlink(tmp_path)

        try:
            data = json.loads(result.stdout)
            return data.get('choices', [{}])[0].get('message', {}).get('content', '')
        except:
            print(f'LLM error: {result.stdout[:300] if result.stdout else "(empty)"}')
            return ''

    # Split large transcripts into chunks (~60K chars each to leave room for prompt)
    MAX_CHUNK = 60000
    if len(content) <= MAX_CHUNK:
        # Single call
        SYSTEM = '''You are a technical writer creating detailed wiki entries following the Andrej Karpathy LLM Wiki format. Given a video transcript, create a comprehensive wiki entity page in markdown. Include: (1) YAML frontmatter with title, created date, type: entity, tags extracted from content, sources field pointing to the raw transcript file; (2) A detailed summary section covering the main topics, arguments, and insights - be thorough and capture the depth of the content; (3) Key concepts with brief explanations of each; (4) Major sections/themes with timestamps or approximate positions; (5) Key takeaways (5-10 bullet points); (6) Notable quotes or examples; (7) Related entities section. Format as valid markdown with proper heading hierarchy.'''
        USER = f'''Create a comprehensive wiki entry for the following video transcript. Be thorough and detailed - this is meant to be a useful reference page, not a brief summary:\n\n{content}'''
        summary = call_llm([SYSTEM, USER])
    else:
        # Multi-chunk: generate partial summaries, then synthesize
        print(f'  Splitting {len(content)} char transcript into chunks...')
        chunks = []
        for i in range(0, len(content), MAX_CHUNK):
            chunk = content[i:i+MAX_CHUNK]
            chunk_num = i // MAX_CHUNK + 1
            total_chunks = math.ceil(len(content) / MAX_CHUNK)
            print(f'  Chunk {chunk_num}/{total_chunks} ({len(chunk)} chars)...')
            SYSTEM = f'''You are a section summarizer. Given PART {chunk_num} of {total_chunks} of a video transcript, write a detailed section summary covering the main topics, arguments, insights, key concepts, notable quotes, and key takeaways from THIS SECTION ONLY. Be thorough. Output just the section summary - no preamble.'''
            USER = f'''Transcript section {chunk_num} of {total_chunks}:\n\n{chunk}'''
            section = call_llm([SYSTEM, USER], model='anthropic/claude-sonnet-4', timeout=600)
            if section:
                chunks.append(f'## Part {chunk_num}: Section Summary\n{section}')
            else:
                print(f'  WARNING: Chunk {chunk_num} returned empty')

        # Synthesize all chunks into a full wiki page
        if chunks:
            SYSTEM = '''You are a technical writer creating detailed wiki entries following the Andrej Karpathy LLM Wiki format. Given the section-by-section summaries of a video transcript, create a single comprehensive wiki entity page in markdown. Include: (1) YAML frontmatter with title, created date, type: entity, tags extracted from content, sources field pointing to the raw transcript file; (2) A detailed summary section synthesizing ALL section summaries into a cohesive overview covering the main topics, arguments, and insights; (3) Key concepts with brief explanations of each; (4) Major sections/themes with timestamps or approximate positions; (5) Key takeaways (5-10 bullet points); (6) Notable quotes or examples; (7) Related entities section. Format as valid markdown with proper heading hierarchy.'''
            USER = 'Combine these section summaries into a complete wiki entry:\n\n' + '\n\n---\n\n'.join(chunks)
            summary = call_llm([SYSTEM, USER], timeout=300)
        else:
            summary = ''

    if summary:
        with open(entity_path, 'w') as f:
            f.write(f'# {basename}\n\n{summary}')
        print(f'Created: {entity_path}')
        try:
            os.remove(transcript_path)
        except FileNotFoundError:
            print(f'Transcript already removed: {transcript_path}')
    else:
        print(f'No summary for {basename}')
        print(result.stdout[:500] if result.stdout else '(empty)')

date_result = subprocess.run(['date', '-u', '+%Y%m%dT%H%M%SZ'], capture_output=True, text=True)
ts = date_result.stdout.strip()
subprocess.run(['git', 'add', '-A'], capture_output=True)
result = subprocess.run(['git', 'commit', '-m', f'Auto: process transcripts {ts}'], capture_output=True)
if result.returncode == 0:
    result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True)
    print('Pushed to GitHub')
else:
    print('Nothing to commit')

print(f'Cron run complete at {subprocess.run(["date"],capture_output=True,text=True).stdout}')
