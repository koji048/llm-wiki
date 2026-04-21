#!/usr/bin/env python3
"""
LLM Wiki transcript processor v2 — generates wiki entity pages from video transcripts.
Uses Opus 4.7 for maximum depth and quality. Karpathy wiki style.
"""
import subprocess, json, os, sys, tempfile, math, re, time
from datetime import date

WORK_DIR = '/root/llm-wiki'
os.chdir(WORK_DIR)

OR_KEY = open('/root/.openrouter_api_key').read().strip()
TODAY = date.today().isoformat()


def call_llm(system_msg, user_msg, model='anthropic/claude-opus-4.7', timeout=600, retries=2):
    """Call OpenRouter with retry on failure. Return response text or ''."""
    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': system_msg},
            {'role': 'user', 'content': user_msg}
        ],
        'temperature': 0.2,
        'max_tokens': 8192
    }
    for attempt in range(retries + 1):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            json.dump(payload, tmp)
            tmp_path = tmp.name
        try:
            result = subprocess.run(
                ['curl', '-s', '--request', 'POST',
                 '--url', 'https://openrouter.ai/api/v1/chat/completions',
                 '--header', f'Authorization: Bearer {OR_KEY}',
                 '--header', 'Content-Type: application/json',
                 '--header', 'HTTP-Referer: https://llm-wiki',
                 '--header', 'X-Title: LLM Wiki Processor',
                 '--data', f'@{tmp_path}'],
                capture_output=True, text=True, timeout=timeout
            )
        finally:
            os.unlink(tmp_path)

        try:
            data = json.loads(result.stdout)
            if 'error' in data:
                err_msg = data['error'].get('message', str(data['error']))
                print(f'  API error (attempt {attempt+1}): {err_msg[:200]}')
                if attempt < retries:
                    wait = 10 * (attempt + 1)
                    print(f'  Retrying in {wait}s...')
                    time.sleep(wait)
                    continue
                return ''
            raw = data.get('choices', [{}])[0].get('message', {}).get('content', '')
            if not raw or not raw.strip():
                print(f'  Empty response (attempt {attempt+1})')
                if attempt < retries:
                    time.sleep(5)
                    continue
                return ''
            m = re.search(r'```(?:\w+)?\n(.*?)\n```', raw, re.DOTALL)
            return (m.group(1) if m else raw).strip()
        except json.JSONDecodeError as e:
            print(f'  JSON parse error (attempt {attempt+1}): {e}')
            if result.stdout:
                print(f'  Raw preview: {result.stdout[:200]}')
            if attempt < retries:
                time.sleep(5)
                continue
            return ''
        except Exception as e:
            print(f'  LLM error: {e} — raw: {result.stdout[:300] if result.stdout else "(empty)"}')
            if attempt < retries:
                time.sleep(5)
                continue
            return ''
    return ''


SINGLE_PASS_SYS = f"""You are a technical writer creating comprehensive wiki entries following
the Andrej Karpathy LLM Wiki format. Every entry must be a self-contained reference page
that someone can read instead of watching the full video.

OUTPUT FORMAT — produce EXACTLY this structure, nothing else:

---
title: "EXTRACTED VIDEO TITLE"
created: {TODAY}
type: entity
tags: [tag1, tag2, tag3, tag4, tag5]
sources: [raw/transcripts/EXACT_ORIGINAL_FILENAME.txt]
---

# EXTRACTED VIDEO TITLE

## Summary
[2-4 paragraphs. Start with what this video is about and who the presenter is.
Then explain the core topics, main arguments, and key insights in depth.
Be specific — name-drop models, papers, techniques, companies, numbers, dates.
Do NOT write generic marketing summaries. This is a technical reference page.]

## Key Concepts
[For each major concept (aim for 6-12):
- **Concept Name**: One-sentence definition, then 2-3 sentences of detailed explanation.
  Name specific examples, papers, or techniques when relevant.]

## Major Sections
[Chronological or thematic breakdown. For each section: heading + 2-4 sentences.
Include approximate timestamps if visible in the transcript.]

## Key Takeaways
- [Bullet 1: specific, factual claim or actionable insight]
- [Bullet 2]
- [Bullet 3]
- [Bullet 4]
- [Bullet 5]
- [Bullet 6]
- [Bullet 7+ if important]

## Notable Quotes
> "[Quote 1 — include speaker attribution if visible]"
> "[Quote 2]"
> "[Quote 3 — memorable phrase or definition]"

## Related Entities
[[Entity Name 1]], [[Entity Name 2]], [[Entity Name 3]], [[Entity Name 4]]
"""


SECTION_SYS = """You are a section analyst. Produce a dense, faithful summary of ONE
SECTION of a video transcript. Do NOT editorialize or add information not present.
Do NOT speculate about what comes before or after.

For your section, extract:
1. Specific topics discussed (name models, papers, techniques, companies)
2. Key claims and any numbers/statistics cited
3. Notable definitions or explanations given
4. Any notable quotes or analogies used
5. The main argument or point being made

OUTPUT: Write a thorough section summary in markdown. No preamble. 200-500 words.
"""


SYNTHESIS_SYS = f"""You are a wiki architect. You have section-by-section summaries of a
video transcript. Synthesize them into a single, cohesive wiki entity page.

Use the section summaries as your source of truth — do not make things up.
Extract real names, numbers, papers, techniques from the summaries.

OUTPUT FORMAT — produce EXACTLY this structure:

---
title: "EXTRACTED VIDEO TITLE"
created: {TODAY}
type: entity
tags: [tag1, tag2, tag3, tag4, tag5]
sources: [raw/transcripts/EXACT_ORIGINAL_FILENAME.txt]
---

# EXTRACTED VIDEO TITLE

## Summary
[2-4 paragraphs. Cover ALL major topics from the sections. Be specific — include
model names, paper names, companies, numbers, techniques. Avoid generic platitudes.
This is a technical deep-dive reference page.]

## Key Concepts
[For each major concept (aim for 6-12):
- **Concept Name**: One-sentence definition, then 2-3 sentences of explanation.
  Be specific. Mention examples, papers, techniques when relevant.]

## Major Sections
[Chronological or thematic breakdown covering every section.
For each: heading + 2-4 sentences. Include approximate timestamps if visible.]

## Key Takeaways
- [Bullet 1: specific, factual claim or actionable insight]
- [Bullet 2]
- [Bullet 3]
- [Bullet 4]
- [Bullet 5]
- [Bullet 6]
- [Bullet 7+ if important]

## Notable Quotes
> "[Quote 1]"
> "[Quote 2]"
> "[Quote 3]"

## Related Entities
[[Entity Name 1]], [[Entity Name 2]], [[Entity Name 3]], [[Entity Name 4]]
"""


def extract_title(fname):
    """Pull the human-readable title from the transcript filename."""
    name = fname[:-4]  # strip .txt
    vid_match = re.search(r'\[([A-Za-z0-9_-]{11})\]\.en$', name)
    video_id = vid_match.group(1) if vid_match else 'unknown'
    title = re.sub(r'\s*\[[A-Za-z0-9_-]{11}\]\.en$', '', name)
    return title.strip(), video_id


def main():
    subprocess.run(['git', 'pull', 'origin', 'master'], capture_output=True)

    transcripts = [f for f in os.listdir('raw/transcripts')
                   if f.endswith('.txt') and f != '.gitkeep']

    if not transcripts:
        print('No transcripts to process')
        return

    print(f'Found {len(transcripts)} transcript(s)')

    for fname in transcripts:
        basename = fname[:-4]
        transcript_path = f'raw/transcripts/{fname}'
        entity_path = f'entities/{basename}.md'
        video_title, video_id = extract_title(fname)

        print(f'\nProcessing: {video_title} [{video_id}]')
        content = open(transcript_path).read()
        content_len = len(content)
        print(f'  Transcript: {content_len:,} chars')

        MAX_SINGLE = 55000
        if content_len <= MAX_SINGLE:
            user_msg = f"""Original transcript file: raw/transcripts/{fname}

Create a comprehensive wiki entity page for this video transcript. Be thorough
and technically precise — this is a reference page, not a synopsis.

Video title: {video_title}

---

{content}"""

            summary = call_llm(SINGLE_PASS_SYS, user_msg)
            if summary:
                with open(entity_path, 'w') as f:
                    f.write(f'# {video_title}\n\n{summary}')
                print(f'  Created: {entity_path} ({len(summary):,} chars)')
                os.remove(transcript_path)
            else:
                print(f'  FAILED — no summary generated')

        else:
            CHUNK_SIZE = 55000
            chunks = []
            total = math.ceil(content_len / CHUNK_SIZE)

            print(f'  Splitting into {total} chunks...')
            for i in range(0, content_len, CHUNK_SIZE):
                chunk = content[i:i+CHUNK_SIZE]
                n = i // CHUNK_SIZE + 1
                print(f'  Chunk {n}/{total} ({len(chunk):,} chars)...')

                section = call_llm(
                    SECTION_SYS,
                    f'Video title: {video_title}\nSection {n} of {total}:\n\n{chunk}',
                    timeout=900
                )
                if section:
                    chunks.append(f'## Section {n}\n{section}')
                else:
                    print(f'  WARNING: Chunk {n} returned empty')

            if chunks:
                print(f'  Synthesizing {len(chunks)} sections...')
                summary = call_llm(
                    SYNTHESIS_SYS,
                    f'Video title: {video_title}\nOriginal file: raw/transcripts/{fname}\n\n'
                    + '\n\n---\n\n'.join(chunks),
                    timeout=900
                )
                if summary:
                    with open(entity_path, 'w') as f:
                        f.write(f'# {video_title}\n\n{summary}')
                    print(f'  Created: {entity_path} ({len(summary):,} chars)')
                    os.remove(transcript_path)
                else:
                    print(f'  FAILED — synthesis returned empty')
            else:
                print(f'  FAILED — no chunks processed')

    ts = subprocess.run(['date', '-u', '+%Y%m%dT%H%M%SZ'],
                        capture_output=True, text=True).stdout.strip()
    subprocess.run(['git', 'add', '-A'])
    r = subprocess.run(['git', 'commit', '-m', f'Auto: process transcripts {ts}'],
                       capture_output=True, text=True)
    if r.returncode == 0:
        r = subprocess.run(['git', 'push', 'origin', 'master'],
                          capture_output=True, text=True)
        print(f'\nPushed to GitHub')
    else:
        print(f'\nNothing new to commit')

    print(f'Done at {subprocess.run(["date"],capture_output=True,text=True).stdout}')


if __name__ == '__main__':
    main()
