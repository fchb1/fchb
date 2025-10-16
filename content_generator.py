#!/usr/bin/env python3
"""
TikTok Content Generator for Mobile Detailing Business
Generates engaging content ideas, captions, hooks, and hashtags
"""

import random
import argparse
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any


class TikTokContentGenerator:
    """Generate TikTok content for mobile detailing business"""
    
    def __init__(self):
        self.hooks = [
            "Wait until you see what I pulled out of this car! 😱",
            "This is why you need professional detailing 👀",
            "POV: You finally get your car detailed after 2 years",
            "I've been detailing for 10 years and this shocked me",
            "This customer said their car was 'clean' 🤢",
            "The before is going to blow your mind",
            "This is the most satisfying detail I've ever done ✨",
            "No one believes this is the same car",
            "This detail took 8 hours but watch this transformation",
            "Here's what happens when you skip regular detailing",
            "I bet you've never seen this detailing hack before",
            "This $300 detail vs a $30 car wash - which would you choose?",
            "Stop wasting money on cheap car washes! Here's why:",
            "Your car dealer doesn't want you to know this trick",
            "This one product changed how I detail cars forever",
        ]
        
        self.video_concepts = [
            {
                "title": "Before & After Transformation",
                "description": "Showcase a dramatic vehicle transformation",
                "shots": [
                    "Start with the dirty 'before' state",
                    "Quick time-lapse of the cleaning process",
                    "Reveal the pristine 'after' result",
                    "Close-up details of the finish"
                ],
                "duration": "15-30 seconds",
                "difficulty": "Easy"
            },
            {
                "title": "Satisfying Dirt Extraction",
                "description": "Show dirt being removed from carpets or upholstery",
                "shots": [
                    "Close-up of dirty surface",
                    "Extraction tool in action",
                    "Dirty water being collected",
                    "Final clean result"
                ],
                "duration": "10-20 seconds",
                "difficulty": "Easy"
            },
            {
                "title": "Product Comparison",
                "description": "Compare professional vs consumer products",
                "shots": [
                    "Show both products side by side",
                    "Apply each to similar surfaces",
                    "Compare the results",
                    "Reveal the winner"
                ],
                "duration": "30-45 seconds",
                "difficulty": "Medium"
            },
            {
                "title": "Day in the Life",
                "description": "Follow your mobile detailing journey",
                "shots": [
                    "Morning prep and loading van",
                    "Arrival at customer location",
                    "Quick clips of multiple details",
                    "Happy customer reactions"
                ],
                "duration": "45-60 seconds",
                "difficulty": "Medium"
            },
            {
                "title": "Detailing Hack Tutorial",
                "description": "Teach a quick detailing tip or trick",
                "shots": [
                    "Present the problem",
                    "Introduce the solution/hack",
                    "Demonstrate step-by-step",
                    "Show the impressive result"
                ],
                "duration": "20-35 seconds",
                "difficulty": "Easy"
            },
            {
                "title": "Gross to Gorgeous",
                "description": "Focus on the nastiest part of the job",
                "shots": [
                    "Reveal the disgusting starting point",
                    "Your reaction (humor optional)",
                    "Cleaning process",
                    "Amazing clean result"
                ],
                "duration": "15-25 seconds",
                "difficulty": "Easy"
            },
            {
                "title": "Price Breakdown Story",
                "description": "Explain why detailing costs what it does",
                "shots": [
                    "Text: 'Why does detailing cost $200+'",
                    "Show all the steps involved",
                    "Display products and equipment used",
                    "Final result justifying the price"
                ],
                "duration": "30-45 seconds",
                "difficulty": "Medium"
            },
            {
                "title": "Customer Reaction",
                "description": "Capture genuine customer amazement",
                "shots": [
                    "Customer drops off dirty car",
                    "Time-lapse of detail",
                    "Reveal to customer (their reaction)",
                    "Testimonial or thank you"
                ],
                "duration": "20-40 seconds",
                "difficulty": "Hard"
            },
            {
                "title": "Trending Sound Adaptation",
                "description": "Use trending audio with detailing context",
                "shots": [
                    "Sync your content to trending sound",
                    "Make it relevant to detailing",
                    "Add text overlays for context",
                    "Include your branding"
                ],
                "duration": "15-30 seconds",
                "difficulty": "Medium"
            },
            {
                "title": "Mistake Prevention",
                "description": "Show common car care mistakes",
                "shots": [
                    "Text: 'Stop doing this to your car!'",
                    "Show the mistake",
                    "Explain why it's bad",
                    "Show the correct way"
                ],
                "duration": "25-40 seconds",
                "difficulty": "Easy"
            }
        ]
        
        self.topics = [
            "Interior deep clean",
            "Exterior wash and wax",
            "Ceramic coating application",
            "Leather conditioning",
            "Engine bay detailing",
            "Headlight restoration",
            "Scratch removal",
            "Pet hair removal",
            "Odor elimination",
            "Paint correction",
            "Wheel and tire detailing",
            "Glass cleaning",
            "Dashboard restoration",
            "Stain removal",
            "Clay bar treatment"
        ]
        
        self.trending_angles = [
            "ASMR detailing sounds",
            "Satisfying cleaning videos",
            "Before/after transitions",
            "POV style content",
            "Story time while detailing",
            "Myth busting car care",
            "Product testing",
            "Extreme transformations",
            "Time-lapse magic",
            "Customer surprise reactions"
        ]
        
        self.hashtag_groups = {
            "core": [
                "#MobileDetailing",
                "#CarDetailing",
                "#AutoDetailing",
                "#DetailingWorld",
                "#CarCare"
            ],
            "engagement": [
                "#SatisfyingVideos",
                "#Satisfying",
                "#OddlySatisfying",
                "#BeforeAndAfter",
                "#Transformation"
            ],
            "niche": [
                "#DetailingLife",
                "#DetailersOfTikTok",
                "#DetailingBusiness",
                "#ProfessionalDetailer",
                "#DetailingTips"
            ],
            "viral": [
                "#CarTok",
                "#CleanTok",
                "#SmallBusiness",
                "#CarLovers",
                "#AutoCare"
            ],
            "location": [
                "#MobileDetailer",
                "#LocalBusiness",
                "#SupportLocal",
                "#SmallBusinessOwner"
            ]
        }
        
    def generate_hook(self) -> str:
        """Generate an attention-grabbing hook"""
        return random.choice(self.hooks)
    
    def generate_caption(self, topic: str = None) -> Dict[str, Any]:
        """Generate a complete caption with hook and body"""
        if topic is None:
            topic = random.choice(self.topics)
            
        hook = self.generate_hook()
        
        caption_templates = [
            f"POV: Your car hasn't been detailed in 2 years and you finally book us 😍 The {topic} transformation is insane! Drop a 🔥 if you need this!",
            f"This {topic} took 3 hours but look at this result ✨ Tag someone whose car needs this ASAP!",
            f"When they say they 'just cleaned' their car 😅 Here's what professional {topic} actually looks like 👀",
            f"Real talk: {topic} is so underrated 💯 Your car will thank you! Who's booking their appointment? 👇",
            f"The {topic} before and after that has everyone talking 🗣️ DM to book your transformation!",
            f"Everyone asks how we get results like this with {topic}... Here's the secret 🤫",
            f"This is why {topic} should be done every 6 months minimum! The difference is crazy 🤯",
            f"POV: You trusted us with your car and now it looks better than when you bought it 🚗✨ Thanks for trusting our {topic} service!",
            f"I've been doing {topic} for years and this is still so satisfying to watch 😌 Drop a ❤️ if you agree!",
            f"Your car after our {topic} service >>> Any car wash 💪 Book now, spots filling up fast!",
        ]
        
        body = random.choice(caption_templates)
        
        return {
            "hook": hook,
            "body": body,
            "full_caption": f"{hook}\n\n{body}",
            "topic": topic
        }
    
    def generate_hashtags(self, count: int = 15, include_custom: List[str] = None) -> List[str]:
        """Generate a mix of hashtags for maximum reach"""
        hashtags = []
        
        # Take some from each category
        hashtags.extend(random.sample(self.hashtag_groups["core"], min(3, len(self.hashtag_groups["core"]))))
        hashtags.extend(random.sample(self.hashtag_groups["engagement"], min(3, len(self.hashtag_groups["engagement"]))))
        hashtags.extend(random.sample(self.hashtag_groups["niche"], min(3, len(self.hashtag_groups["niche"]))))
        hashtags.extend(random.sample(self.hashtag_groups["viral"], min(3, len(self.hashtag_groups["viral"]))))
        hashtags.extend(random.sample(self.hashtag_groups["location"], min(2, len(self.hashtag_groups["location"]))))
        
        # Add custom hashtags if provided
        if include_custom:
            hashtags.extend([f"#{tag.replace('#', '')}" for tag in include_custom])
        
        # Trim to requested count
        return hashtags[:count]
    
    def generate_video_concept(self, difficulty: str = None) -> Dict[str, Any]:
        """Generate a complete video concept"""
        concepts = self.video_concepts
        
        if difficulty:
            concepts = [c for c in concepts if c["difficulty"].lower() == difficulty.lower()]
        
        concept = random.choice(concepts)
        topic = random.choice(self.topics)
        angle = random.choice(self.trending_angles)
        
        return {
            **concept,
            "suggested_topic": topic,
            "trending_angle": angle,
            "hook": self.generate_hook(),
            "caption": self.generate_caption(topic),
            "hashtags": self.generate_hashtags()
        }
    
    def generate_content_ideas(self, count: int = 5) -> List[Dict[str, Any]]:
        """Generate multiple content ideas"""
        ideas = []
        
        for _ in range(count):
            topic = random.choice(self.topics)
            angle = random.choice(self.trending_angles)
            
            ideas.append({
                "topic": topic,
                "angle": angle,
                "hook": self.generate_hook(),
                "video_concept": random.choice(self.video_concepts)["title"]
            })
        
        return ideas
    
    def generate_post(self, topic: str = None) -> Dict[str, Any]:
        """Generate a complete TikTok post ready to use"""
        caption_data = self.generate_caption(topic)
        concept = self.generate_video_concept()
        
        return {
            "video_concept": {
                "title": concept["title"],
                "description": concept["description"],
                "shots": concept["shots"],
                "duration": concept["duration"]
            },
            "hook": caption_data["hook"],
            "caption": caption_data["full_caption"],
            "hashtags": self.generate_hashtags(),
            "trending_angle": concept["trending_angle"],
            "best_posting_times": [
                "7-9 AM (morning commute)",
                "12-2 PM (lunch break)",
                "7-10 PM (evening scrolling)"
            ],
            "engagement_tips": [
                "Respond to comments within first hour",
                "Pin a comment asking viewers to book",
                "Use a call-to-action in your caption",
                "Add location tags to reach local audience"
            ]
        }
    
    def generate_content_calendar(self, days: int = 7) -> List[Dict[str, Any]]:
        """Generate a content calendar for specified days"""
        calendar = []
        
        content_mix = [
            "before_after",
            "tutorial",
            "satisfying",
            "educational",
            "behind_scenes",
            "customer_reaction",
            "trending"
        ]
        
        start_date = datetime.now()
        
        for i in range(days):
            post_date = start_date + timedelta(days=i)
            content_type = content_mix[i % len(content_mix)]
            
            post = self.generate_post()
            
            calendar.append({
                "date": post_date.strftime("%Y-%m-%d"),
                "day": post_date.strftime("%A"),
                "content_type": content_type,
                "post": post
            })
        
        return calendar


def print_formatted_post(post: Dict[str, Any]):
    """Pretty print a post"""
    print("\n" + "="*60)
    print("🎬 VIDEO CONCEPT")
    print("="*60)
    print(f"Title: {post['video_concept']['title']}")
    print(f"Description: {post['video_concept']['description']}")
    print(f"Duration: {post['video_concept']['duration']}")
    print(f"\nTrending Angle: {post['trending_angle']}")
    print("\nShot List:")
    for i, shot in enumerate(post['video_concept']['shots'], 1):
        print(f"  {i}. {shot}")
    
    print("\n" + "="*60)
    print("📝 CAPTION")
    print("="*60)
    print(f"\n{post['caption']}")
    
    print("\n" + "="*60)
    print("🏷️  HASHTAGS")
    print("="*60)
    print(" ".join(post['hashtags']))
    
    print("\n" + "="*60)
    print("⏰ BEST POSTING TIMES")
    print("="*60)
    for time in post['best_posting_times']:
        print(f"  • {time}")
    
    print("\n" + "="*60)
    print("💡 ENGAGEMENT TIPS")
    print("="*60)
    for tip in post['engagement_tips']:
        print(f"  • {tip}")
    print("\n")


def interactive_mode():
    """Run the generator in interactive mode"""
    generator = TikTokContentGenerator()
    
    print("\n" + "="*60)
    print("🚗 TikTok Content Generator for Mobile Detailing")
    print("="*60)
    
    while True:
        print("\nWhat would you like to generate?")
        print("1. Complete Post")
        print("2. Content Ideas")
        print("3. Just Captions")
        print("4. Just Hashtags")
        print("5. Video Concepts")
        print("6. Content Calendar")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            topic = input("Enter a specific topic (or press Enter for random): ").strip()
            topic = topic if topic else None
            post = generator.generate_post(topic)
            print_formatted_post(post)
            
        elif choice == "2":
            count = input("How many ideas? (default 5): ").strip()
            count = int(count) if count.isdigit() else 5
            ideas = generator.generate_content_ideas(count)
            
            print("\n" + "="*60)
            print("💡 CONTENT IDEAS")
            print("="*60)
            for i, idea in enumerate(ideas, 1):
                print(f"\n{i}. Topic: {idea['topic']}")
                print(f"   Angle: {idea['angle']}")
                print(f"   Concept: {idea['video_concept']}")
                print(f"   Hook: {idea['hook']}")
            print()
            
        elif choice == "3":
            count = input("How many captions? (default 3): ").strip()
            count = int(count) if count.isdigit() else 3
            
            print("\n" + "="*60)
            print("📝 CAPTIONS")
            print("="*60)
            for i in range(count):
                caption = generator.generate_caption()
                print(f"\n{i+1}.\n{caption['full_caption']}")
            print()
            
        elif choice == "4":
            count = input("How many hashtags? (default 15): ").strip()
            count = int(count) if count.isdigit() else 15
            hashtags = generator.generate_hashtags(count)
            
            print("\n" + "="*60)
            print("🏷️  HASHTAGS")
            print("="*60)
            print(" ".join(hashtags))
            print()
            
        elif choice == "5":
            difficulty = input("Difficulty? (easy/medium/hard or press Enter for any): ").strip()
            difficulty = difficulty if difficulty else None
            concept = generator.generate_video_concept(difficulty)
            
            print("\n" + "="*60)
            print("🎬 VIDEO CONCEPT")
            print("="*60)
            print(f"Title: {concept['title']}")
            print(f"Description: {concept['description']}")
            print(f"Duration: {concept['duration']}")
            print(f"Difficulty: {concept['difficulty']}")
            print(f"Suggested Topic: {concept['suggested_topic']}")
            print(f"Trending Angle: {concept['trending_angle']}")
            print("\nShot List:")
            for i, shot in enumerate(concept['shots'], 1):
                print(f"  {i}. {shot}")
            print()
            
        elif choice == "6":
            days = input("How many days? (default 7): ").strip()
            days = int(days) if days.isdigit() else 7
            calendar = generator.generate_content_calendar(days)
            
            print("\n" + "="*60)
            print("📅 CONTENT CALENDAR")
            print("="*60)
            for day in calendar:
                print(f"\n📆 {day['date']} - {day['day']}")
                print(f"Type: {day['content_type']}")
                print(f"Concept: {day['post']['video_concept']['title']}")
                print(f"Hook: {day['post']['hook']}")
            print()
            
        elif choice == "7":
            print("\n👋 Thanks for using TikTok Content Generator!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")


def main():
    parser = argparse.ArgumentParser(
        description="TikTok Content Generator for Mobile Detailing Business"
    )
    parser.add_argument(
        "--type",
        choices=["ideas", "post", "caption", "hashtags", "concept", "calendar"],
        help="Type of content to generate"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of items to generate"
    )
    parser.add_argument(
        "--topic",
        type=str,
        help="Specific topic for content"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of days for content calendar"
    )
    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        help="Difficulty level for video concepts"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output results to JSON file"
    )
    
    args = parser.parse_args()
    generator = TikTokContentGenerator()
    
    if args.interactive or not args.type:
        interactive_mode()
        return
    
    result = None
    
    if args.type == "ideas":
        result = generator.generate_content_ideas(args.count)
        print("\n💡 CONTENT IDEAS\n")
        for i, idea in enumerate(result, 1):
            print(f"{i}. {idea['topic']} - {idea['angle']}")
            print(f"   Hook: {idea['hook']}\n")
    
    elif args.type == "post":
        result = generator.generate_post(args.topic)
        print_formatted_post(result)
    
    elif args.type == "caption":
        result = [generator.generate_caption(args.topic) for _ in range(args.count)]
        print("\n📝 CAPTIONS\n")
        for i, caption in enumerate(result, 1):
            print(f"{i}.\n{caption['full_caption']}\n")
    
    elif args.type == "hashtags":
        result = generator.generate_hashtags(args.count)
        print("\n🏷️  HASHTAGS\n")
        print(" ".join(result))
        print()
    
    elif args.type == "concept":
        result = [generator.generate_video_concept(args.difficulty) for _ in range(args.count)]
        print("\n🎬 VIDEO CONCEPTS\n")
        for i, concept in enumerate(result, 1):
            print(f"{i}. {concept['title']} ({concept['difficulty']})")
            print(f"   {concept['description']}\n")
    
    elif args.type == "calendar":
        result = generator.generate_content_calendar(args.days)
        print("\n📅 CONTENT CALENDAR\n")
        for day in result:
            print(f"{day['date']} - {day['day']}: {day['post']['video_concept']['title']}")
    
    if args.output and result:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n✅ Results saved to {args.output}")


if __name__ == "__main__":
    main()
