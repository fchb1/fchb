#!/usr/bin/env python3
"""
Demo script to showcase the content generator capabilities
"""

import sys
from pathlib import Path
from content_generator import ContentGenerator
import config

def print_section(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def demo():
    print("""
╔════════════════════════════════════════════════════════════╗
║     MOTIVATIONAL CONTENT GENERATOR - DEMO                  ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    print_section("CONFIGURATION")
    print(f"Theme Keywords: {len(config.MOTIVATIONAL_KEYWORDS)} keywords")
    for kw in config.MOTIVATIONAL_KEYWORDS[:5]:
        print(f"  • {kw}")
    print(f"  ... and {len(config.MOTIVATIONAL_KEYWORDS) - 5} more")
    
    print(f"\nMotivational Quotes: {len(config.MOTIVATIONAL_QUOTES)} quotes")
    for quote in config.MOTIVATIONAL_QUOTES[:3]:
        print(f"  • {quote}")
    print(f"  ... and {len(config.MOTIVATIONAL_QUOTES) - 3} more")
    
    print(f"\nVideo Settings:")
    print(f"  • Duration: {config.MIN_VIDEO_LENGTH}-{config.MAX_VIDEO_LENGTH} seconds")
    print(f"  • Clips per video: {config.CLIPS_PER_VIDEO}")
    print(f"  • Resolution: {config.VIDEO_RESOLUTION}")
    
    print_section("INITIALIZING GENERATOR")
    generator = ContentGenerator()
    
    print("\nThis demo will:")
    print("  1. Download source videos from YouTube")
    print("  2. Extract and process clips")
    print("  3. Combine clips with motivational overlays")
    print("  4. Generate one complete video")
    
    response = input("\nProceed with demo? (y/n): ").strip().lower()
    if response != 'y':
        print("Demo cancelled.")
        return
    
    print_section("STEP 1: COLLECTING SOURCE VIDEOS")
    print("Downloading motivational content from YouTube...")
    print("(This may take a few minutes)")
    
    try:
        generator.initialize_source_library(num_videos=15)
        
        stats = generator.get_stats()
        print(f"\n✓ Source library initialized")
        print(f"  • Source videos: {stats['source_videos']}")
        print(f"  • Temp directory: {stats['temp_dir']}")
        
    except Exception as e:
        print(f"\n✗ Error collecting source videos: {e}")
        print("\nNote: This demo requires internet connection and YouTube access")
        return
    
    print_section("STEP 2: GENERATING MASHUP VIDEO")
    print("Creating motivational video mashup...")
    
    try:
        videos = generator.generate_content(num_videos=1)
        
        if videos:
            print(f"\n✓ Video generated successfully!")
            print(f"  • Output: {videos[0]}")
            print(f"  • Size: {Path(videos[0]).stat().st_size / 1024 / 1024:.2f} MB")
            
            stats = generator.get_stats()
            print(f"\n📊 Final Statistics:")
            print(f"  • Source videos used: {stats['source_videos']}")
            print(f"  • Videos generated: {stats['generated_videos']}")
            print(f"  • Output directory: {stats['output_dir']}")
            
            print_section("NEXT STEPS")
            print("Your video is ready to upload!")
            print(f"\nLocation: {videos[0]}")
            print("\nPlatforms:")
            print("  ✓ YouTube Shorts (9:16 vertical format)")
            print("  ✓ TikTok (9:16 vertical format)")
            print("  ✓ Instagram Reels (9:16 vertical format)")
            
            print("\nTo generate more videos:")
            print("  • One video:  python main.py once")
            print("  • Multiple:   python main.py once -n 5")
            print("  • Hourly:     python main.py hourly")
        
        else:
            print("\n✗ Video generation failed")
            
    except Exception as e:
        print(f"\n✗ Error generating video: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print_section("CLEANUP")
        response = input("Clean up temporary files? (y/n): ").strip().lower()
        if response == 'y':
            generator.cleanup()
            print("✓ Cleanup complete")

if __name__ == '__main__':
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Demo error: {e}")
        sys.exit(1)
