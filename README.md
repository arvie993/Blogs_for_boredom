# 🎯 Bored No More! - Things To Do When You're Bored

A beautiful, interactive blog website built with Flask and Jinja2 that helps you discover fun activities when you're feeling bored. Features dynamic content from APIs, category filtering, and a random activity generator!

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 📚 Curated Activities
- 8 hand-picked activities across multiple categories
- Each activity includes:
  - Difficulty level (Easy/Medium/Hard)
  - Time needed
  - Pro tips to get started
  - Featured highlighting

### 🏷️ Category Filtering
- **Creative** - Cooking, music, DIY projects
- **Mindfulness** - Journaling, meditation
- **Outdoor** - Nature walks, exploration
- **Entertainment** - Movie marathons
- **Educational** - Language learning
- **Productive** - Organizing, decluttering

### 🔄 Fresh API Content
Every page load fetches new suggestions from:
- **Bored API** - Random activity suggestions
- **Advice Slip API** - Daily advice
- **ZenQuotes API** - Inspirational quotes

### 🎲 Random Activity Generator
A dedicated page that fetches random activities from the Bored API with a fun, animated interface.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Templating**: Jinja2
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: Bored API, Advice Slip API, ZenQuotes API

## 📁 Project Structure

```
day-57-starting-files-blog-templating/
├── main.py                 # Flask application with routes
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── static/
│   └── css/
│       └── styles.css     # Main stylesheet
└── templates/
    ├── index.html         # Home page with all activities
    ├── activity.html      # Individual activity detail page
    ├── category.html      # Category filter page
    └── random.html        # Random activity generator
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arvie993/Blogs_for_boredom.git
   cd Blogs_for_boredom
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 🎨 Jinja2 Features Demonstrated

This project showcases various Jinja2 templating features:

### Loops
```jinja2
{% for post in posts %}
    <div class="card">{{ post.title }}</div>
{% endfor %}
```

### Conditionals
```jinja2
{% if post.featured %}
    <span class="badge">⭐ Featured</span>
{% endif %}
```

### Multiline Statements with Whitespace Control
```jinja2
{%- if post.difficulty == "Easy" -%}
    🟢 Easy
{%- elif post.difficulty == "Medium" -%}
    🟡 Medium
{%- else -%}
    🔴 Hard
{%- endif -%}
```

### Filters
```jinja2
{{ posts | length }}
{{ featured_posts | length - 1 }}
```

### Loop Variables
```jinja2
{% for tip in post.tips %}
    {% if loop.first %}<strong>Start here:</strong>{% endif %}
    {{ tip }}
    {% if loop.last %} 🎉{% endif %}
{% endfor %}
```

### URL Building
```jinja2
{{ url_for('activity_detail', post_id=post.id) }}
{{ url_for('category_page', category_name=post.category) }}
{{ url_for('static', filename='css/styles.css') }}
```

## 📱 Pages & Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with all activities |
| `/activity/<id>` | Detail page for specific activity |
| `/category/<name>` | Activities filtered by category |
| `/random` | Random activity generator |

## 👤 Author

**arvie993**
- GitHub: [@arvie993](https://github.com/arvie993)

## 🤝 Contributing

Feel free to fork this project and submit pull requests!

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Bored API](https://bored-api.appbrewery.com/) - Random activity suggestions
- [Advice Slip API](https://api.adviceslip.com/) - Daily advice
- [ZenQuotes API](https://zenquotes.io/) - Inspirational quotes
- Built as part of 100 Days of Python challenge

---

Made with ❤️ and Python 🐍
