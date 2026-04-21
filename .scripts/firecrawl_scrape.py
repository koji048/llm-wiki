#!/usr/bin/env python3
"""
LLM Wiki Firecrawl scraper — fetches web pages via Firecrawl API and saves markdown.
Usage: python3 firecrawl_scrape.py <url> [url2 ...]
   Or: python3 firecrawl_scrape.py --batch  (reads URLs from .urls file)
Saves output to raw/articles/ as .md files.
"""
import subprocess, json, os, sys, re, time
from datetime import date

WORK_DIR = '/root/llm-wiki'
os.chdir(WORK_DIR)

API_KEY_PATH = '/root/.firecrawl_api_key'
FC_KEY = None

def get_api_key():
    global FC_KEY
    if FC_KEY:
        return FC_KEY
    # Try env var first
    FC_KEY = os.environ.get('FIRECRAWL_API_KEY', '')
    if FC_KEY:
        return FC_KEY
    # Try key file
    if os.path.exists(API_KEY_PATH):
        FC_KEY = open(API_KEY_PATH).read().strip()
        return FC_KEY
    # Fallback to known key
    FC_KEY = 'fc-c52828738fdf42aabb3711708ac22085'
    return FC_KEY


def slug_from_url(url):
    """Create a safe filename slug from URL."""
    name = re.sub(r'https?://', '', url)
    name = re.sub(r'[^\w\-]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')[:120]
    return name


def scrape_url(url, max_retries=3):
    """Scrape a URL via Firecrawl. Returns markdown string or None."""
    key = get_api_key()
    payload = {
        'url': url,
        'formats': ['markdown'],
    }
    for attempt in range(max_retries + 1):
        try:
            result = subprocess.run(
                ['curl', '-s', '--request', 'POST',
                 '--url', 'https://api.firecrawl.dev/v0/scrape',
                 '--header', f'Authorization: Bearer {key}',
                 '--header', 'Content-Type: application/json',
                 '--data', json.dumps(payload)],
                capture_output=True, text=True, timeout=60
            )
            data = json.loads(result.stdout)
            if not data.get('success'):
                rc = data.get('returnCode', 'UNKNOWN')
                print(f'  Firecrawl error ({rc}) on attempt {attempt+1}')
                if attempt < max_retries:
                    time.sleep(5 * (attempt + 1))
                    continue
                return None
            md = data.get('data', {}).get('markdown', '')
            if not md.strip():
                print(f'  Empty markdown returned')
                return None
            return md
        except json.JSONDecodeError as e:
            print(f'  JSON parse error: {e} — attempt {attempt+1}')
            if attempt < max_retries:
                time.sleep(5)
                continue
            return None
        except Exception as e:
            print(f'  Error: {e} — attempt {attempt+1}')
            if attempt < max_retries:
                time.sleep(5)
                continue
            return None
    return None


def save_article(url, markdown):
    """Save markdown to raw/articles/ and return the path."""
    slug = slug_from_url(url)
    # Try to extract a title from first line
    lines = markdown.strip().split('\n')
    title = ''
    for line in lines:
        line = line.strip()
        if line and not line.startswith('[') and len(line) > 5:
            title = re.sub(r'^#+\s*', '', line).strip()
            break

    date_str = date.today().isoformat()
    safe_slug = re.sub(r'[^\w\-]', '_', slug)[:100]

    filename = f'{safe_slug}.md'
    path = f'raw/articles/{filename}'
    content = f"---\ntitle: \"{title[:200]}\"\ncreated: {date_str}\nsource: {url}\ntags: [web, article]\ntype: raw\n---\n\n{markdown}"
    with open(path, 'w') as f:
        f.write(content)
    print(f'  Saved: {path} ({len(markdown):,} chars)')
    return path


def main():
    urls = []

    if '--batch' in sys.argv:
        # Read URLs from .urls file
        url_file = '.scripts/scrape_urls.txt'
        if os.path.exists(url_file):
            with open(url_file) as f:
                urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        if not urls:
            print('No URLs in scrape_urls.txt')
            return

    # Collect URLs from args
    for arg in sys.argv[1:]:
        if arg.startswith('http'):
            urls.append(arg)

    if not urls:
        print('Usage: python3 firecrawl_scrape.py <url> [url2 ...]')
        print('   or: python3 firecrawl_scrape.py --batch')
        return

    print(f'Scraping {len(urls)} URL(s)...')
    saved = []
    for url in urls:
        print(f'\nScraping: {url}')
        md = scrape_url(url)
        if md:
            path = save_article(url, md)
            saved.append(path)
        else:
            print(f'  FAILED: {url}')

    if saved:
        print(f'\n{len(saved)} article(s) saved to raw/articles/')
        print('Run process_articles.py to generate entity pages.')
    else:
        print('\nNo articles saved.')


if __name__ == '__main__':
    main()
