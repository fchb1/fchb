"""
Utility functions for the content generator
"""

import os
from pathlib import Path
from typing import List
import config

def get_video_info(video_path: str) -> dict:
    """Get information about a video file"""
    from moviepy.editor import VideoFileClip
    
    try:
        clip = VideoFileClip(video_path)
        info = {
            'path': video_path,
            'duration': clip.duration,
            'size': clip.size,
            'fps': clip.fps,
            'file_size_mb': Path(video_path).stat().st_size / 1024 / 1024
        }
        clip.close()
        return info
    except Exception as e:
        return {'error': str(e)}

def list_generated_videos() -> List[dict]:
    """List all generated videos with their info"""
    output_dir = Path(config.OUTPUT_DIR)
    
    if not output_dir.exists():
        return []
    
    videos = []
    for video_path in output_dir.glob('*.mp4'):
        info = get_video_info(str(video_path))
        videos.append(info)
    
    return videos

def clean_old_videos(keep_last_n: int = 10):
    """Keep only the last N generated videos"""
    output_dir = Path(config.OUTPUT_DIR)
    
    if not output_dir.exists():
        return
    
    video_files = sorted(
        output_dir.glob('*.mp4'),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    
    for video_file in video_files[keep_last_n:]:
        try:
            video_file.unlink()
            print(f"Deleted old video: {video_file.name}")
        except Exception as e:
            print(f"Error deleting {video_file.name}: {e}")

def get_disk_usage() -> dict:
    """Get disk usage statistics"""
    output_dir = Path(config.OUTPUT_DIR)
    temp_dir = Path(config.TEMP_DIR)
    
    def get_dir_size(path: Path) -> float:
        if not path.exists():
            return 0
        total = sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
        return total / 1024 / 1024
    
    return {
        'output_mb': get_dir_size(output_dir),
        'temp_mb': get_dir_size(temp_dir),
        'total_mb': get_dir_size(output_dir) + get_dir_size(temp_dir)
    }

def format_duration(seconds: float) -> str:
    """Format duration in human-readable format"""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"

def print_statistics():
    """Print detailed statistics about the generator"""
    output_dir = Path(config.OUTPUT_DIR)
    temp_dir = Path(config.TEMP_DIR)
    
    print("\n" + "="*60)
    print("  CONTENT GENERATOR STATISTICS")
    print("="*60)
    
    if output_dir.exists():
        videos = list(output_dir.glob('*.mp4'))
        print(f"\nGenerated Videos: {len(videos)}")
        
        if videos:
            total_size = sum(v.stat().st_size for v in videos) / 1024 / 1024
            print(f"Total Size: {total_size:.2f} MB")
            print(f"Average Size: {total_size/len(videos):.2f} MB per video")
            
            print(f"\nNewest: {videos[-1].name}")
            print(f"Oldest: {videos[0].name}")
    else:
        print("\nGenerated Videos: 0")
    
    if temp_dir.exists():
        temp_files = list(temp_dir.glob('*'))
        print(f"\nTemporary Files: {len(temp_files)}")
        if temp_files:
            temp_size = sum(f.stat().st_size for f in temp_files if f.is_file()) / 1024 / 1024
            print(f"Temp Size: {temp_size:.2f} MB")
    else:
        print("\nTemporary Files: 0")
    
    usage = get_disk_usage()
    print(f"\nTotal Disk Usage: {usage['total_mb']:.2f} MB")
    print("="*60)
