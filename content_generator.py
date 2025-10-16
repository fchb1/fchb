import os
import time
from datetime import datetime
from pathlib import Path
from typing import List
import config
from downloader import ContentDownloader
from video_processor import VideoProcessor

class ContentGenerator:
    def __init__(self):
        self.downloader = ContentDownloader()
        self.processor = VideoProcessor()
        self.source_videos = []
    
    def initialize_source_library(self, num_videos: int = 30):
        """Download and build a library of source videos"""
        print("Initializing source video library...")
        print("=" * 60)
        
        self.source_videos = self.downloader.collect_source_videos(num_videos)
        
        print(f"\nCollected {len(self.source_videos)} source videos")
        print("=" * 60)
    
    def generate_content(self, num_videos: int = 1) -> List[str]:
        """Generate new content by mashing up source videos"""
        if not self.source_videos:
            print("No source videos available. Initializing library...")
            self.initialize_source_library()
        
        if not self.source_videos:
            print("Failed to collect source videos. Cannot generate content.")
            return []
        
        print(f"\nGenerating {num_videos} new video(s)...")
        print("=" * 60)
        
        created_videos = self.processor.create_multiple_videos(
            self.source_videos, 
            num_videos=num_videos
        )
        
        print(f"\nSuccessfully created {len(created_videos)} video(s)")
        for video in created_videos:
            print(f"  - {video}")
        print("=" * 60)
        
        return created_videos
    
    def run_once(self):
        """Run a single generation cycle"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{'='*60}")
        print(f"Starting content generation at {timestamp}")
        print(f"{'='*60}")
        
        created_videos = self.generate_content(num_videos=1)
        
        if created_videos:
            print(f"\n✓ Generation cycle completed successfully")
            print(f"  Output directory: {config.OUTPUT_DIR}")
        else:
            print(f"\n✗ Generation cycle failed")
        
        return created_videos
    
    def refresh_source_library(self):
        """Refresh the source video library with new content"""
        print("\nRefreshing source video library...")
        self.downloader.cleanup_temp_files()
        self.initialize_source_library()
    
    def get_stats(self) -> dict:
        """Get statistics about the generator"""
        output_path = Path(config.OUTPUT_DIR)
        output_videos = list(output_path.glob('*.mp4')) if output_path.exists() else []
        
        temp_path = Path(config.TEMP_DIR)
        temp_videos = list(temp_path.glob('*')) if temp_path.exists() else []
        
        return {
            'source_videos': len(self.source_videos),
            'generated_videos': len(output_videos),
            'temp_files': len(temp_videos),
            'output_dir': str(output_path.absolute()),
            'temp_dir': str(temp_path.absolute())
        }
    
    def cleanup(self):
        """Clean up temporary files"""
        print("\nCleaning up temporary files...")
        self.downloader.cleanup_temp_files()
        print("Cleanup complete")
