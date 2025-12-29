# Quick Start Guide - AI Content Platform

## 🎯 Important: This is ONE Server (Not Separate Frontend/Backend)

FastAPI serves **both** the backend API and frontend HTML together. You only need to run **one command**.

## 📦 Step 1: Database Setup

**Good news:** The database creates itself automatically! 

When you run the server, it will create `content.db` in your project folder. No manual setup needed.

## 🚀 Step 2: Run the Server

### Option A: Simple Command (Recommended)
```bash
cd c:\Users\USER\OneDrive\Desktop\Ai-Content
uvicorn main:app --reload
```

The server will start on: **http://127.0.0.1:8000**

### Option B: Custom Port
```bash
uvicorn main:app --reload --port 8080
```

## 🌐 Step 3: Access the Application

Open your browser and go to:
- **Landing Page:** http://127.0.0.1:8000
- **Dashboard:** http://127.0.0.1:8000/dashboard
- **History:** http://127.0.0.1:8000/history

## 📂 What Gets Created

When you run the server, these files are auto-created:
```
Ai-Content/
├── content.db          ← SQLite database (auto-created)
└── __pycache__/        ← Python cache (auto-created)
```

## ✅ Verification

After starting the server, you should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

## 🔧 Troubleshooting

### If you see errors about missing modules:
```bash
pip install -r requirements.txt
```

### If port 8000 is busy:
```bash

uvicorn main:app --reload --port 8080
```

### To stop the server:
Press `Ctrl + C` in the terminal

## 📝 How It Works

```
Browser Request
     ↓
http://127.0.0.1:8000
     ↓
FastAPI Server (main.py)
     ↓
├─→ HTML Pages (templates/)     ← Frontend
├─→ Static Files (css/js)       ← Frontend Assets
└─→ API Endpoints (/api/*)      ← Backend Logic
     ↓
Database (content.db)
```

## 🎨 Frontend Files Location

The frontend is in these folders:
- `templates/` - HTML pages
- `static/css/` - Stylesheets
- `static/js/` - JavaScript

FastAPI automatically serves them when you visit the URLs.

## 🔑 Remember

- **One server** runs everything
- **Database** creates automatically
- **No separate frontend server** needed
- **Just run:** `uvicorn main:app --reload`
