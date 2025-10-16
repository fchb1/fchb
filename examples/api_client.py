#!/usr/bin/env python3
"""
Example: Using the API to generate and manage videos
"""

import requests
import time
import json

API_URL = "http://localhost:5000"

def check_status():
    """Check API status"""
    response = requests.get(f"{API_URL}/status")
    return response.json()

def generate_video(num_videos=1):
    """Request video generation"""
    response = requests.post(
        f"{API_URL}/generate",
        json={'num_videos': num_videos}
    )
    return response.json()

def list_videos():
    """List all generated videos"""
    response = requests.get(f"{API_URL}/videos")
    return response.json()

def get_stats():
    """Get statistics"""
    response = requests.get(f"{API_URL}/stats")
    return response.json()

def download_video(filename, save_path):
    """Download a specific video"""
    response = requests.get(f"{API_URL}/videos/{filename}")
    
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    return False

def main():
    print("API Client Example")
    print("="*60)
    print(f"API URL: {API_URL}")
    print("="*60)
    
    try:
        print("\n1. Checking API status...")
        status = check_status()
        print(f"   Status: {json.dumps(status, indent=2)}")
        
        if not status['generating']:
            print("\n2. Requesting video generation...")
            result = generate_video(num_videos=1)
            print(f"   Result: {result['message']}")
            
            print("\n3. Waiting for generation to complete...")
            while True:
                status = check_status()
                if not status['generating']:
                    break
                print("   Still generating...")
                time.sleep(5)
            
            print("   ✓ Generation complete!")
        else:
            print("\n2. Generation already in progress, waiting...")
        
        print("\n4. Listing generated videos...")
        videos = list_videos()
        print(f"   Total videos: {videos['count']}")
        
        if videos['videos']:
            latest_video = videos['videos'][-1]
            if 'path' in latest_video:
                import os
                filename = os.path.basename(latest_video['path'])
                print(f"\n5. Downloading latest video: {filename}")
                
                if download_video(filename, f"downloaded_{filename}"):
                    print(f"   ✓ Downloaded to: downloaded_{filename}")
        
        print("\n6. Getting statistics...")
        stats = get_stats()
        print(f"   Videos generated: {stats['videos_generated']}")
        print(f"   Disk usage: {stats['disk_usage_mb']['total_mb']:.2f} MB")
        
        print("\n✓ Example complete!")
    
    except requests.exceptions.ConnectionError:
        print("\n✗ Error: Cannot connect to API")
        print("   Make sure the API server is running:")
        print("   python api.py")
    
    except Exception as e:
        print(f"\n✗ Error: {e}")

if __name__ == '__main__':
    main()
