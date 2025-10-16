#!/usr/bin/env python3
"""
Example: Custom video generation with specific parameters
"""

import sys
sys.path.insert(0, '..')

from content_generator import ContentGenerator
import config

def main():
    print("Custom Video Generation Example")
    print("="*60)
    
    generator = ContentGenerator()
    
    print("\n1. Initializing source library...")
    generator.initialize_source_library(num_videos=20)
    
    print("\n2. Generating 3 custom videos...")
    
    original_clips = config.CLIPS_PER_VIDEO
    config.CLIPS_PER_VIDEO = 5
    
    videos = generator.generate_content(num_videos=3)
    
    config.CLIPS_PER_VIDEO = original_clips
    
    print(f"\n✓ Generated {len(videos)} videos:")
    for video in videos:
        print(f"  - {video}")
    
    print("\n3. Cleaning up...")
    generator.cleanup()
    
    print("\n✓ Done!")

if __name__ == '__main__':
    main()
