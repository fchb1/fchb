#!/usr/bin/env python3
"""
Example: Batch process multiple videos with different themes
"""

import sys
sys.path.insert(0, '..')

from content_generator import ContentGenerator
from downloader import ContentDownloader
import config

def generate_theme_batch(theme_keywords, num_videos=3):
    """Generate videos for a specific theme"""
    print(f"\n{'='*60}")
    print(f"Generating {num_videos} videos for theme: {theme_keywords[0]}")
    print(f"{'='*60}")
    
    original_keywords = config.MOTIVATIONAL_KEYWORDS
    config.MOTIVATIONAL_KEYWORDS = theme_keywords
    
    generator = ContentGenerator()
    generator.initialize_source_library(num_videos=15)
    
    videos = generator.generate_content(num_videos=num_videos)
    
    generator.cleanup()
    
    config.MOTIVATIONAL_KEYWORDS = original_keywords
    
    return videos

def main():
    print("Batch Theme Processing Example")
    print("="*60)
    
    themes = [
        {
            'name': 'Courage',
            'keywords': ['courage motivation', 'face your fears', 'be brave']
        },
        {
            'name': 'Mental Strength',
            'keywords': ['mental strength', 'mental toughness', 'strong mind']
        },
        {
            'name': 'Self-Belief',
            'keywords': ['believe in yourself', 'self confidence', 'trust yourself']
        }
    ]
    
    all_videos = []
    
    for theme in themes:
        videos = generate_theme_batch(theme['keywords'], num_videos=2)
        all_videos.extend(videos)
        print(f"\n✓ Generated {len(videos)} videos for {theme['name']}")
    
    print(f"\n{'='*60}")
    print(f"✓ Total videos generated: {len(all_videos)}")
    print(f"{'='*60}")
    
    for i, video in enumerate(all_videos, 1):
        print(f"{i}. {video}")

if __name__ == '__main__':
    main()
