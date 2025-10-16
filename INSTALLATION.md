# Installation Guide

Complete step-by-step installation instructions for the Motivational Content Generator.

## System Requirements

### Operating System
- Linux (Ubuntu 20.04+, Debian 10+, CentOS 8+)
- macOS (10.15+)
- Windows (10/11 with WSL2)

### Software Prerequisites
- Python 3.8 or higher
- FFmpeg
- Git (for cloning)
- 2GB RAM minimum
- 5GB free disk space

## Quick Installation (Recommended)

### Linux / macOS

```bash
# 1. Clone the repository
git clone <repository-url>
cd motivational-content-generator

# 2. Run quick start script
./quick_start.sh

# 3. Activate virtual environment
source venv/bin/activate

# 4. Test the installation
python test_generator.py

# 5. Generate your first video
python main.py once
```

That's it! Your video will be in the `output/` directory.

## Manual Installation

### Step 1: Install System Dependencies

#### Ubuntu / Debian
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv ffmpeg git
```

#### macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python ffmpeg git
```

#### Windows (WSL2)
```bash
# First, enable WSL2 and install Ubuntu from Microsoft Store
# Then, in Ubuntu terminal:
sudo apt update
sudo apt install -y python3 python3-pip python3-venv ffmpeg git
```

### Step 2: Clone Repository

```bash
git clone <repository-url>
cd motivational-content-generator
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment

#### Linux / macOS
```bash
source venv/bin/activate
```

#### Windows (WSL2)
```bash
source venv/bin/activate
```

### Step 5: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 6: (Optional) Install API Dependencies

If you want to use the REST API:

```bash
pip install -r requirements-api.txt
```

### Step 7: Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit configuration (optional)
nano .env
```

### Step 8: Create Directories

```bash
mkdir -p output temp
```

### Step 9: Test Installation

```bash
python test_generator.py
```

All tests should pass. If any fail, check the error messages and ensure all dependencies are installed.

### Step 10: Generate First Video

```bash
python main.py once
```

## Docker Installation

### Prerequisites
- Docker (20.10+)
- Docker Compose (1.29+)

### Installation Steps

```bash
# 1. Clone repository
git clone <repository-url>
cd motivational-content-generator

# 2. Build and start
docker-compose up -d

# 3. View logs
docker-compose logs -f

# 4. Stop when needed
docker-compose down
```

Videos will be generated in the `output/` directory on your host machine.

## Verification

### Check Python Version
```bash
python3 --version
# Should be 3.8 or higher
```

### Check FFmpeg
```bash
ffmpeg -version
# Should show FFmpeg version info
```

### Check Dependencies
```bash
pip list
# Should show all required packages
```

### Run Test Suite
```bash
python test_generator.py
# All tests should pass
```

## Troubleshooting Installation

### Python Not Found
```bash
# Ubuntu/Debian
sudo apt install python3

# macOS
brew install python
```

### FFmpeg Not Found
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Verify installation
ffmpeg -version
```

### Permission Denied on quick_start.sh
```bash
chmod +x quick_start.sh
./quick_start.sh
```

### Virtual Environment Issues
```bash
# Remove old venv
rm -rf venv

# Create new one
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Module Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### MoviePy Installation Fails
```bash
# Install system dependencies first
sudo apt install -y libsm6 libxext6 libxrender-dev

# Then reinstall
pip install moviepy
```

## Platform-Specific Notes

### Ubuntu 20.04+
- All dependencies available in default repositories
- Recommended for production deployment

### macOS
- Requires Xcode Command Line Tools
- Install with: `xcode-select --install`

### Windows
- WSL2 recommended over native Windows
- Native Windows support limited for video processing

### Raspberry Pi
- Works on Pi 4 with 4GB+ RAM
- Video generation is slower
- Consider using for light workloads

## Post-Installation

### Configuration

Edit `.env` file:
```bash
nano .env
```

Adjust these settings:
- `OUTPUT_DIR` - Where videos are saved
- `TEMP_DIR` - Temporary file location
- `MAX_VIDEO_LENGTH` - Maximum video duration
- `CLIPS_PER_VIDEO` - Clips to combine

### Customization

Edit `config.py` to customize:
- Motivational keywords
- Quote library
- Text styling
- Creator references

### First Run

```bash
# Generate one video to test
python main.py once

# Check the output
ls -lh output/

# View video info
python manage.py list
```

## Upgrading

### Update Code
```bash
git pull origin main
```

### Update Dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

### Update Docker
```bash
docker-compose down
docker-compose pull
docker-compose up -d --build
```

## Uninstallation

### Remove Application
```bash
# Stop any running processes
# Ctrl+C if running in terminal

# Remove virtual environment
rm -rf venv

# Remove generated content (optional)
rm -rf output temp

# Remove application
cd ..
rm -rf motivational-content-generator
```

### Remove Docker
```bash
docker-compose down
docker image rm motivational-content-gen
```

### Remove System Dependencies (Optional)
```bash
# Ubuntu/Debian
sudo apt remove ffmpeg

# macOS
brew uninstall ffmpeg
```

## Next Steps

After installation:

1. **Read Documentation**
   - README.md for overview
   - QUICK_REFERENCE.md for commands
   - USAGE_GUIDE.md for details

2. **Test the Tool**
   - Run `python demo.py`
   - Generate test videos
   - Review output quality

3. **Customize**
   - Edit keywords in config.py
   - Add custom quotes
   - Adjust video parameters

4. **Production**
   - Set up hourly generation
   - Configure systemd service
   - Or use Docker deployment

5. **Monitor**
   - Check disk usage
   - Review generated content
   - Adjust settings as needed

## Support

If you encounter issues:

1. Run test suite: `python test_generator.py`
2. Check error messages carefully
3. Review troubleshooting section
4. Verify all dependencies installed
5. Check system requirements met

## Additional Resources

- **README.md** - Project overview
- **USAGE_GUIDE.md** - Detailed usage
- **QUICK_REFERENCE.md** - Command reference
- **PROJECT_OVERVIEW.md** - Technical details

---

Happy content generating! 🚀
