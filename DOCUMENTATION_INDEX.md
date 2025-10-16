# Documentation Index

Complete guide to all documentation available for the Motivational Content Generator.

## 📚 Core Documentation

### [README.md](README.md)
**Start here!** Main documentation covering:
- Project overview
- Quick installation
- Basic usage
- Configuration
- Troubleshooting
- Legal considerations

### [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
**Quick lookup** for common commands and tasks:
- All CLI commands
- API endpoints
- Configuration snippets
- Common workflows
- Troubleshooting checklist

### [USAGE_GUIDE.md](USAGE_GUIDE.md)
**Comprehensive guide** with detailed explanations:
- Installation walkthrough
- All usage modes
- Management commands
- Docker deployment
- Systemd setup
- Workflows and best practices

### [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
**Technical deep-dive** into the project:
- Architecture overview
- Component descriptions
- Technology stack
- File structure
- Development guidelines
- Future roadmap

## 🚀 Getting Started Path

1. **First Time Users**
   ```
   README.md → Quick Start section → Run ./quick_start.sh
   ```

2. **Learning the Tool**
   ```
   USAGE_GUIDE.md → Try examples → Experiment with settings
   ```

3. **Daily Reference**
   ```
   QUICK_REFERENCE.md → Find command → Execute
   ```

4. **Deep Understanding**
   ```
   PROJECT_OVERVIEW.md → Understand architecture → Extend features
   ```

## 📖 Specific Topics

### Installation & Setup
- README.md - "Installation" section
- USAGE_GUIDE.md - "Installation" section
- quick_start.sh - Automated setup script

### Basic Usage
- README.md - "Usage" section
- QUICK_REFERENCE.md - "Basic Commands"
- USAGE_GUIDE.md - "Usage Modes"

### Configuration
- README.md - "Configuration" section
- USAGE_GUIDE.md - "Configuration" section
- QUICK_REFERENCE.md - "Configuration Files"
- config.py - Source code with comments

### API Usage
- README.md - Brief API mention
- api.py - Full API implementation
- QUICK_REFERENCE.md - "API Endpoints"
- examples/api_client.py - Working example

### Docker Deployment
- Dockerfile - Docker image definition
- docker-compose.yml - Compose configuration
- USAGE_GUIDE.md - "Docker Deployment"
- QUICK_REFERENCE.md - "Docker" section

### System Service
- motivational-content-gen.service - Service file
- USAGE_GUIDE.md - "Systemd Service" section
- QUICK_REFERENCE.md - "Systemd Service" section

### Management & Maintenance
- manage.py - Management CLI tool
- USAGE_GUIDE.md - "Management Commands"
- QUICK_REFERENCE.md - "Management" section

### Troubleshooting
- README.md - "Troubleshooting" section
- USAGE_GUIDE.md - Tips throughout
- QUICK_REFERENCE.md - "Troubleshooting" section
- test_generator.py - Diagnostic tool

## 🔧 Code Documentation

### Main Application Files

#### [main.py](main.py)
Entry point for the application
- Command-line interface
- Mode selection (once/hourly/continuous)
- Argument parsing

#### [content_generator.py](content_generator.py)
Core content generation logic
- Source library management
- Video generation orchestration
- Statistics tracking

#### [downloader.py](downloader.py)
Video downloading functionality
- YouTube Shorts downloading
- Keyword-based search
- URL-based downloading

#### [video_processor.py](video_processor.py)
Video editing and processing
- Clip extraction
- Vertical format conversion
- Text overlay generation
- Video combination

#### [scheduler.py](scheduler.py)
Scheduling system
- Hourly generation
- Continuous mode
- Job management

#### [config.py](config.py)
Configuration settings
- Keywords and quotes
- Video parameters
- Text styling
- Directory paths

#### [utils.py](utils.py)
Utility functions
- Video information
- Disk usage
- Statistics
- Helper functions

#### [manage.py](manage.py)
Management CLI
- List videos
- Clean up files
- Show statistics
- View configuration

#### [api.py](api.py)
REST API server
- Status endpoints
- Generation control
- Video management
- Statistics API

#### [demo.py](demo.py)
Interactive demonstration
- Guided walkthrough
- Feature showcase
- Test functionality

#### [test_generator.py](test_generator.py)
Test suite
- Dependency checks
- Configuration validation
- Component testing

## 📝 Examples

### [examples/custom_generation.py](examples/custom_generation.py)
Custom video generation
- Parameter customization
- Multiple video generation
- Configuration override

### [examples/batch_process.py](examples/batch_process.py)
Batch theme processing
- Theme-based generation
- Multiple keyword sets
- Organized output

### [examples/api_client.py](examples/api_client.py)
API client usage
- Making API requests
- Status monitoring
- Video downloading

## 🔍 Finding Information

### By Task

**"I want to install the tool"**
→ README.md (Quick Start) or run `./quick_start.sh`

**"I want to generate one video"**
→ QUICK_REFERENCE.md or run `python main.py once`

**"I want to run it continuously"**
→ USAGE_GUIDE.md (Hourly Mode) or `python main.py hourly`

**"I want to customize keywords"**
→ config.py or README.md (Configuration)

**"I want to use the API"**
→ api.py or examples/api_client.py

**"I want to deploy with Docker"**
→ USAGE_GUIDE.md (Docker) or `docker-compose up`

**"I need to troubleshoot"**
→ README.md (Troubleshooting) or run `python test_generator.py`

**"I want to clean up files"**
→ QUICK_REFERENCE.md (Management) or `python manage.py clean`

**"I want to understand the architecture"**
→ PROJECT_OVERVIEW.md

### By Experience Level

**Beginner**
1. README.md
2. Run ./quick_start.sh
3. Try demo.py
4. Read QUICK_REFERENCE.md

**Intermediate**
1. USAGE_GUIDE.md
2. Customize config.py
3. Try examples/
4. Use manage.py

**Advanced**
1. PROJECT_OVERVIEW.md
2. Review source code
3. Use api.py
4. Extend functionality

### By Role

**Content Creator**
- README.md - Basic usage
- QUICK_REFERENCE.md - Daily commands
- USAGE_GUIDE.md - Workflows

**Developer**
- PROJECT_OVERVIEW.md - Architecture
- Source code files - Implementation
- examples/ - Code examples

**System Administrator**
- USAGE_GUIDE.md - Deployment
- Dockerfile & docker-compose.yml - Containerization
- motivational-content-gen.service - Service setup

## 📊 Documentation Statistics

- **Total Documentation Files**: 7
- **Total Code Files**: 11
- **Total Examples**: 3
- **Lines of Documentation**: ~2000+
- **Lines of Code**: ~1500+

## 🔄 Keeping Updated

This project includes:
- Inline code comments
- Docstrings in functions
- Configuration comments
- Example scripts
- Test suite

All documentation is version-controlled and updated with code changes.

## 💡 Tips for Using Documentation

1. **Start Simple**: Begin with README.md
2. **Use Search**: Search all .md files for keywords
3. **Try Examples**: Run example scripts to learn
4. **Check Tests**: test_generator.py validates setup
5. **Read Code**: Python code is well-commented
6. **Experiment**: Modify config.py and test

## 🎯 Common Documentation Paths

### Complete Beginner Path
```
README.md 
  → ./quick_start.sh
  → python main.py once
  → QUICK_REFERENCE.md
```

### Content Creator Path
```
README.md
  → USAGE_GUIDE.md (Workflows)
  → Customize config.py
  → python main.py hourly
```

### Developer Path
```
PROJECT_OVERVIEW.md
  → Review source files
  → examples/ directory
  → Extend and customize
```

### Deployment Path
```
USAGE_GUIDE.md (Docker or Systemd)
  → Configure for production
  → Set up monitoring
  → Maintain with manage.py
```

## 📞 Need More Help?

If you can't find what you need:
1. Search all .md files for keywords
2. Check examples/ directory
3. Run test_generator.py for diagnostics
4. Review error messages
5. Check configuration files

## 🎓 Learning Resources

Ordered by learning path:

1. **README.md** - Overview and quick start
2. **QUICK_REFERENCE.md** - Command reference
3. **USAGE_GUIDE.md** - Detailed instructions
4. **PROJECT_OVERVIEW.md** - Technical details
5. **examples/** - Practical examples
6. **Source Code** - Implementation details

Happy content generating! 🚀
