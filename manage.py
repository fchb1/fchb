#!/usr/bin/env python3
"""
Management CLI for the content generator
"""

import argparse
import sys
from pathlib import Path
import config
from utils import list_generated_videos, clean_old_videos, print_statistics, get_disk_usage
from downloader import ContentDownloader

def cmd_list():
    """List all generated videos"""
    videos = list_generated_videos()
    
    if not videos:
        print("No videos generated yet.")
        return
    
    print(f"\n{'='*80}")
    print(f"  GENERATED VIDEOS ({len(videos)} total)")
    print(f"{'='*80}")
    
    for i, video in enumerate(videos, 1):
        if 'error' in video:
            print(f"\n{i}. ERROR: {video['error']}")
            continue
        
        filename = Path(video['path']).name
        print(f"\n{i}. {filename}")
        print(f"   Duration: {video['duration']:.1f}s")
        print(f"   Size: {video['file_size_mb']:.2f} MB")
        print(f"   Resolution: {video['size'][0]}x{video['size'][1]}")
        print(f"   FPS: {video['fps']}")
        print(f"   Path: {video['path']}")
    
    print(f"\n{'='*80}")

def cmd_clean(args):
    """Clean up files"""
    if args.all:
        output_dir = Path(config.OUTPUT_DIR)
        temp_dir = Path(config.TEMP_DIR)
        
        count = 0
        
        if output_dir.exists():
            for video in output_dir.glob('*.mp4'):
                video.unlink()
                count += 1
        
        downloader = ContentDownloader()
        downloader.cleanup_temp_files()
        
        print(f"✓ Cleaned {count} output videos and all temporary files")
    
    elif args.temp:
        downloader = ContentDownloader()
        downloader.cleanup_temp_files()
        print("✓ Cleaned temporary files")
    
    elif args.keep:
        clean_old_videos(keep_last_n=args.keep)
        print(f"✓ Kept last {args.keep} videos, deleted older ones")
    
    else:
        print("Please specify --all, --temp, or --keep N")

def cmd_stats():
    """Show statistics"""
    print_statistics()

def cmd_disk():
    """Show disk usage"""
    usage = get_disk_usage()
    
    print("\n" + "="*60)
    print("  DISK USAGE")
    print("="*60)
    print(f"\nOutput Directory: {usage['output_mb']:.2f} MB")
    print(f"Temp Directory:   {usage['temp_mb']:.2f} MB")
    print(f"Total:            {usage['total_mb']:.2f} MB")
    print("="*60 + "\n")

def cmd_config():
    """Show configuration"""
    print("\n" + "="*60)
    print("  CONFIGURATION")
    print("="*60)
    
    print(f"\nOutput Directory: {config.OUTPUT_DIR}")
    print(f"Temp Directory:   {config.TEMP_DIR}")
    
    print(f"\nVideo Settings:")
    print(f"  Max Length:     {config.MAX_VIDEO_LENGTH}s")
    print(f"  Min Length:     {config.MIN_VIDEO_LENGTH}s")
    print(f"  Clips per Video: {config.CLIPS_PER_VIDEO}")
    print(f"  Resolution:     {config.VIDEO_RESOLUTION}")
    
    print(f"\nScheduling:")
    print(f"  Interval:       Every {config.GENERATION_INTERVAL_HOURS} hour(s)")
    
    print(f"\nTheme Keywords ({len(config.MOTIVATIONAL_KEYWORDS)}):")
    for kw in config.MOTIVATIONAL_KEYWORDS:
        print(f"  • {kw}")
    
    print(f"\nMotivational Quotes ({len(config.MOTIVATIONAL_QUOTES)}):")
    for quote in config.MOTIVATIONAL_QUOTES[:5]:
        print(f"  • {quote}")
    if len(config.MOTIVATIONAL_QUOTES) > 5:
        print(f"  ... and {len(config.MOTIVATIONAL_QUOTES) - 5} more")
    
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description='Manage the motivational content generator'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    subparsers.add_parser('list', help='List all generated videos')
    
    clean_parser = subparsers.add_parser('clean', help='Clean up files')
    clean_parser.add_argument('--all', action='store_true', help='Delete all videos and temp files')
    clean_parser.add_argument('--temp', action='store_true', help='Delete only temp files')
    clean_parser.add_argument('--keep', type=int, metavar='N', help='Keep last N videos, delete older')
    
    subparsers.add_parser('stats', help='Show statistics')
    subparsers.add_parser('disk', help='Show disk usage')
    subparsers.add_parser('config', help='Show configuration')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == 'list':
            cmd_list()
        elif args.command == 'clean':
            cmd_clean(args)
        elif args.command == 'stats':
            cmd_stats()
        elif args.command == 'disk':
            cmd_disk()
        elif args.command == 'config':
            cmd_config()
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
