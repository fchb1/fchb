import random
from pathlib import Path
from typing import List, Tuple
from moviepy.editor import (
    VideoFileClip, 
    concatenate_videoclips, 
    TextClip, 
    CompositeVideoClip,
    ColorClip
)
from moviepy.video.fx.all import crop, resize
import config

class VideoProcessor:
    def __init__(self):
        self.output_dir = Path(config.OUTPUT_DIR)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.target_width = 1080
        self.target_height = 1920
    
    def extract_random_clip(self, video_path: str, duration: float = None) -> VideoFileClip:
        """Extract a random segment from a video"""
        try:
            clip = VideoFileClip(video_path)
            
            if duration is None:
                duration = min(random.uniform(5, 15), clip.duration)
            
            if clip.duration <= duration:
                start_time = 0
            else:
                start_time = random.uniform(0, clip.duration - duration)
            
            extracted = clip.subclip(start_time, min(start_time + duration, clip.duration))
            
            processed = self.process_to_vertical(extracted)
            
            return processed
        
        except Exception as e:
            print(f"Error extracting clip from {video_path}: {e}")
            return None
    
    def process_to_vertical(self, clip: VideoFileClip) -> VideoFileClip:
        """Convert video to vertical 9:16 format"""
        w, h = clip.size
        target_aspect = self.target_height / self.target_width
        current_aspect = h / w
        
        if current_aspect < target_aspect:
            new_w = int(h / target_aspect)
            x_center = w / 2
            x1 = int(x_center - new_w / 2)
            clip = crop(clip, x1=x1, width=new_w, y1=0, height=h)
        else:
            new_h = int(w * target_aspect)
            y_center = h / 2
            y1 = int(y_center - new_h / 2)
            clip = crop(clip, x1=0, width=w, y1=y1, height=new_h)
        
        clip = resize(clip, height=self.target_height)
        
        return clip
    
    def add_text_overlay(self, clip: VideoFileClip, text: str, position: str = 'center') -> CompositeVideoClip:
        """Add text overlay to video clip"""
        try:
            txt_clip = TextClip(
                text,
                fontsize=config.TEXT_STYLES['fontsize'],
                color=config.TEXT_STYLES['color'],
                font='Arial-Bold',
                stroke_color=config.TEXT_STYLES['stroke_color'],
                stroke_width=config.TEXT_STYLES['stroke_width'],
                method='caption',
                size=(self.target_width - 100, None),
                align='center'
            )
            
            txt_clip = txt_clip.set_duration(clip.duration)
            
            if position == 'top':
                txt_clip = txt_clip.set_position(('center', 100))
            elif position == 'bottom':
                txt_clip = txt_clip.set_position(('center', self.target_height - 300))
            else:
                txt_clip = txt_clip.set_position('center')
            
            video = CompositeVideoClip([clip, txt_clip])
            
            return video
        
        except Exception as e:
            print(f"Error adding text overlay: {e}")
            return clip
    
    def create_mashup(self, video_paths: List[str], target_duration: float = None) -> str:
        """Create a mashup from multiple video clips"""
        if not video_paths:
            print("No video paths provided")
            return None
        
        if target_duration is None:
            target_duration = random.uniform(config.MIN_VIDEO_LENGTH, config.MAX_VIDEO_LENGTH)
        
        clips = []
        total_duration = 0
        clip_duration = target_duration / config.CLIPS_PER_VIDEO
        
        random.shuffle(video_paths)
        
        for video_path in video_paths[:config.CLIPS_PER_VIDEO]:
            clip = self.extract_random_clip(video_path, duration=clip_duration)
            if clip:
                clips.append(clip)
                total_duration += clip.duration
                
                if total_duration >= target_duration:
                    break
        
        if not clips:
            print("No clips successfully extracted")
            return None
        
        try:
            quote = random.choice(config.MOTIVATIONAL_QUOTES)
            quote_clip = clips[len(clips) // 2] if len(clips) > 1 else clips[0]
            quote_position = random.choice(['top', 'center', 'bottom'])
            clips[clips.index(quote_clip)] = self.add_text_overlay(quote_clip, quote, quote_position)
            
            final_clip = concatenate_videoclips(clips, method="compose")
            
            output_filename = f"motivational_{random.randint(1000, 9999)}.mp4"
            output_path = self.output_dir / output_filename
            
            final_clip.write_videofile(
                str(output_path),
                fps=30,
                codec='libx264',
                audio_codec='aac',
                preset='medium',
                threads=4
            )
            
            for clip in clips:
                clip.close()
            
            print(f"Created mashup: {output_path}")
            return str(output_path)
        
        except Exception as e:
            print(f"Error creating mashup: {e}")
            for clip in clips:
                try:
                    clip.close()
                except:
                    pass
            return None
    
    def create_multiple_videos(self, video_paths: List[str], num_videos: int = 1) -> List[str]:
        """Create multiple mashup videos"""
        created_videos = []
        
        for i in range(num_videos):
            print(f"Creating video {i+1}/{num_videos}...")
            video = self.create_mashup(video_paths)
            if video:
                created_videos.append(video)
        
        return created_videos
