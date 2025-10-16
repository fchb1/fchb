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
