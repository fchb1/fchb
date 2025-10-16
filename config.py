import os
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = os.getenv('OUTPUT_DIR', './output')
TEMP_DIR = os.getenv('TEMP_DIR', './temp')
MAX_VIDEO_LENGTH = int(os.getenv('MAX_VIDEO_LENGTH', 60))
MIN_VIDEO_LENGTH = int(os.getenv('MIN_VIDEO_LENGTH', 15))
CLIPS_PER_VIDEO = int(os.getenv('CLIPS_PER_VIDEO', 3))
GENERATION_INTERVAL_HOURS = int(os.getenv('GENERATION_INTERVAL_HOURS', 1))
VIDEO_RESOLUTION = os.getenv('VIDEO_RESOLUTION', '1080x1920')

MOTIVATIONAL_KEYWORDS = [
    'courage motivation',
    'mental strength',
    'believe in yourself',
    'overcome fear',
    'stay strong motivation',
    'never give up',
    'build confidence',
    'mental toughness',
    'face your fears',
    'self belief motivation'
]

TOP_CREATORS = [
    '@MotivationMaestro',
    '@GaryVee',
    '@TonyRobbins',
    '@LesB',
    '@DavidGoggins',
    '@BryanStrongJr',
    '@TheRealAlexMorton'
]

MOTIVATIONAL_QUOTES = [
    "Courage is not the absence of fear, but the triumph over it.",
    "Your mental strength is your greatest asset.",
    "Believe in yourself and magic will happen.",
    "The only limit is the one you set yourself.",
    "Mental toughness is built through small daily wins.",
    "You are stronger than you think.",
    "Fear is temporary, regret is forever.",
    "Push yourself because no one else will do it for you.",
    "Great things never come from comfort zones.",
    "Your mindset determines your success.",
    "Embrace the struggle, it's building you.",
    "Courage isn't having the strength to go on, it's going on when you don't have strength.",
    "Mental strength is the foundation of all achievement.",
    "Believe you can and you're halfway there.",
    "The harder you work for something, the greater you'll feel when you achieve it."
]

TEXT_STYLES = {
    'font': 'Arial-Bold',
    'fontsize': 70,
    'color': 'white',
    'stroke_color': 'black',
    'stroke_width': 3,
    'method': 'caption',
    'align': 'center'
}
