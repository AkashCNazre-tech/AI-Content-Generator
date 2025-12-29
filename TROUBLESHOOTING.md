# Troubleshooting Guide

## ❌ Error: SQLAlchemy + Python 3.13 Compatibility

You're using **Python 3.13** which has compatibility issues with some packages.

## ✅ Solution Options

### Option 1: Use Test Server (Quick Fix)
Run the simplified server without database:
```bash
python test_server.py
```
Then open: http://127.0.0.1:8000

**Note:** This won't save content history, but all generators will work.

### Option 2: Downgrade Python (Recommended)
Install **Python 3.11** or **3.12**:
1. Download from https://www.python.org/downloads/
2. Install Python 3.11.x or 3.12.x
3. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run server:
   ```bash
   uvicorn main:app --reload
   ```

### Option 3: Wait for Package Updates
SQLAlchemy and other packages are being updated for Python 3.13 compatibility.

## 🔍 Check Your Python Version
```bash
python --version
```

## 📝 What I Fixed
- ✅ Updated SQLAlchemy to 2.0.36+
- ✅ Changed to DeclarativeBase (SQLAlchemy 2.0 style)
- ✅ Created test_server.py as fallback

## 🚀 Quick Start (If Server is Running)

If you see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

Then open your browser to:
- http://127.0.0.1:8000 (Landing page)
- http://127.0.0.1:8000/dashboard (Generators)
- http://127.0.0.1:8000/test (Test endpoint)

## 💡 Alternative: Use Virtual Environment

```bash

py -3.11 -m venv venv


venv\Scripts\activate


pip install -r requirements.txt


uvicorn main:app --reload
```

## ⚠️ Known Issues

- **Python 3.13** is very new (released Oct 2024)
- Some packages haven't fully updated yet
- **Recommended:** Use Python 3.11 or 3.12 for best compatibility
