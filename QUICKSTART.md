# Quick Start Guide

Get started with the TikTok Content Generator in under 5 minutes!

## Step 1: Installation

```bash
# Clone or download this repository
cd tiktok-content-generator

# Make the script executable (optional)
chmod +x content_generator.py
```

No additional dependencies needed! Uses only Python standard library.

## Step 2: Your First Content

### Interactive Mode (Recommended for beginners)

```bash
python content_generator.py --interactive
```

This will guide you through all options with a simple menu.

### Quick Commands

Generate a complete post:
```bash
python content_generator.py --type post
```

Generate 10 content ideas:
```bash
python content_generator.py --type ideas --count 10
```

Generate a 7-day content calendar:
```bash
python content_generator.py --type calendar --days 7
```

## Step 3: Customize for Your Business

Edit `content_generator.py` to add your own:

### Add Your Local Hashtags
Find the `hashtag_groups` section and add your city/region:

```python
"location": [
    "#MobileDetailer",
    "#LocalBusiness",
    "#PhoenixDetailing",  # <-- Add your city
    "#ArizonaDetailer",   # <-- Add your state
]
```

### Add Your Signature Services
Find the `topics` list and add your specialties:

```python
self.topics = [
    "Interior deep clean",
    "Ceramic coating application",
    "Your Custom Service",  # <-- Add here
]
```

### Add Your Unique Hooks
Find the `hooks` list and add your personality:

```python
self.hooks = [
    "Wait until you see this transformation! 😱",
    "Your custom hook here!",  # <-- Add your style
]
```

## Step 4: Save & Use Your Content

### Save to a file:
```bash
python content_generator.py --type calendar --days 7 --output weekly_plan.json
```

### Copy & Paste:
1. Run the generator
2. Copy the caption and hashtags
3. Paste directly into TikTok
4. Record your video based on the concept

## Pro Tips

### Daily Workflow
```bash
# Monday morning: Generate week's content
python content_generator.py --type calendar --days 7 --output thisweek.json

# Each day: Generate fresh post
python content_generator.py --type post --topic "ceramic-coating"
```

### Batch Content Creation
```bash
# Generate 20 captions at once
python content_generator.py --type caption --count 20 --output captions.json

# Generate 15 video concepts
python content_generator.py --type concept --count 15 --output concepts.json
```

## Common Use Cases

### "I need content for today!"
```bash
python content_generator.py --type post
```
Copy the caption, hashtags, and follow the video concept guide.

### "I want to plan next week"
```bash
python content_generator.py --type calendar --days 7
```
Review the calendar and schedule your recording days.

### "I need caption ideas"
```bash
python content_generator.py --type caption --count 10
```
Pick the ones you like and customize them.

### "What video should I make?"
```bash
python content_generator.py --type concept
```
Get a complete video concept with shot list.

## Troubleshooting

### "Command not found"
Make sure Python 3 is installed:
```bash
python3 --version
```
Use `python3` instead of `python` if needed.

### "Permission denied"
Make the file executable:
```bash
chmod +x content_generator.py
./content_generator.py --interactive
```

### "I want to customize the output"
Edit the `content_generator.py` file - all templates are clearly commented.

## Next Steps

1. ✅ Generate your first post
2. ✅ Record and post your video
3. ✅ Track which concepts perform best
4. ✅ Customize the generator with your learnings
5. ✅ Create a content calendar for next week

## Need Help?

- Check `examples.md` for detailed examples
- Read `README.md` for full documentation
- Review the code comments in `content_generator.py`

## Quick Reference

| Command | What it does |
|---------|-------------|
| `--type post` | Complete post with everything |
| `--type ideas` | Just content ideas |
| `--type caption` | Just captions |
| `--type hashtags` | Just hashtags |
| `--type concept` | Just video concepts |
| `--type calendar` | Content calendar |
| `--interactive` | Menu-driven interface |
| `--count N` | Generate N items |
| `--days N` | Calendar for N days |
| `--output file.json` | Save to file |

---

**Ready to go viral? Start generating content now! 🚀**
