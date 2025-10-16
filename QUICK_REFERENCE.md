# Quick Reference Card

## One-Liners

```bash
# Complete post (most common)
python3 content_generator.py --type post

# Interactive mode (easiest)
python3 content_generator.py --interactive

# Weekly plan
python3 content_generator.py --type calendar --days 7

# 20 ideas
python3 content_generator.py --type ideas --count 20

# Specific topic
python3 content_generator.py --type post --topic "ceramic-coating"

# Save to file
python3 content_generator.py --type post --output post.json
```

## Commands

| Type | What You Get |
|------|-------------|
| `post` | Complete post (concept + caption + hashtags + tips) |
| `ideas` | Quick content ideas (topic + angle + hook) |
| `caption` | Just the caption with hook |
| `hashtags` | Just hashtags (14-15) |
| `concept` | Video concept with shot list |
| `calendar` | Multi-day content plan |

## Options

| Option | Example |
|--------|---------|
| `--count N` | `--count 10` |
| `--days N` | `--days 7` |
| `--topic "X"` | `--topic "paint-correction"` |
| `--difficulty` | `--difficulty easy` |
| `--output file` | `--output plan.json` |
| `--interactive` | (no value) |

## Available Topics

- interior-deep-clean
- exterior-wash-and-wax
- ceramic-coating-application
- leather-conditioning
- engine-bay-detailing
- headlight-restoration
- scratch-removal
- pet-hair-removal
- odor-elimination
- paint-correction
- wheel-and-tire-detailing
- glass-cleaning
- dashboard-restoration
- stain-removal
- clay-bar-treatment

## Files to Read

1. **First time?** → `GETTING_STARTED.md`
2. **Quick start?** → `QUICKSTART.md`
3. **Customize?** → `CUSTOMIZATION_GUIDE.md`
4. **Strategy?** → `TIKTOK_STRATEGY.md`
5. **Examples?** → `examples.md`

## Testing

```bash
# Run all tests
python3 test_generator.py
```

## Best Posting Times

- 7-9 AM (morning commute)
- 12-2 PM (lunch break)
- 7-10 PM (evening scrolling)

## Content Mix (Weekly)

- 40% Before/after transformations
- 30% Educational content
- 20% Behind the scenes
- 10% Customer reactions

## Hashtag Formula

3 Core + 3 Niche + 3 Trending + 2 Location + 2-4 Specific = 13-15 total

## Daily Workflow

```bash
# Morning
python3 content_generator.py --type post

# Record video (30-60 min)
# Post to TikTok
# Engage with comments (throughout day)
```

## Weekly Workflow

```bash
# Monday morning
python3 content_generator.py --type calendar --days 7 --output week.json

# Tuesday (batch film)
# Record 5-7 videos in one session

# Wed-Sun (post daily)
# One post per day
# Engage actively
```

## Troubleshooting

```bash
# Check Python
python3 --version

# Make executable
chmod +x content_generator.py

# Run tests
python3 test_generator.py
```

## Quick Customization

Edit `content_generator.py`:
- Line ~85: Add your location hashtags
- Line ~50: Add your services
- Line ~25: Add your hooks

---

**Most Common Command:**
```bash
python3 content_generator.py --interactive
```

**Most Useful Command:**
```bash
python3 content_generator.py --type calendar --days 7 --output thisweek.json
```

---

Keep this card handy! 📌
