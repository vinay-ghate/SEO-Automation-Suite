from bs4 import BeautifulSoup
from typing import Dict, List
import re

def extract_text_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    
    for script in soup(["script", "style"]):
        script.decompose()
    
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)
    
    return text

def extract_headings(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, 'html.parser')
    headings = []
    
    for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for heading in soup.find_all(tag):
            headings.append({
                'level': tag,
                'text': heading.get_text().strip()
            })
    
    return headings

def extract_meta_tags(html: str) -> Dict:
    soup = BeautifulSoup(html, 'html.parser')
    
    meta_tags = {
        'title': '',
        'description': '',
        'keywords': ''
    }
    
    title_tag = soup.find('title')
    if title_tag:
        meta_tags['title'] = title_tag.get_text()
    
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag:
        meta_tags['description'] = desc_tag.get('content', '')
    
    return meta_tags
