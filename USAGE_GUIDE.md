# Usage Guide

Complete guide to using the Motivational Content Generator.

## Quick Start

### 1. First Time Setup

```bash
# Run the quick start script
./quick_start.sh
```

This will:
- Check for Python 3 and FFmpeg
- Create a virtual environment
- Install all dependencies
- Create necessary directories

### 2. Generate Your First Video

```bash
# Activate virtual environment
source venv/bin/activate

# Generate a single video
python main.py once
```

The tool will:
1. Download motivational videos from YouTube
2. Extract and process clips
3. Combine them with text overlays
4. Save the final video to `output/`

## Usage Modes

### One-Time Generation

Generate videos on demand:

```bash
# Generate 1 video
python main.py once

# Generate 5 videos
python main.py once -n 5

# Only download source videos (no generation)
python main.py once --init-only
```

### Hourly Mode (Production)

Automatically generate content every hour:

```bash
python main.py hourly
```

This mode:
- Generates a new video every hour
- Runs continuously until stopped (Ctrl+C)
- Refreshes source library every 10 generations
- Perfect for automated content pipelines

### Continuous Mode (Testing)

Generate content continuously with custom intervals:

```bash
# Generate every 60 seconds
python main.py continuous -d 60

# Generate every 5 minutes
python main.py continuous -d 300
```

Use this for testing and debugging.

## Management Commands

The `manage.py` script provides utilities for managing your content:

### List Generated Videos

```bash
python manage.py list
```

Shows all generated videos with details:
- Duration
- File size
- Resolution
- FPS
- File path

### Show Statistics

```bash
python manage.py stats
```

Displays:
- Number of videos generated
- Total size
- Average size per video
- Newest/oldest videos
- Temp file count

### Show Disk Usage

```bash
python manage.py disk
```

Shows disk space used by:
- Output directory
- Temp directory
- Total usage

### Clean Up Files

```bash
# Delete all videos and temp files
python manage.py clean --all

# Delete only temp files
python manage.py clean --temp

# Keep last 10 videos, delete older
python manage.py clean --keep 10
```

### Show Configuration

```bash
python manage.py config
```

Displays current configuration:
- Directory paths
- Video settings
- Keywords
- Quotes

## Configuration

### Environment Variables

Create/edit `.env` file:

```bash
# Directories
OUTPUT_DIR=./output
TEMP_DIR=./temp

# Video settings
MAX_VIDEO_LENGTH=60
MIN_VIDEO_LENGTH=15
CLIPS_PER_VIDEO=3
VIDEO_RESOLUTION=1080x1920

# Scheduling
GENERATION_INTERVAL_HOURS=1
```

### Customizing Keywords

Edit `config.py`:

```python
MOTIVATIONAL_KEYWORDS = [
    'your keyword here',
    'another keyword',
    # Add more...
]
```

These keywords are used to search for source videos on YouTube.

### Customizing Quotes

Edit `config.py`:

```python
MOTIVATIONAL_QUOTES = [
    "Your custom quote here",
    "Another inspiring quote",
    # Add more...
]
```

These quotes are randomly selected and added as text overlays.

### Customizing Text Style

Edit `config.py`:

```python
TEXT_STYLES = {
    'fontsize': 70,        # Size of text
    'color': 'white',      # Text color
    'stroke_color': 'black',  # Outline color
    'stroke_width': 3,     # Outline thickness
}
```

## Docker Deployment

### Using Docker Compose

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Using Docker Directly

```bash
# Build image
docker build -t motivational-content-gen .

# Run container
docker run -d \
  --name content-gen \
  -v $(pwd)/output:/app/output \
  -v $(pwd)/temp:/app/temp \
  motivational-content-gen
```

## Systemd Service (Linux)

### Setup

1. Edit `motivational-content-gen.service`:
   - Replace `/path/to/your/project` with actual path
   - Set correct user

2. Copy to systemd:
```bash
sudo cp motivational-content-gen.service /etc/systemd/system/
sudo systemctl daemon-reload
```

3. Enable and start:
```bash
sudo systemctl enable motivational-content-gen
sudo systemctl start motivational-content-gen
```

### Manage Service

```bash
# Check status
sudo systemctl status motivational-content-gen

# View logs
sudo journalctl -u motivational-content-gen -f

# Restart
sudo systemctl restart motivational-content-gen

# Stop
sudo systemctl stop motivational-content-gen
```

## Workflows

### Daily Content Pipeline

1. **Morning**: Generate 5 videos
```bash
python main.py once -n 5
```

2. **Review**: Check generated videos
```bash
python manage.py list
```

3. **Upload**: Use the videos in `output/` directory

4. **Cleanup**: Keep only recent videos
```bash
python manage.py clean --keep 20
```

### Automated 24/7 Generation

1. **Start**: Run in hourly mode
```bash
python main.py hourly
```

2. **Monitor**: Check periodically
```bash
python manage.py stats
```

3. **Manage Storage**: Clean up weekly
```bash
python manage.py clean --keep 50
```

### Testing New Settings

1. **Edit Configuration**: Modify `config.py`

2. **Test**: Generate one video
```bash
python main.py once
```

3. **Review**: Check the output

4. **Iterate**: Adjust settings and repeat

## Tips & Best Practices

### Optimize Video Quality

- Use higher resolution source videos
- Adjust `CLIPS_PER_VIDEO` for more variety
- Experiment with different durations

### Manage Storage

- Regularly clean temp files
- Keep only needed videos
- Monitor disk usage

### Content Variety

- Add more keywords for diverse content
- Update quotes regularly
- Refresh source library frequently

### Performance

- Close other heavy applications
- Ensure good internet connection
- Use SSD for faster processing

### Troubleshooting

**No videos downloaded:**
- Check internet connection
- Try different keywords
- Verify YouTube access

**Video processing errors:**
- Ensure FFmpeg is installed
- Check source video quality
- Verify disk space

**Out of memory:**
- Reduce `CLIPS_PER_VIDEO`
- Process fewer videos at once
- Close other applications

## Advanced Usage

### Custom Source Videos

Add your own source videos:

```python
from downloader import ContentDownloader

downloader = ContentDownloader()
downloader.download_from_url('https://youtube.com/...')
```

### Batch Processing

Generate multiple videos with different settings:

```python
from content_generator import ContentGenerator

generator = ContentGenerator()
generator.initialize_source_library()

# Generate 10 videos
for i in range(10):
    generator.generate_content(num_videos=1)
```

### Integration with Upload APIs

After generation, automatically upload:

```python
from content_generator import ContentGenerator
# Your upload function
from my_uploader import upload_to_youtube, upload_to_tiktok

generator = ContentGenerator()
videos = generator.generate_content(num_videos=1)

for video in videos:
    upload_to_youtube(video)
    upload_to_tiktok(video)
```

## Support

For issues, questions, or contributions:
- Check the README.md
- Review error messages
- Verify configuration
- Check system requirements
