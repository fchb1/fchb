#!/usr/bin/env python3
"""
Simple Flask API for the content generator
Allows remote control and monitoring
"""

try:
    from flask import Flask, jsonify, request, send_file
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False
    print("Flask not installed. Install with: pip install flask")

from pathlib import Path
import threading
from datetime import datetime
import config
from content_generator import ContentGenerator
from utils import list_generated_videos, get_disk_usage, print_statistics

if FLASK_AVAILABLE:
    app = Flask(__name__)
    generator = ContentGenerator()
    generation_lock = threading.Lock()
    
    # Store generation status
    status = {
        'generating': False,
        'last_generation': None,
        'total_generated': 0,
        'errors': []
    }
    
    @app.route('/')
    def index():
        """API documentation"""
        return jsonify({
            'name': 'Motivational Content Generator API',
            'version': '1.0',
            'endpoints': {
                '/status': 'GET - Get current status',
                '/generate': 'POST - Generate new video',
                '/videos': 'GET - List all generated videos',
                '/videos/<filename>': 'GET - Download specific video',
                '/stats': 'GET - Get statistics',
                '/config': 'GET - Get configuration',
                '/cleanup': 'POST - Clean up temp files'
            }
        })
    
    @app.route('/status')
    def get_status():
        """Get current generator status"""
        return jsonify(status)
    
    @app.route('/generate', methods=['POST'])
    def generate():
        """Generate new video(s)"""
        if status['generating']:
            return jsonify({'error': 'Generation already in progress'}), 409
        
        data = request.json or {}
        num_videos = data.get('num_videos', 1)
        
        if num_videos < 1 or num_videos > 10:
            return jsonify({'error': 'num_videos must be between 1 and 10'}), 400
        
        def generate_async():
            with generation_lock:
                try:
                    status['generating'] = True
                    status['errors'] = []
                    
                    if not generator.source_videos:
                        generator.initialize_source_library()
                    
                    videos = generator.generate_content(num_videos=num_videos)
                    
                    status['generating'] = False
                    status['last_generation'] = datetime.now().isoformat()
                    status['total_generated'] += len(videos)
                    
                except Exception as e:
                    status['generating'] = False
                    status['errors'].append(str(e))
        
        thread = threading.Thread(target=generate_async)
        thread.start()
        
        return jsonify({
            'message': f'Started generation of {num_videos} video(s)',
            'status': 'processing'
        })
    
    @app.route('/videos')
    def get_videos():
        """List all generated videos"""
        videos = list_generated_videos()
        return jsonify({
            'count': len(videos),
            'videos': videos
        })
    
    @app.route('/videos/<filename>')
    def download_video(filename):
        """Download a specific video"""
        video_path = Path(config.OUTPUT_DIR) / filename
        
        if not video_path.exists():
            return jsonify({'error': 'Video not found'}), 404
        
        return send_file(str(video_path), mimetype='video/mp4')
    
    @app.route('/stats')
    def get_stats():
        """Get generator statistics"""
        videos = list_generated_videos()
        disk = get_disk_usage()
        
        return jsonify({
            'videos_generated': len(videos),
            'disk_usage_mb': disk,
            'status': status
        })
    
    @app.route('/config')
    def get_config():
        """Get current configuration"""
        return jsonify({
            'output_dir': config.OUTPUT_DIR,
            'temp_dir': config.TEMP_DIR,
            'max_video_length': config.MAX_VIDEO_LENGTH,
            'min_video_length': config.MIN_VIDEO_LENGTH,
            'clips_per_video': config.CLIPS_PER_VIDEO,
            'generation_interval_hours': config.GENERATION_INTERVAL_HOURS,
            'keywords_count': len(config.MOTIVATIONAL_KEYWORDS),
            'quotes_count': len(config.MOTIVATIONAL_QUOTES)
        })
    
    @app.route('/cleanup', methods=['POST'])
    def cleanup():
        """Clean up temporary files"""
        if status['generating']:
            return jsonify({'error': 'Cannot cleanup while generating'}), 409
        
        generator.cleanup()
        
        return jsonify({'message': 'Cleanup complete'})
    
    def run_api(host='0.0.0.0', port=5000, debug=False):
        """Run the API server"""
        print(f"""
╔════════════════════════════════════════════════════════════╗
║     CONTENT GENERATOR API SERVER                           ║
╚════════════════════════════════════════════════════════════╝

API running on http://{host}:{port}

Endpoints:
  GET  /              - API documentation
  GET  /status        - Current status
  POST /generate      - Generate video(s)
  GET  /videos        - List videos
  GET  /videos/<name> - Download video
  GET  /stats         - Statistics
  GET  /config        - Configuration
  POST /cleanup       - Clean temp files

Example requests:
  curl http://{host}:{port}/status
  curl -X POST http://{host}:{port}/generate -H "Content-Type: application/json" -d '{{"num_videos": 1}}'
  curl http://{host}:{port}/videos

Press Ctrl+C to stop
        """)
        
        app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    if not FLASK_AVAILABLE:
        print("Please install Flask: pip install flask")
        exit(1)
    
    import argparse
    parser = argparse.ArgumentParser(description='Run the Content Generator API')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    run_api(host=args.host, port=args.port, debug=args.debug)
