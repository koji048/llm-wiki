#!/usr/bin/env python3
"""Direct scraper using curl + readability extraction."""
import subprocess, os, sys, re
from datetime import date

WORK_DIR = '/root/llm-wiki'
os.chdir(WORK_DIR)

def slug_from_url(url):
    u = re.sub(r'https?://', '', url)
    parts = [p for p in re.split(r'[/\-_.?&=]', u) if p]
    return '-'.join(parts[-4:])[:100]

def scrape_url(url):
    """Fetch URL with curl and extract text."""
    try:
        result = subprocess.run(
            ['curl', '-s', '--max-time', '30',
             '-H', 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
             url],
            capture_output=True, text=True, timeout=35
        )
        html = result.stdout
        if not html.strip():
            return None
        # Simple text extraction - get title and body text
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else ''
        # Remove scripts, styles, nav, footer
        html_clean = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL|re.IGNORECASE)
        html_clean = re.sub(r'<style[^>]*>.*?</style>', '', html_clean, flags=re.DOTALL|re.IGNORECASE)
        html_clean = re.sub(r'<nav[^>]*>.*?</nav>', '', html_clean, flags=re.DOTALL|re.IGNORECASE)
        html_clean = re.sub(r'<footer[^>]*>.*?</footer>', '', html_clean, flags=re.DOTALL|re.IGNORECASE)
        html_clean = re.sub(r'<header[^>]*>.*?</header>', '', html_clean, flags=re.DOTALL|re.IGNORECASE)
        # Convert HTML to markdown-like
        text = re.sub(r'<br\s*/?>','\n', html_clean)
        text = re.sub(r'</p>', '\n\n', text)
        text = re.sub(r'</div>', '\n', text)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = text.strip()
        if title:
            text = f'# {title}\n\n{text}'
        return text
    except Exception as e:
        print(f'Error: {e}')
        return None

def save_article(url, content):
    slug = slug_from_url(url)
    filename = f'{slug}.md'
    path = f'raw/articles/{filename}'
    if os.path.exists(path):
        ts = date.today().strftime('%Y%m%d')
        filename = f'{slug}-{ts}.md'
        path = f'raw/articles/{filename}'
    header = f"""---
source: {url}
tags: [web, article]
type: raw
---\n"""
    with open(path, 'w') as f:
        f.write(header + content)
    print(f'Saved: {path}')
    return path

def main():
    urls = []
    if '--batch' in sys.argv:
        with open('.scripts/scrape_urls.txt') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    for arg in sys.argv[1:]:
        if arg.startswith('http'):
            urls.append(arg)
    
    if not urls:
        print('No URLs')
        return
    
    print(f'Scraping {len(urls)} URL(s)...')
    saved = []
    for url in urls:
        print(f'Scraping: {url}')
        md = scrape_url(url)
        if md and len(md) > 200:
            save_article(url, md)
            saved.append(url)
        else:
            print(f'FAILED or too short: {url}')
    
    print(f'Done. {len(saved)} article(s) saved.')
    if saved:
        print('Run process_articles.py next.')

if __name__ == '__main__':
    main()
