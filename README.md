<<<<<<< HEAD
# AI Content Generation Platform

## 🚀 Quick Start (3 Steps)

### 1. Open Terminal
```bash
cd c:\Users\USER\OneDrive\Desktop\Ai-Content
```

### 2. Run Server
```bash
python -m uvicorn main:app --reload
```

### 3. Open Browser
Go to: **http://127.0.0.1:8000**

---

## ✅ What You Get

- **Landing Page** - http://127.0.0.1:8000
- **Dashboard** - http://127.0.0.1:8000/dashboard (4 AI generators)
- **History** - http://127.0.0.1:8000/history (saved content)

## 📊 Database

The SQLite database (`content.db`) is created **automatically** when you first run the server. No setup needed!

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML + CSS + JavaScript
- **Database:** SQLite (auto-created)
- **AI:** OpenAI GPT + DALL-E

## 📁 Project Structure

```
Ai-Content/
├── main.py                 # FastAPI app (entry point)
├── requirements.txt        # Dependencies
├── .env                    # API keys
├── content.db             # Database (auto-created)
│
├── app/                   # Backend package
│   ├── config.py          # Settings
│   ├── database.py        # SQLAlchemy models
│   ├── models.py          # Pydantic schemas
│   └── services/          # Business logic
│       ├── openai_service.py
│       └── content_service.py
│
├── templates/             # HTML pages
│   ├── base.html
│   ├── index.html         # Landing
│   ├── dashboard.html     # Generators
│   └── history.html       # Content history
│
└── static/                # Frontend assets
    ├── css/
    │   ├── main.css
    │   └── components.css
    └── js/
        ├── app.js
        ├── generators.js
        └── history.js
```

## 🎯 Features

1. **Ad Copy Generator** - Create marketing content
2. **Image Generator** - DALL-E powered visuals
3. **Blog Post Writer** - SEO-optimized articles
4. **Social Media Posts** - Platform-specific content
5. **Content History** - Save and manage all generated content

## 🔑 API Key

Your OpenAI API key is in `.env`:
```
OPENAI_API_KEY=sk-proj-...
```

## 💡 Usage

1. Start the server (see Quick Start above)
2. Open http://127.0.0.1:8000 in browser
3. Click "Start Creating"
4. Choose a generator tab
5. Fill the form and click Generate

## 🐛 Troubleshooting

**Server won't start?**
```bash
pip install -r requirements.txt
```

**Port already in use?**
```bash
python -m uvicorn main:app --reload --port 8080
```

**Stop the server:**
Press `Ctrl + C`

---

Made with ❤️ using FastAPI + OpenAI
=======
# AI---Content-Generater
>>>>>>> 6f51c6b4032d92fd18075a8a8c632ff1eb19b70f
