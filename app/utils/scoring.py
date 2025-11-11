from typing import Dict
import re

def score_meta_tag(title: str, description: str, keywords: list) -> Dict:
    title_score = score_title(title)
    description_score = score_description(description)
    keyword_score = score_keywords(title, description, keywords)
    
    ctr_score = (title_score + description_score) / 2
    
    return {
        'ctr_score': round(ctr_score, 2),
        'keyword_score': round(keyword_score, 2),
        'title_score': round(title_score, 2),
        'description_score': round(description_score, 2)
    }

def score_title(title: str) -> float:
    score = 0.5
    
    if 50 <= len(title) <= 60:
        score += 0.3
    elif 40 <= len(title) < 50 or 60 < len(title) <= 70:
        score += 0.2
    
    if any(char.isdigit() for char in title):
        score += 0.1
    
    if '|' in title or '-' in title:
        score += 0.1
    
    return min(score, 1.0)

def score_description(description: str) -> float:
    score = 0.5
    
    if 150 <= len(description) <= 160:
        score += 0.3
    elif 140 <= len(description) < 150 or 160 < len(description) <= 170:
        score += 0.2
    
    if any(word in description.lower() for word in ['best', 'guide', 'how to']):
        score += 0.1
    
    if '.' in description:
        score += 0.1
    
    return min(score, 1.0)

def score_keywords(title: str, description: str, keywords: list) -> float:
    if not keywords:
        return 0.5
    
    combined_text = f"{title} {description}".lower()
    matches = sum(1 for kw in keywords if kw.lower() in combined_text)
    
    return min(matches / len(keywords), 1.0)
