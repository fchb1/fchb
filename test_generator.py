#!/usr/bin/env python3
"""
Test suite for the content generator
Run basic checks without actually generating videos
"""

import sys
from pathlib import Path

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import yt_dlp
        print("  ✓ yt_dlp")
    except ImportError:
        print("  ✗ yt_dlp - Install with: pip install yt-dlp")
        return False
    
    try:
        import moviepy
        print("  ✓ moviepy")
    except ImportError:
        print("  ✗ moviepy - Install with: pip install moviepy")
        return False
    
    try:
        from PIL import Image
        print("  ✓ Pillow")
    except ImportError:
        print("  ✗ Pillow - Install with: pip install Pillow")
        return False
    
    try:
        import numpy
        print("  ✓ numpy")
    except ImportError:
        print("  ✗ numpy - Install with: pip install numpy")
        return False
    
    try:
        import schedule
        print("  ✓ schedule")
    except ImportError:
        print("  ✗ schedule - Install with: pip install schedule")
        return False
    
    try:
        import dotenv
        print("  ✓ python-dotenv")
    except ImportError:
        print("  ✗ python-dotenv - Install with: pip install python-dotenv")
        return False
    
    return True

def test_ffmpeg():
    """Test that FFmpeg is available"""
    print("\nTesting FFmpeg...")
    
    import subprocess
    
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"  ✓ FFmpeg found: {version_line}")
            return True
        else:
            print("  ✗ FFmpeg not working properly")
            return False
    
    except FileNotFoundError:
        print("  ✗ FFmpeg not found")
        print("    Install FFmpeg:")
        print("      Ubuntu/Debian: sudo apt install ffmpeg")
        print("      MacOS: brew install ffmpeg")
        return False

def test_modules():
    """Test that project modules can be imported"""
    print("\nTesting project modules...")
    
    try:
        import config
        print("  ✓ config")
    except Exception as e:
        print(f"  ✗ config - {e}")
        return False
    
    try:
        from downloader import ContentDownloader
        print("  ✓ downloader")
    except Exception as e:
        print(f"  ✗ downloader - {e}")
        return False
    
    try:
        from video_processor import VideoProcessor
        print("  ✓ video_processor")
    except Exception as e:
        print(f"  ✗ video_processor - {e}")
        return False
    
    try:
        from content_generator import ContentGenerator
        print("  ✓ content_generator")
    except Exception as e:
        print(f"  ✗ content_generator - {e}")
        return False
    
    try:
        from scheduler import ContentScheduler
        print("  ✓ scheduler")
    except Exception as e:
        print(f"  ✗ scheduler - {e}")
        return False
    
    return True

def test_configuration():
    """Test configuration values"""
    print("\nTesting configuration...")
    
    import config
    
    checks = [
        (hasattr(config, 'OUTPUT_DIR'), "OUTPUT_DIR defined"),
        (hasattr(config, 'TEMP_DIR'), "TEMP_DIR defined"),
        (hasattr(config, 'MAX_VIDEO_LENGTH'), "MAX_VIDEO_LENGTH defined"),
        (hasattr(config, 'MIN_VIDEO_LENGTH'), "MIN_VIDEO_LENGTH defined"),
        (hasattr(config, 'CLIPS_PER_VIDEO'), "CLIPS_PER_VIDEO defined"),
        (hasattr(config, 'MOTIVATIONAL_KEYWORDS'), "MOTIVATIONAL_KEYWORDS defined"),
        (hasattr(config, 'MOTIVATIONAL_QUOTES'), "MOTIVATIONAL_QUOTES defined"),
        (len(config.MOTIVATIONAL_KEYWORDS) > 0, "Keywords list not empty"),
        (len(config.MOTIVATIONAL_QUOTES) > 0, "Quotes list not empty"),
    ]
    
    all_passed = True
    for check, description in checks:
        if check:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description}")
            all_passed = False
    
    return all_passed

def test_directories():
    """Test that directories can be created"""
    print("\nTesting directory creation...")
    
    import config
    
    try:
        Path(config.OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Output directory: {config.OUTPUT_DIR}")
    except Exception as e:
        print(f"  ✗ Cannot create output directory: {e}")
        return False
    
    try:
        Path(config.TEMP_DIR).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Temp directory: {config.TEMP_DIR}")
    except Exception as e:
        print(f"  ✗ Cannot create temp directory: {e}")
        return False
    
    return True

def test_classes():
    """Test that classes can be instantiated"""
    print("\nTesting class instantiation...")
    
    try:
        from downloader import ContentDownloader
        downloader = ContentDownloader()
        print("  ✓ ContentDownloader")
    except Exception as e:
        print(f"  ✗ ContentDownloader - {e}")
        return False
    
    try:
        from video_processor import VideoProcessor
        processor = VideoProcessor()
        print("  ✓ VideoProcessor")
    except Exception as e:
        print(f"  ✗ VideoProcessor - {e}")
        return False
    
    try:
        from content_generator import ContentGenerator
        generator = ContentGenerator()
        print("  ✓ ContentGenerator")
    except Exception as e:
        print(f"  ✗ ContentGenerator - {e}")
        return False
    
    try:
        from scheduler import ContentScheduler
        scheduler = ContentScheduler()
        print("  ✓ ContentScheduler")
    except Exception as e:
        print(f"  ✗ ContentScheduler - {e}")
        return False
    
    return True

def main():
    print("="*60)
    print("  CONTENT GENERATOR TEST SUITE")
    print("="*60)
    
    tests = [
        ("Dependencies", test_imports),
        ("FFmpeg", test_ffmpeg),
        ("Project Modules", test_modules),
        ("Configuration", test_configuration),
        ("Directories", test_directories),
        ("Classes", test_classes),
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n  ✗ Unexpected error in {name}: {e}")
            results.append((name, False))
    
    print("\n" + "="*60)
    print("  TEST RESULTS")
    print("="*60)
    
    all_passed = True
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status}: {name}")
        if not passed:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n✓ All tests passed! Ready to generate content.")
        print("\nNext steps:")
        print("  python main.py once          # Generate one video")
        print("  python main.py hourly        # Run hourly generation")
        return 0
    else:
        print("\n✗ Some tests failed. Please fix the issues above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
