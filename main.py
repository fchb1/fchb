#!/usr/bin/env python3
"""
Motivational Content Generator
Creates hourly short-form content for YouTube and TikTok
Focuses on courage, mental strength, and self-belief
"""

import argparse
import sys
from content_generator import ContentGenerator
from scheduler import ContentScheduler

def main():
    parser = argparse.ArgumentParser(
        description='Generate motivational short-form content for YouTube and TikTok'
    )
    
    parser.add_argument(
        'mode',
        choices=['once', 'hourly', 'continuous'],
        help='Generation mode: once (single generation), hourly (every hour), continuous (custom interval)'
    )
    
    parser.add_argument(
        '-n', '--num-videos',
        type=int,
        default=1,
        help='Number of videos to generate (default: 1)'
    )
    
    parser.add_argument(
        '-d', '--delay',
        type=int,
        default=60,
        help='Delay in seconds between generations in continuous mode (default: 60)'
    )
    
    parser.add_argument(
        '--init-only',
        action='store_true',
        help='Only initialize source library without generating content'
    )
    
    args = parser.parse_args()
    
    print("""
╔════════════════════════════════════════════════════════════╗
║     MOTIVATIONAL CONTENT GENERATOR                         ║
║     YouTube Shorts & TikTok Edition                        ║
║                                                            ║
║     Themes: Courage • Mental Strength • Self-Belief        ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        if args.mode == 'once':
            generator = ContentGenerator()
            
            if args.init_only:
                generator.initialize_source_library()
                print("\n✓ Source library initialized")
            else:
                generator.initialize_source_library()
                videos = generator.generate_content(num_videos=args.num_videos)
                
                if videos:
                    print(f"\n✓ Successfully generated {len(videos)} video(s)")
                    sys.exit(0)
                else:
                    print(f"\n✗ Failed to generate videos")
                    sys.exit(1)
        
        elif args.mode == 'hourly':
            scheduler = ContentScheduler()
            scheduler.setup()
            scheduler.run_hourly()
        
        elif args.mode == 'continuous':
            scheduler = ContentScheduler()
            scheduler.setup()
            scheduler.run_continuous(delay_seconds=args.delay)
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
