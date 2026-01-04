from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)


def get_api_suggestions():
    """Fetch fresh suggestions from external APIs"""
    suggestions = []
    
    # Fetch from Bored API (multiple activities)
    try:
        for _ in range(3):
            response = requests.get("https://bored-api.appbrewery.com/random", timeout=5)
            if response.status_code == 200:
                data = response.json()
                suggestions.append({
                    "type": "activity",
                    "text": data.get("activity", ""),
                    "category": data.get("type", "").capitalize(),
                    "participants": data.get("participants", 1),
                    "price": "Free" if data.get("price", 0) == 0 else "Paid",
                    "accessibility": data.get("accessibility", 0)
                })
    except Exception as e:
        print(f"Bored API error: {e}")
    
    # Fetch random advice from Advice Slip API
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if "slip" in data:
                suggestions.append({
                    "type": "advice",
                    "text": data["slip"].get("advice", ""),
                    "id": data["slip"].get("id", 0)
                })
    except Exception as e:
        print(f"Advice API error: {e}")
    
    # Fetch a random quote from ZenQuotes API
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                suggestions.append({
                    "type": "quote",
                    "text": data[0].get("q", ""),
                    "author": data[0].get("a", "Unknown")
                })
    except Exception as e:
        print(f"Quote API error: {e}")
    
    return suggestions

# Blog posts data - things to do when bored
blog_posts = [
    {
        "id": 1,
        "title": "Learn a New Recipe",
        "emoji": "👨‍🍳",
        "category": "Creative",
        "difficulty": "Easy",
        "time_needed": "1-2 hours",
        "description": "Cooking is a fun and rewarding way to spend your time. Try making something you've never made before!",
        "tips": [
            "Start with simple recipes",
            "Watch cooking tutorials on YouTube",
            "Don't be afraid to experiment with flavors",
            "Take photos of your creations"
        ],
        "featured": True
    },
    {
        "id": 2,
        "title": "Start a Journal",
        "emoji": "📓",
        "category": "Mindfulness",
        "difficulty": "Easy",
        "time_needed": "15-30 minutes",
        "description": "Writing down your thoughts can help clear your mind and boost creativity.",
        "tips": [
            "Write without judgment",
            "Try gratitude journaling",
            "Use prompts if you're stuck",
            "Make it a daily habit"
        ],
        "featured": False
    },
    {
        "id": 3,
        "title": "Learn to Play an Instrument",
        "emoji": "🎸",
        "category": "Creative",
        "difficulty": "Medium",
        "time_needed": "30+ minutes daily",
        "description": "Pick up that guitar or keyboard you've been ignoring! There are tons of free tutorials online.",
        "tips": [
            "Start with basic chords",
            "Practice for short sessions regularly",
            "Learn songs you love",
            "Be patient with yourself"
        ],
        "featured": True
    },
    {
        "id": 4,
        "title": "Go for a Nature Walk",
        "emoji": "🌲",
        "category": "Outdoor",
        "difficulty": "Easy",
        "time_needed": "30-60 minutes",
        "description": "Fresh air and nature can do wonders for your mood. Explore a local park or trail!",
        "tips": [
            "Leave your phone behind (or on silent)",
            "Pay attention to sounds and smells",
            "Take photos of interesting plants",
            "Try to identify local birds"
        ],
        "featured": False
    },
    {
        "id": 5,
        "title": "Start a DIY Project",
        "emoji": "🔨",
        "category": "Creative",
        "difficulty": "Medium",
        "time_needed": "2-4 hours",
        "description": "Build something with your hands! From simple crafts to home improvements.",
        "tips": [
            "Start with upcycling old items",
            "Watch tutorials before starting",
            "Gather all materials first",
            "Don't aim for perfection"
        ],
        "featured": True
    },
    {
        "id": 6,
        "title": "Have a Movie Marathon",
        "emoji": "🎬",
        "category": "Entertainment",
        "difficulty": "Easy",
        "time_needed": "4-6 hours",
        "description": "Pick a theme or franchise and binge-watch! Make it special with snacks and cozy blankets.",
        "tips": [
            "Choose a theme (80s classics, horror, etc.)",
            "Prepare snacks in advance",
            "Invite friends virtually or in person",
            "Take breaks between movies"
        ],
        "featured": False
    },
    {
        "id": 7,
        "title": "Learn a New Language",
        "emoji": "🗣️",
        "category": "Educational",
        "difficulty": "Hard",
        "time_needed": "30 minutes daily",
        "description": "Apps like Duolingo make it easy and fun to learn new languages from your couch!",
        "tips": [
            "Set realistic daily goals",
            "Practice with native speakers online",
            "Watch shows in your target language",
            "Learn phrases, not just words"
        ],
        "featured": True
    },
    {
        "id": 8,
        "title": "Organize Your Space",
        "emoji": "🧹",
        "category": "Productive",
        "difficulty": "Medium",
        "time_needed": "1-3 hours",
        "description": "A clean space leads to a clear mind. Tackle that messy closet or desk drawer!",
        "tips": [
            "Start with one small area",
            "Use the 'spark joy' method",
            "Donate items you don't need",
            "Create a system that works for you"
        ],
        "featured": False
    }
]

# Categories for filtering
categories = ["All", "Creative", "Mindfulness", "Outdoor", "Entertainment", "Educational", "Productive"]


@app.route('/')
def home():
    current_year = datetime.now().year
    featured_posts = [post for post in blog_posts if post.get("featured")]
    
    # Fetch fresh suggestions from APIs
    api_suggestions = get_api_suggestions()
    
    return render_template(
        "index.html",
        posts=blog_posts,
        featured_posts=featured_posts,
        categories=categories,
        year=current_year,
        total_activities=len(blog_posts),
        api_suggestions=api_suggestions
    )


@app.route('/activity/<int:post_id>')
def activity_detail(post_id):
    """Show details for a specific activity"""
    current_year = datetime.now().year
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    if post is None:
        return render_template("404.html", year=current_year), 404
    return render_template(
        "activity.html",
        post=post,
        year=current_year,
        all_posts=blog_posts
    )


@app.route('/category/<category_name>')
def category_page(category_name):
    """Show all activities in a specific category"""
    current_year = datetime.now().year
    filtered_posts = [p for p in blog_posts if p["category"].lower() == category_name.lower()]
    return render_template(
        "category.html",
        posts=filtered_posts,
        category_name=category_name.capitalize(),
        year=current_year,
        categories=categories
    )


@app.route('/random')
def random_activity():
    """Get a random activity from the Bored API"""
    current_year = datetime.now().year
    activity = None
    try:
        response = requests.get("https://bored-api.appbrewery.com/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            activity = {
                "text": data.get("activity", ""),
                "category": data.get("type", "").capitalize(),
                "participants": data.get("participants", 1),
                "price": "Free" if data.get("price", 0) == 0 else "Paid",
                "link": data.get("link", "")
            }
    except Exception as e:
        print(f"Error fetching random activity: {e}")
    
    return render_template(
        "random.html",
        activity=activity,
        year=current_year
    )


if __name__ == "__main__":
    app.run(debug=True)
