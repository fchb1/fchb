import schedule
import time
from datetime import datetime
import config
from content_generator import ContentGenerator

class ContentScheduler:
    def __init__(self):
        self.generator = ContentGenerator()
        self.running = False
        self.generation_count = 0
    
    def setup(self):
        """Initialize the content generator"""
        print("Setting up Content Generation Tool")
        print("=" * 60)
        print(f"Configuration:")
        print(f"  - Generation Interval: Every {config.GENERATION_INTERVAL_HOURS} hour(s)")
        print(f"  - Video Length: {config.MIN_VIDEO_LENGTH}-{config.MAX_VIDEO_LENGTH} seconds")
        print(f"  - Clips Per Video: {config.CLIPS_PER_VIDEO}")
        print(f"  - Output Directory: {config.OUTPUT_DIR}")
        print("=" * 60)
        
        self.generator.initialize_source_library()
    
    def generate_job(self):
        """Job to be run on schedule"""
        self.generation_count += 1
        print(f"\n\n{'#'*60}")
        print(f"# GENERATION CYCLE #{self.generation_count}")
        print(f"# Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'#'*60}")
        
        try:
            self.generator.run_once()
            
            if self.generation_count % 10 == 0:
                print("\nRefreshing source library (every 10 generations)...")
                self.generator.refresh_source_library()
        
        except Exception as e:
            print(f"Error during generation cycle: {e}")
    
    def run_hourly(self):
        """Run the content generator on hourly schedule"""
        self.running = True
        
        schedule.every(config.GENERATION_INTERVAL_HOURS).hours.do(self.generate_job)
        
        print("\n" + "=" * 60)
        print("Scheduler started!")
        print(f"Next generation in {config.GENERATION_INTERVAL_HOURS} hour(s)")
        print("Press Ctrl+C to stop")
        print("=" * 60)
        
        self.generate_job()
        
        try:
            while self.running:
                schedule.run_pending()
                time.sleep(60)
        
        except KeyboardInterrupt:
            print("\n\nStopping scheduler...")
            self.running = False
            self.cleanup()
    
    def run_continuous(self, delay_seconds: int = 60):
        """Run continuously with custom delay (for testing)"""
        self.running = True
        
        print("\n" + "=" * 60)
        print("Continuous mode started!")
        print(f"Generating new content every {delay_seconds} seconds")
        print("Press Ctrl+C to stop")
        print("=" * 60)
        
        try:
            while self.running:
                self.generate_job()
                
                if self.running:
                    print(f"\nWaiting {delay_seconds} seconds until next generation...")
                    time.sleep(delay_seconds)
        
        except KeyboardInterrupt:
            print("\n\nStopping continuous mode...")
            self.running = False
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        print("\nCleaning up resources...")
        self.generator.cleanup()
        print("Shutdown complete")
        
        stats = self.generator.get_stats()
        print("\nFinal Statistics:")
        print(f"  - Total generations: {self.generation_count}")
        print(f"  - Videos created: {stats['generated_videos']}")
        print(f"  - Output directory: {stats['output_dir']}")
