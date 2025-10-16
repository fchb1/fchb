#!/usr/bin/env python3
"""
Test suite for TikTok Content Generator
Run this to verify everything works correctly
"""

import sys
from content_generator import TikTokContentGenerator


def test_hooks():
    """Test hook generation"""
    print("Testing hook generation...")
    generator = TikTokContentGenerator()
    hook = generator.generate_hook()
    assert isinstance(hook, str)
    assert len(hook) > 0
    print(f"✓ Hook generated: {hook[:50]}...")


def test_caption():
    """Test caption generation"""
    print("\nTesting caption generation...")
    generator = TikTokContentGenerator()
    caption = generator.generate_caption()
    assert 'hook' in caption
    assert 'body' in caption
    assert 'full_caption' in caption
    assert 'topic' in caption
    print(f"✓ Caption generated for topic: {caption['topic']}")


def test_hashtags():
    """Test hashtag generation"""
    print("\nTesting hashtag generation...")
    generator = TikTokContentGenerator()
    hashtags = generator.generate_hashtags(15)
    assert isinstance(hashtags, list)
    assert len(hashtags) <= 15
    assert all(tag.startswith('#') for tag in hashtags)
    print(f"✓ Generated {len(hashtags)} hashtags")


def test_video_concept():
    """Test video concept generation"""
    print("\nTesting video concept generation...")
    generator = TikTokContentGenerator()
    concept = generator.generate_video_concept()
    assert 'title' in concept
    assert 'description' in concept
    assert 'shots' in concept
    assert 'duration' in concept
    assert 'hook' in concept
    print(f"✓ Video concept: {concept['title']}")


def test_content_ideas():
    """Test content ideas generation"""
    print("\nTesting content ideas generation...")
    generator = TikTokContentGenerator()
    ideas = generator.generate_content_ideas(5)
    assert isinstance(ideas, list)
    assert len(ideas) == 5
    assert all('topic' in idea for idea in ideas)
    print(f"✓ Generated {len(ideas)} content ideas")


def test_complete_post():
    """Test complete post generation"""
    print("\nTesting complete post generation...")
    generator = TikTokContentGenerator()
    post = generator.generate_post()
    assert 'video_concept' in post
    assert 'hook' in post
    assert 'caption' in post
    assert 'hashtags' in post
    assert 'best_posting_times' in post
    assert 'engagement_tips' in post
    print("✓ Complete post generated successfully")


def test_content_calendar():
    """Test content calendar generation"""
    print("\nTesting content calendar generation...")
    generator = TikTokContentGenerator()
    calendar = generator.generate_content_calendar(7)
    assert isinstance(calendar, list)
    assert len(calendar) == 7
    assert all('date' in day for day in calendar)
    assert all('day' in day for day in calendar)
    assert all('post' in day for day in calendar)
    print(f"✓ Generated {len(calendar)}-day content calendar")


def test_topic_specific():
    """Test topic-specific generation"""
    print("\nTesting topic-specific content...")
    generator = TikTokContentGenerator()
    post = generator.generate_post("Ceramic coating application")
    assert post is not None
    print("✓ Topic-specific post generated")


def test_difficulty_filter():
    """Test difficulty filtering for video concepts"""
    print("\nTesting difficulty filter...")
    generator = TikTokContentGenerator()
    easy_concept = generator.generate_video_concept("easy")
    assert easy_concept['difficulty'] == "Easy"
    print("✓ Difficulty filter working")


def run_all_tests():
    """Run all tests"""
    print("="*60)
    print("TikTok Content Generator - Test Suite")
    print("="*60)
    
    tests = [
        test_hooks,
        test_caption,
        test_hashtags,
        test_video_concept,
        test_content_ideas,
        test_complete_post,
        test_content_calendar,
        test_topic_specific,
        test_difficulty_filter
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("\n🎉 All tests passed! Your generator is ready to use.")
        return 0
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
