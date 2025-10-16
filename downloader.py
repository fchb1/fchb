import os
import yt_dlp
import random
from pathlib import Path
from typing import List
import config

class ContentDownloader:
    def __init__(self):
        self.temp_dir = Path(config.TEMP_DIR)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def download_youtube_shorts(self, search_query: str, max_results: int = 10) -> List[str]:
        """Download YouTube Shorts based on search query"""
        downloaded_files = []
        
        ydl_opts = {
            'format': 'best[height<=1920]',
            'outtmpl': str(self.temp_dir / '%(id)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'max_downloads': max_results,
            'match_filter': self._filter_shorts,
        }
        
        search_url = f"ytsearch{max_results}:{search_query} shorts"
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(search_url, download=True)
                
                if 'entries' in info:
                    for entry in info['entries']:
                        if entry:
                            video_id = entry.get('id', '')
                            for ext in ['mp4', 'webm', 'mkv']:
                                video_path = self.temp_dir / f"{video_id}.{ext}"
                                if video_path.exists():
                                    downloaded_files.append(str(video_path))
                                    break
            
            print(f"Downloaded {len(downloaded_files)} videos for query: {search_query}")
            return downloaded_files
        
        except Exception as e:
            print(f"Error downloading YouTube Shorts: {e}")
            return downloaded_files
    
    def _filter_shorts(self, info_dict):
        """Filter to only get short videos (under 60 seconds)"""
        duration = info_dict.get('duration', 0)
        if duration and duration <= 60:
            return None
        return "Video too long"
    
    def download_from_url(self, url: str) -> str:
        """Download a specific video from URL"""
        ydl_opts = {
            'format': 'best[height<=1920]',
            'outtmpl': str(self.temp_dir / '%(id)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_id = info.get('id', '')
                
                for ext in ['mp4', 'webm', 'mkv']:
                    video_path = self.temp_dir / f"{video_id}.{ext}"
                    if video_path.exists():
                        print(f"Downloaded video from URL: {url}")
                        return str(video_path)
            
            return None
        
        except Exception as e:
            print(f"Error downloading from URL {url}: {e}")
            return None
    
    def get_random_keyword(self) -> str:
        """Get a random motivational keyword"""
        return random.choice(config.MOTIVATIONAL_KEYWORDS)
    
    def collect_source_videos(self, num_videos: int = 20) -> List[str]:
        """Collect source videos from multiple search queries"""
        all_videos = []
        keywords = random.sample(config.MOTIVATIONAL_KEYWORDS, 
                                min(3, len(config.MOTIVATIONAL_KEYWORDS)))
        
        for keyword in keywords:
            videos = self.download_youtube_shorts(keyword, max_results=num_videos // len(keywords) + 1)
            all_videos.extend(videos)
        
        return all_videos
    
    def cleanup_temp_files(self):
        """Clean up temporary downloaded files"""
        for file in self.temp_dir.glob('*'):
            try:
                if file.is_file():
                    file.unlink()
            except Exception as e:
                print(f"Error deleting {file}: {e}")
