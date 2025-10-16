# Customization Guide

Make this tool truly yours by customizing it for your specific mobile detailing business.

## Quick Customizations

### 1. Add Your Business Name & Location

Find this section in `content_generator.py`:

```python
self.hashtag_groups = {
    "location": [
        "#MobileDetailer",
        "#LocalBusiness",
        "#SupportLocal",
        "#SmallBusinessOwner"
    ]
}
```

Replace with:

```python
self.hashtag_groups = {
    "location": [
        "#MobileDetailer",
        "#MiamiDetailing",      # Your city
        "#FloridaDetailer",     # Your state
        "#SouthFloridaCars",    # Your region
        "#305Detailing"         # Your area code
    ]
}
```

### 2. Add Your Signature Services

Find the `topics` list:

```python
self.topics = [
    "Interior deep clean",
    "Exterior wash and wax",
    # Add your services here
]
```

Add your unique services:

```python
self.topics = [
    "Interior deep clean",
    "Exterior wash and wax",
    "Marine vinyl restoration",  # Your specialty
    "RV detailing",              # Your specialty
    "Boat detailing",            # Your specialty
    "Fleet detailing",           # Your specialty
]
```

### 3. Create Your Brand Voice

Find the `hooks` list and add your personality:

```python
self.hooks = [
    "Wait until you see what I pulled out of this car! 😱",
    # Add your hooks here
]
```

Examples for different brand voices:

**Professional/Educational:**
```python
"Here's what 10 years of detailing experience taught me:",
"Professional tip: This is how you should really clean your car",
"The difference between $50 and $500 detailing:",
```

**Funny/Relatable:**
```python
"I'm never eating in my car again after seeing this 🤮",
"Tell me you have kids without telling me you have kids:",
"This customer said 'it's not that bad' 💀",
```

**Luxury/Premium:**
```python
"Elevating automotive excellence, one detail at a time ✨",
"This is what premium detailing looks like 🔥",
"Luxury car care at your doorstep 🚗💎",
```

### 4. Add Your Pricing Tiers

Add a new method to the generator class:

```python
def get_pricing_context(self) -> Dict[str, Any]:
    """Return your business pricing for content"""
    return {
        "basic": {
            "name": "Express Detail",
            "price": "$79",
            "duration": "1-2 hours"
        },
        "standard": {
            "name": "Complete Detail",
            "price": "$149",
            "duration": "3-4 hours"
        },
        "premium": {
            "name": "Premium Package",
            "price": "$299",
            "duration": "6-8 hours"
        }
    }
```

### 5. Add Your Contact Information

Add a new attribute:

```python
def __init__(self):
    self.business_info = {
        "name": "Your Business Name",
        "phone": "(555) 123-4567",
        "email": "info@yourdetailing.com",
        "website": "www.yourdetailing.com",
        "booking_link": "book.yourdetailing.com",
        "service_area": "Miami & Surrounding Areas"
    }
```

Then update the post generation to include CTAs with your info:

```python
def generate_post(self, topic: str = None) -> Dict[str, Any]:
    # ... existing code ...
    
    return {
        # ... existing fields ...
        "call_to_action": f"📲 Book now: {self.business_info['booking_link']}",
        "service_area": self.business_info['service_area']
    }
```

## Advanced Customizations

### 1. Add Seasonal Content

```python
def get_seasonal_angles(self) -> List[str]:
    """Generate seasonal content ideas"""
    import datetime
    month = datetime.datetime.now().month
    
    seasonal = {
        (12, 1, 2): [  # Winter
            "Winter salt removal",
            "Protect your car from snow damage",
            "Holiday gift certificates available"
        ],
        (3, 4, 5): [  # Spring
            "Spring cleaning special",
            "Pollen removal tips",
            "Prepare for summer road trips"
        ],
        (6, 7, 8): [  # Summer
            "Beat the heat with a cool clean car",
            "Summer road trip prep",
            "Protect against sun damage"
        ],
        (9, 10, 11): [  # Fall
            "Fall leaf removal",
            "Prepare for winter storage",
            "Back to school car refresh"
        ]
    }
    
    for months, angles in seasonal.items():
        if month in months:
            return angles
    return []
```

### 2. Add Customer Type Targeting

```python
self.customer_types = {
    "luxury": {
        "cars": ["BMW", "Mercedes", "Tesla", "Porsche"],
        "angles": ["Premium service", "Concierge detailing", "Paint protection"],
        "hashtags": ["#LuxuryCars", "#ExoticCars", "#LuxuryLifestyle"]
    },
    "family": {
        "cars": ["SUV", "Minivan", "Crossover"],
        "angles": ["Kid-friendly cleaning", "Pet hair removal", "Stain removal"],
        "hashtags": ["#MomLife", "#DadLife", "#FamilyCar"]
    },
    "enthusiast": {
        "cars": ["Sports car", "Classic car", "Modified car"],
        "angles": ["Paint correction", "Show car prep", "Ceramic coating"],
        "hashtags": ["#CarEnthusiast", "#CarCommunity", "#ModifiedCars"]
    }
}
```

### 3. Add Video Length Optimization

```python
def optimize_for_length(self, concept: Dict, target_length: int) -> Dict:
    """Adjust video concept for specific length"""
    if target_length <= 15:
        return {
            **concept,
            "shots": concept["shots"][:2],  # Quick cuts only
            "tip": "15s videos: Lead with your strongest hook"
        }
    elif target_length <= 30:
        return {
            **concept,
            "tip": "30s videos: Hook + Quick transformation + CTA"
        }
    else:
        return {
            **concept,
            "tip": "60s videos: Full story with education and entertainment"
        }
```

### 4. Add Competitor Analysis Features

```python
self.trending_topics_in_niche = [
    "TikTok made me buy it (detailing products)",
    "Things I wish I knew before detailing",
    "Detailing red flags to avoid",
    "Is professional detailing worth it?",
    "How to choose a detailer"
]

def generate_competitor_differentiator(self) -> str:
    """Generate content that sets you apart"""
    differentiators = [
        "We come to you - no need to waste time at a shop",
        "Eco-friendly products that protect your car and the planet",
        "Military veteran owned and operated",
        "10+ years experience, 1000+ satisfied customers",
        "Satisfaction guaranteed or your money back",
    ]
    return random.choice(differentiators)
```

### 5. Add Analytics Placeholders

```python
def add_tracking_to_post(self, post: Dict, campaign: str = None) -> Dict:
    """Add tracking information to posts"""
    tracking_code = f"TT-{datetime.now().strftime('%Y%m%d')}"
    if campaign:
        tracking_code += f"-{campaign}"
    
    post["tracking"] = {
        "code": tracking_code,
        "campaign": campaign,
        "platform": "TikTok",
        "generated_date": datetime.now().isoformat()
    }
    return post
```

## Content Strategy Customizations

### 1. Define Your Content Pillars

```python
self.content_pillars = {
    "educational": {
        "percentage": 30,
        "topics": ["How-tos", "Tips", "Product reviews"],
        "goal": "Build trust and authority"
    },
    "transformational": {
        "percentage": 40,
        "topics": ["Before/after", "Time-lapses", "Results"],
        "goal": "Showcase your work"
    },
    "relational": {
        "percentage": 20,
        "topics": ["Behind scenes", "Meet the team", "Story time"],
        "goal": "Build connection"
    },
    "promotional": {
        "percentage": 10,
        "topics": ["Specials", "Availability", "Booking"],
        "goal": "Drive conversions"
    }
}
```

### 2. Add Posting Schedule Optimizer

```python
def get_optimal_posting_time(self, day_of_week: int) -> List[str]:
    """Get best times based on day of week"""
    schedule = {
        0: ["7:00 AM", "12:00 PM", "7:00 PM"],  # Monday
        1: ["7:30 AM", "12:30 PM", "8:00 PM"],  # Tuesday
        2: ["7:00 AM", "1:00 PM", "7:30 PM"],   # Wednesday
        3: ["7:00 AM", "12:00 PM", "9:00 PM"],  # Thursday
        4: ["8:00 AM", "12:00 PM", "7:00 PM"],  # Friday
        5: ["9:00 AM", "2:00 PM", "8:00 PM"],   # Saturday
        6: ["10:00 AM", "1:00 PM", "8:00 PM"],  # Sunday
    }
    return schedule.get(day_of_week, schedule[0])
```

### 3. Create Service-Specific Templates

```python
self.service_templates = {
    "ceramic_coating": {
        "hook": "This ceramic coating will last 5 years! Here's why it's worth it:",
        "focus": "Show water beading, scratch resistance, glossy finish",
        "cta": "DM for ceramic coating quotes!",
        "price_range": "$500-$1500"
    },
    "interior_detail": {
        "hook": "The before is going to shock you 🤢",
        "focus": "Show dirt extraction, stain removal, fresh result",
        "cta": "Book your interior refresh today!",
        "price_range": "$150-$300"
    },
    "paint_correction": {
        "hook": "Watch these scratches disappear ✨",
        "focus": "Show swirls, correction process, final gloss",
        "cta": "Get a free paint assessment!",
        "price_range": "$300-$800"
    }
}
```

## Testing Your Customizations

After making changes, test them:

```bash
# Test that everything still works
python3 content_generator.py --type post

# Test with your custom topic
python3 content_generator.py --type post --topic "your-custom-service"

# Generate a calendar to see variety
python3 content_generator.py --type calendar --days 7
```

## Pro Tips

1. **Keep It Real**: Use language that sounds like you, not a robot
2. **Local Flavor**: Add local references, landmarks, team names
3. **Test and Iterate**: Track what performs best and update your templates
4. **Stay Current**: Update hooks and angles based on trending TikTok content
5. **Be Consistent**: Your brand voice should be recognizable across all posts

## Next Steps

1. Make your customizations
2. Generate a week of content
3. Post and track performance
4. Update your templates based on results
5. Repeat!

---

Remember: The best customizations come from understanding YOUR audience and YOUR unique value proposition. Make this tool reflect what makes your mobile detailing business special!
