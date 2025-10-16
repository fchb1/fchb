# TikTok Content Generator for Mobile Detailing

A powerful content generation tool designed specifically for mobile detailing businesses to create engaging TikTok content that drives bookings and grows your audience.

## 🚀 Quick Start

**New User?** → Start with [GETTING_STARTED.md](GETTING_STARTED.md)

**Want to Jump Right In?** → Read [QUICKSTART.md](QUICKSTART.md)

### Generate Your First Post (10 seconds)

```bash
python3 content_generator.py --type post
```

### Interactive Mode (Easiest for Beginners)

```bash
python3 content_generator.py --interactive
```

## ✨ Features

- 🎯 **Complete Posts**: Video concepts + captions + hashtags + strategy
- 📝 **Engaging Captions**: Hooks that grab attention in 3 seconds
- 🏷️ **Smart Hashtags**: Researched combinations for maximum reach
- 🎬 **Video Concepts**: Shot-by-shot breakdowns with duration
- 📅 **Content Calendar**: Plan weeks of content in advance
- 🔥 **Trending Integration**: Adapt viral trends to detailing
- 🎨 **Fully Customizable**: Make it match your brand voice
- 💾 **JSON Export**: Save and organize your content plans

## 📋 Requirements

- Python 3.6 or higher
- **No external dependencies!** (Uses Python standard library only)

## 🎯 Usage Examples

### Generate Complete Post
Perfect for daily content creation:
```bash
python3 content_generator.py --type post
```

Output includes: Video concept, hook, caption, hashtags, posting times, engagement tips

### Generate Content Ideas
When you need inspiration:
```bash
python3 content_generator.py --type ideas --count 10
```

### Generate Captions Only
For videos you already have planned:
```bash
python3 content_generator.py --type caption --count 5
```

### Generate Hashtags
Quick hashtag sets:
```bash
python3 content_generator.py --type hashtags --count 15
```

### Generate Video Concepts
Get specific video ideas with shot lists:
```bash
python3 content_generator.py --type concept --difficulty easy
```

### Generate Content Calendar
Plan your entire week:
```bash
python3 content_generator.py --type calendar --days 7
```

### Topic-Specific Content
Focus on a specific service:
```bash
python3 content_generator.py --type post --topic "ceramic-coating"
```

### Save to File
Export for planning:
```bash
python3 content_generator.py --type calendar --days 7 --output week.json
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [GETTING_STARTED.md](GETTING_STARTED.md) | 👈 **Start here** - Complete beginner's guide |
| [QUICKSTART.md](QUICKSTART.md) | Get up and running in 5 minutes |
| [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) | Personalize for your business |
| [TIKTOK_STRATEGY.md](TIKTOK_STRATEGY.md) | Complete TikTok marketing strategy |
| [examples.md](examples.md) | Examples and best practices |
| [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) | High-level project overview |

## 🎨 Content Types Supported

- **Before/After Transformations** - Dramatic results that wow viewers
- **Satisfying Cleaning Videos** - ASMR and oddly satisfying content
- **Educational Tutorials** - Share your expertise and build authority
- **Behind the Scenes** - Show your process and build connection
- **Customer Reactions** - Social proof and testimonials
- **Product Reviews** - Showcase tools and products
- **Day in the Life** - Personal brand building
- **Trending Challenges** - Adapt viral trends to detailing
- **Problem/Solution** - Common car care issues
- **Storytelling** - Engaging narratives

## 🎬 Example Output

When you run `python3 content_generator.py --type post`, you get:

```
============================================================
🎬 VIDEO CONCEPT
============================================================
Title: Before & After Transformation
Description: Showcase a dramatic vehicle transformation
Duration: 15-30 seconds
Trending Angle: Before/after transitions

Shot List:
  1. Start with the dirty 'before' state
  2. Quick time-lapse of the cleaning process
  3. Reveal the pristine 'after' result
  4. Close-up details of the finish

============================================================
📝 CAPTION
============================================================

Wait until you see what I pulled out of this car! 😱

POV: Your car hasn't been detailed in 2 years and you finally book us 😍 
The Interior deep clean transformation is insane! Drop a 🔥 if you need this!

============================================================
🏷️  HASHTAGS
============================================================
#MobileDetailing #CarDetailing #SatisfyingVideos #BeforeAndAfter 
#DetailingTips #CarTok #CleanTok #DetailersOfTikTok

============================================================
⏰ BEST POSTING TIMES
============================================================
  • 7-9 AM (morning commute)
  • 12-2 PM (lunch break)
  • 7-10 PM (evening scrolling)

============================================================
💡 ENGAGEMENT TIPS
============================================================
  • Respond to comments within first hour
  • Pin a comment asking viewers to book
  • Use a call-to-action in your caption
  • Add location tags to reach local audience
```

## 🎯 Command Reference

| Command | Description |
|---------|-------------|
| `--type post` | Generate complete post with everything |
| `--type ideas` | Generate content ideas only |
| `--type caption` | Generate captions only |
| `--type hashtags` | Generate hashtags only |
| `--type concept` | Generate video concepts only |
| `--type calendar` | Generate content calendar |
| `--interactive` | Run in interactive menu mode |
| `--count N` | Generate N items |
| `--days N` | Generate calendar for N days |
| `--topic "X"` | Focus on specific topic |
| `--difficulty easy\|medium\|hard` | Filter concepts by difficulty |
| `--output file.json` | Save results to JSON file |

## 🧪 Testing

Run the test suite to verify everything works:

```bash
python3 test_generator.py
```

All 9 tests should pass ✅

## 🎨 Customization

This tool is designed to be easily customized for your specific business:

- Add your city/location hashtags
- Add your specific services
- Customize hooks with your brand voice
- Add your contact information
- Create service-specific templates

See [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) for detailed instructions.

## 📊 What's Included

### Topics Covered (15+)
- Interior deep clean
- Exterior wash and wax
- Ceramic coating application
- Leather conditioning
- Engine bay detailing
- Headlight restoration
- Scratch removal
- Pet hair removal
- Odor elimination
- Paint correction
- And more...

### Video Concepts (10)
1. Before & After Transformation
2. Satisfying Dirt Extraction
3. Product Comparison
4. Day in the Life
5. Detailing Hack Tutorial
6. Gross to Gorgeous
7. Price Breakdown Story
8. Customer Reaction
9. Trending Sound Adaptation
10. Mistake Prevention

### Hashtag Categories (50+)
- Core industry tags
- Engagement tags
- Niche detailing tags
- Viral/trending tags
- Location-based tags

## 💡 Use Cases

**Daily Workflow:**
```bash
# Morning: Get today's post
python3 content_generator.py --type post
# Record video, post, engage
```

**Weekly Planning:**
```bash
# Monday: Plan the week
python3 content_generator.py --type calendar --days 7 --output week.json
# Batch record all videos
```

**Creative Brainstorming:**
```bash
# Generate lots of ideas
python3 content_generator.py --type ideas --count 20
# Pick favorites and develop
```

## 🚀 Expected Results

With consistent use:
- **Month 1**: 1,000+ views, 100+ followers
- **Month 3**: 10,000+ views, 500+ followers, first bookings
- **Month 6**: 50,000+ views, 1,000+ followers, regular bookings

*Results vary based on content quality, consistency, and market*

## 📝 License

MIT License - Free to use for your business

See [LICENSE](LICENSE) file for details.

## 🎓 Getting Help

1. **Read the docs** - Start with [GETTING_STARTED.md](GETTING_STARTED.md)
2. **Run tests** - `python3 test_generator.py` for diagnostics
3. **Check examples** - See [examples.md](examples.md) for inspiration

## ⭐ Best Practices

1. **Post Consistently** - 1-2x daily
2. **Engage Actively** - Reply to comments fast
3. **Track Performance** - What works, double down
4. **Customize Content** - Make it yours
5. **Provide Value** - Education + entertainment
6. **Local Focus** - Target your service area

## 🔧 Troubleshooting

**Python not found?**
```bash
python3 --version  # Check installation
```

**Permission denied?**
```bash
chmod +x content_generator.py
```

**Need help?**
Check the documentation files - everything is covered!

---

**Ready to dominate TikTok and grow your mobile detailing business?**

Start here: `python3 content_generator.py --interactive`

---

Made with ❤️ for mobile detailing professionals who want to leverage TikTok without spending hours on content planning.
