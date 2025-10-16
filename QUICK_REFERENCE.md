# Quick Reference Guide

## Installation

```bash
# Quick setup
./quick_start.sh

# Manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Basic Commands

### Generate Videos

```bash
# Single video
python main.py once

# Multiple videos
python main.py once -n 5

# Hourly generation
python main.py hourly

# Custom interval (seconds)
python main.py continuous -d 300
```

### Management

```bash
# List videos
python manage.py list

# Show statistics
python manage.py stats

# Show disk usage
python manage.py disk

# Show config
python manage.py config

# Clean up
python manage.py clean --temp
python manage.py clean --all
python manage.py clean --keep 10
```

### Testing

```bash
# Run tests
python test_generator.py

# Run demo
python demo.py
```

### API Server

```bash
# Start API
python api.py

# Custom host/port
python api.py --host 0.0.0.0 --port 8080
```

## API Endpoints

```bash
# Get status
curl http://localhost:5000/status

# Generate video
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"num_videos": 1}'

# List videos
curl http://localhost:5000/videos

# Get stats
curl http://localhost:5000/stats

# Download video
curl http://localhost:5000/videos/motivational_1234.mp4 -o video.mp4
```

## Configuration Files

### .env
```bash
OUTPUT_DIR=./output
TEMP_DIR=./temp
MAX_VIDEO_LENGTH=60
MIN_VIDEO_LENGTH=15
CLIPS_PER_VIDEO=3
GENERATION_INTERVAL_HOURS=1
VIDEO_RESOLUTION=1080x1920
```

### config.py
- `MOTIVATIONAL_KEYWORDS` - Search keywords
- `MOTIVATIONAL_QUOTES` - Text overlays
- `TEXT_STYLES` - Font styling

## Docker

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down

# Rebuild
docker-compose up -d --build
```

## Systemd Service

```bash
# Install
sudo cp motivational-content-gen.service /etc/systemd/system/
sudo systemctl daemon-reload

# Start
sudo systemctl start motivational-content-gen

# Enable auto-start
sudo systemctl enable motivational-content-gen

# Status
sudo systemctl status motivational-content-gen

# Logs
sudo journalctl -u motivational-content-gen -f
```

## Common Workflows

### Generate & Upload Daily
```bash
# Morning: Generate 5 videos
python main.py once -n 5

# Review in output/ directory
python manage.py list

# Upload to platforms
# (manual or use upload scripts)

# Evening: Clean up
python manage.py clean --keep 20
```

### 24/7 Automation
```bash
# Option 1: Screen session
screen -S content-gen
python main.py hourly
# Ctrl+A, D to detach

# Option 2: Systemd
sudo systemctl start motivational-content-gen

# Option 3: Docker
docker-compose up -d
```

## Troubleshooting

### FFmpeg not found
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# MacOS
brew install ffmpeg
```

### Dependencies missing
```bash
pip install -r requirements.txt --force-reinstall
```

### No videos downloaded
- Check internet connection
- Try different keywords in config.py
- Verify YouTube access

### Disk full
```bash
python manage.py clean --all
python manage.py disk
```

## Directory Structure

```
project/
├── output/          # Generated videos
├── temp/            # Temporary files
├── examples/        # Example scripts
└── [source files]
```

## File Locations

- **Generated Videos**: `./output/motivational_*.mp4`
- **Temp Files**: `./temp/`
- **Configuration**: `.env` and `config.py`
- **Logs**: Terminal output (redirect as needed)

## Environment Setup

```bash
# Activate venv
source venv/bin/activate

# Deactivate venv
deactivate

# Update dependencies
pip install -r requirements.txt --upgrade
```

## Performance Tips

1. Close heavy applications
2. Use SSD storage
3. Stable internet connection
4. Regular cleanup
5. Monitor resources with `python manage.py stats`

## Getting Help

1. Check README.md
2. Read USAGE_GUIDE.md
3. Run test suite: `python test_generator.py`
4. Review examples in `examples/`
5. Check error messages

## Quick Edits

### Change video length
Edit `.env`:
```
MAX_VIDEO_LENGTH=45
MIN_VIDEO_LENGTH=20
```

### Add keywords
Edit `config.py`:
```python
MOTIVATIONAL_KEYWORDS = [
    'your keyword here',
    # ...
]
```

### Change generation frequency
Edit `.env`:
```
GENERATION_INTERVAL_HOURS=2
```

## Output Formats

All videos are:
- ✅ 9:16 vertical (1080x1920)
- ✅ MP4 format (H.264)
- ✅ 15-60 seconds
- ✅ Ready for YouTube Shorts & TikTok

## Best Practices

1. Test with `once` before running `hourly`
2. Monitor disk space regularly
3. Keep last 20-50 videos
4. Refresh source library weekly
5. Update keywords monthly
6. Back up successful videos
7. Review platform guidelines
