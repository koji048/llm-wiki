#!/usr/bin/env python3
"""
LLM Wiki article processor — generates wiki entity pages from scraped markdown.
Uses Opus 4.7. Reads raw/articles/*.md → writes entities/*.md.
"""
import subprocess, json, os, sys, tempfile, re, time
from datetime import date

WORK_DIR = '/root/llm-wiki'
os.chdir(WORK_DIR)

OR_KEY = open('/root/.openrouter_api_key').read().strip()
TODAY = date.today().isoformat()

def call_llm(system_msg, user_msg, model='anthropic/claude-opus-4.7', timeout=600, retries=2):
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
                    time.sleep(10 * (attempt + 1))
                    continue
                return ''
            raw = data.get('choices', [{}])[0].get('message', {}).get('content', '')
            if not raw or not raw.strip():
                if attempt < retries:
                    time.sleep(5)
                    continue
                return ''
            return raw.strip()
        except json.JSONDecodeError as e:
            print(f'  JSON parse error (attempt {attempt+1}): {e}')
            if result.stdout:
                print(f'  Raw: {result.stdout[:200]}')
            if attempt < retries:
                time.sleep(5)
                continue
            return ''
        except Exception as e:
            print(f'  LLM error: {e}')
            if attempt < retries:
                time.sleep(5)
                continue
            return ''
    return ''


ARTICLE_SYS = f"""You are a technical writer creating comprehensive wiki entries following
the Andrej Karpathy LLM Wiki format. Every entry must be a self-contained reference page.

Read the source article carefully. Synthesize its key ideas, claims, and technical details
into a thorough wiki entity page.

OUTPUT FORMAT — produce EXACTLY this structure:

---
title: "EXTRACTED TITLE"
created: {TODAY}
type: entity
tags: [tag1, tag2, tag3, tag4, tag5]
related: [[Entity Name 1]], [[Entity Name 2]]
sources: [raw/articles/FILENAME.md]
---

# EXTRACTED TITLE

## Summary
[2-4 paragraphs. Be specific — name techniques, papers, tools, companies, numbers.
This is a technical reference page, not a summary. Go deep.]

## Key Concepts
[For each major concept (aim for 6-12):
- **Concept Name**: One-sentence definition, then 2-3 sentences of detailed explanation.
  Name specific examples, papers, or techniques when relevant.]

## Key Takeaways
- [Bullet 1: specific, factual claim or actionable insight]
- [Bullet 2]
- [Bullet 3]
- [Bullet 4]
- [Bullet 5]
- [Bullet 6+ if important]

## Notable Quotes
> "[Quote 1 — notable claim or definition]"
> "[Quote 2]"
> "[Quote 3]"

## Related Entities
[[Entity Name 1]], [[Entity Name 2]], [[Entity Name 3]], [[Entity Name 4]]

## Tags
[suggest 4-8 tags for this content]
"""


NAV_JUNK = {
    'skip to main content', 'discord', 'search...', 'ctrl k', 'ask ai',
    'navigation', 'table of contents', 'github', 'table of contents',
}
NAV_PATTERNS = [
    re.compile(r'^\[Skip to', re.I),
    re.compile(r'Agent Skills now has an official', re.I),
    re.compile(r'^\s*\*\s*\['),  # list items (nav)
    re.compile(r'^Agent Skills home page', re.I),
    re.compile(r'^\s*Search\.\.\.', re.I),
    re.compile(r'^\s*Ctrl K', re.I),
    re.compile(r'^\s*For skill creators', re.I),
    re.compile(r'^#+\s*For ', re.I),
]


def is_nav_junk(line):
    """Skip nav/junk lines that aren't real article content."""
    stripped = line.strip()
    if not stripped:
        return True
    # Short navigation lines
    if stripped.lower() in NAV_JUNK:
        return True
    # Nav pattern matches
    for pat in NAV_PATTERNS:
        if pat.match(stripped):
            return True
    return False


def extract_title(content):
    """Pull title from frontmatter or first real article heading."""
    m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
    if m and m.group(1).strip():
        return m.group(1).strip()
    # Find the first real H1 heading after nav junk
    for line in content.split('\n'):
        if is_nav_junk(line):
            continue
        m = re.match(r'^(#{1,2})\s+(.+)$', line.strip())
        if m and len(m.group(1)) <= 2:
            title = m.group(2).strip()
            # Clean markdown links
            title = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', title)
            title = title.strip()
            if len(title) > 4:
                return title
    return 'Untitled'


def extract_source_url(content):
    """Pull source URL from frontmatter."""
    m = re.search(r'^source:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else ''


def extract_body(content):
    """Remove frontmatter."""
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            return content[end+3:].strip()
    return content


def slugify(title, url=''):
    """Create a short slug from title or URL."""
    # Use URL slug if title is generic
    if 'untitled' in title.lower() or len(title) < 5:
        if url:
            u = re.sub(r'https?://', '', url)
            u = re.sub(r'[^\w]', '-', u)
            u = re.sub(r'-+', '-', u)
            return u.strip('-')[:60]
    s = re.sub(r'[^\w\s\-]', '', title.lower())
    s = re.sub(r'[\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    # Remove common stop words for brevity
    stop = {'the', 'a', 'an', 'of', 'to', 'for', 'in', 'on', 'at', 'and', 'or', 'is', 'it', 'with'}
    parts = [p for p in s.split('-') if p and p not in stop]
    slug = '-'.join(parts)[:60]
    return slug or 'article'


def main():
    subprocess.run(['git', 'pull', 'origin', 'master'], capture_output=True)

    articles = [f for f in os.listdir('raw/articles')
                 if f.endswith('.md') and f != '.gitkeep']

    if not articles:
        print('No articles to process')
        return

    print(f'Found {len(articles)} article(s)')

    for fname in articles:
        article_path = f'raw/articles/{fname}'
        body = extract_body(open(article_path).read())
        title = extract_title(open(article_path).read())
        source_url = extract_source_url(open(article_path).read())
        slug = slugify(title, source_url)
        entity_path = f'entities/{slug}.md'

        # Avoid overwriting existing entities
        if os.path.exists(entity_path):
            slug = f'{slug}-{date.today().strftime("%Y%m%d")}'
            entity_path = f'entities/{slug}.md'

        print(f'\nProcessing: {title}')
        print(f'  Source: {source_url}')
        print(f'  Body: {len(body):,} chars')

        # For very long articles, chunk
        MAX_SINGLE = 55000
        if len(body) <= MAX_SINGLE:
            user_msg = f"""Source article: {source_url}
Original file: raw/articles/{fname}

Create a comprehensive wiki entity page for this article. Be thorough and technically
precise — this is a reference page, not a synopsis.

--- ARTICLE CONTENT ---

{body}

--- END ARTICLE ---

Extract all key technical details, claims, numbers, tools, and concepts.
"""
            summary = call_llm(ARTICLE_SYS, user_msg)
            if summary:
                with open(entity_path, 'w') as f:
                    f.write(f'# {title}\n\n{summary}')
                print(f'  Created: {entity_path} ({len(summary):,} chars)')
                os.remove(article_path)
            else:
                print(f'  FAILED — no summary generated')

        else:
            # Chunk long articles
            print(f'  Long article — chunking...')
            chunks = []
            total = 0
            for i in range(0, len(body), MAX_SINGLE):
                chunk = body[i:i+MAX_SINGLE]
                n = i // MAX_SINGLE + 1
                print(f'  Chunk {n} ({len(chunk):,} chars)...')
                section = call_llm(
                    """You are a section summarizer. Summarize this section of an article
in 300-500 words. Extract key facts, claims, techniques, and names.
Write only the summary, no preamble.""",
                    f'Section {n}:\n\n{chunk}',
                    timeout=900
                )
                if section:
                    chunks.append(f'## Section {n}\n{section}')
                    total += len(section)
                else:
                    print(f'  WARNING: Chunk {n} returned empty')

            if chunks:
                synthesis = call_llm(
                    """You are a wiki architect. You have section summaries of an article.
Synthesize them into a single wiki entity page. Use all the information — do not omit
important details. Be specific: name tools, techniques, numbers, companies.""",
                    f'Article title: {title}\nSource: {source_url}\n\n' + '\n\n'.join(chunks),
                    timeout=900
                )
                if synthesis:
                    with open(entity_path, 'w') as f:
                        f.write(f'# {title}\n\n{synthesis}')
                    print(f'  Created: {entity_path} ({len(synthesis):,} chars)')
                    os.remove(article_path)
                else:
                    print(f'  FAILED — synthesis returned empty')

    ts = subprocess.run(['date', '-u', '+%Y%m%dT%H%M%SZ'],
                       capture_output=True, text=True).stdout.strip()
    subprocess.run(['git', 'add', '-A'])
    r = subprocess.run(['git', 'commit', '-m', f'Auto: process articles {ts}'],
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
