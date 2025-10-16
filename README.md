# Motivational Content Generator

An automated tool that creates short-form motivational content for YouTube Shorts and TikTok. The tool combines clips from top creators in the courage, mental strength, and self-belief categories to create engaging mashup videos.

## Features

- 🎬 **Automated Video Generation**: Creates short-form vertical videos (9:16 aspect ratio)
- ⏰ **Hourly Scheduling**: Generate content automatically every hour
- 🎯 **Themed Content**: Focuses on courage, mental strength, and believing in yourself
- 💬 **Motivational Overlays**: Adds inspirational quotes as text overlays
- 🎨 **Smart Video Processing**: Automatically crops and resizes videos to vertical format
- 📦 **Batch Processing**: Combine multiple clips from different sources

## Installation

### Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system

#### Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**MacOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create environment configuration:
```bash
cp .env.example .env
```

4. (Optional) Edit `.env` to customize settings:
```bash
nano .env
```

## Usage

### Generate a Single Video

Create one video immediately:
```bash
python main.py once
```

Create multiple videos:
```bash
python main.py once -n 5
```

### Run Hourly Generation

Generate new content every hour:
```bash
python main.py hourly
```

### Continuous Mode (Testing)

Generate content continuously with custom delay:
```bash
python main.py continuous -d 300  # Every 5 minutes
```

### Initialize Source Library Only

Download source videos without generating content:
```bash
python main.py once --init-only
```

## Configuration

Edit `.env` file to customize:

| Variable | Description | Default |
|----------|-------------|---------|
| `OUTPUT_DIR` | Directory for generated videos | `./output` |
| `TEMP_DIR` | Directory for temporary files | `./temp` |
| `MAX_VIDEO_LENGTH` | Maximum video length in seconds | `60` |
| `MIN_VIDEO_LENGTH` | Minimum video length in seconds | `15` |
| `CLIPS_PER_VIDEO` | Number of clips to combine | `3` |
| `GENERATION_INTERVAL_HOURS` | Hours between generations | `1` |
| `VIDEO_RESOLUTION` | Output video resolution | `1080x1920` |

## How It Works

1. **Source Collection**: Downloads motivational short-form videos based on keywords like "courage motivation", "mental strength", "believe in yourself"

2. **Clip Extraction**: Randomly extracts segments from source videos

3. **Video Processing**: 
   - Converts clips to vertical 9:16 format
   - Combines multiple clips into a single video
   - Adds motivational quote overlays

4. **Output**: Saves finished videos to the output directory, ready for upload

## Customization

### Add Custom Keywords

Edit `config.py` to add more search keywords:
```python
MOTIVATIONAL_KEYWORDS = [
    'your custom keyword',
    'another keyword',
    # ...
]
```

### Add Custom Quotes

Edit `config.py` to add your own motivational quotes:
```python
MOTIVATIONAL_QUOTES = [
    "Your custom quote here",
    # ...
]
```

### Adjust Text Styling

Modify `TEXT_STYLES` in `config.py`:
```python
TEXT_STYLES = {
    'fontsize': 70,
    'color': 'white',
    'stroke_color': 'black',
    'stroke_width': 3,
}
```

## Output

Generated videos are saved in the `output/` directory with filenames like:
- `motivational_1234.mp4`
- `motivational_5678.mp4`

Videos are optimized for:
- ✅ YouTube Shorts (9:16 vertical)
- ✅ TikTok (9:16 vertical)
- ✅ Instagram Reels (9:16 vertical)

## Project Structure

```
.
├── main.py                 # Main entry point
├── content_generator.py    # Core generation logic
├── downloader.py           # Video downloading functionality
├── video_processor.py      # Video editing and processing
├── scheduler.py            # Scheduling system
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
└── README.md              # Documentation
```

## Legal & Ethical Considerations

⚠️ **Important Notice:**

This tool downloads and remixes content from other creators. Before using this tool for commercial purposes:

1. **Copyright**: Ensure you have the right to use the source content
2. **Fair Use**: Understand fair use laws in your jurisdiction
3. **Attribution**: Consider crediting original creators
4. **Transformative Use**: Add significant original commentary or value
5. **Platform Rules**: Follow YouTube and TikTok's content policies

For educational and personal use only. Commercial use may require licenses or permissions from original content creators.

## Troubleshooting

### FFmpeg Not Found
```bash
# Verify FFmpeg installation
ffmpeg -version
```

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### No Videos Downloaded
- Check your internet connection
- Try different keywords
- YouTube may be rate-limiting requests

### Video Processing Errors
- Ensure FFmpeg is properly installed
- Check that source videos are valid
- Verify sufficient disk space

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is provided as-is for educational purposes. Users are responsible for ensuring their use complies with applicable laws and platform policies.
