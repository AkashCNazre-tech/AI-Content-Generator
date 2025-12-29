# Running Both Servers Simultaneously

## Quick Start

### Option 1: Using Batch Scripts (Easiest)

Open **two separate terminal windows**:

**Terminal 1 - Simple Version:**
```bash
cd c:\Users\USER\OneDrive\Desktop\Ai-Content
start_simple.bat
```
- Runs on: http://127.0.0.1:8000
- Features: Basic content generation (no database)

**Terminal 2 - Full Version:**
```bash
cd c:\Users\USER\OneDrive\Desktop\Ai-Content
start_full.bat
```
- Runs on: http://127.0.0.1:8001
- Features: Content generation + database + history tracking

---

### Option 2: Manual Commands

**Terminal 1:**
```bash
cd c:\Users\USER\OneDrive\Desktop\Ai-Content
python main_simple.py
```

**Terminal 2:**
```bash
cd c:\Users\USER\OneDrive\Desktop\Ai-Content
uvicorn main:app --reload --port 8001
```

---

## Access the Applications

- **Simple Version**: http://127.0.0.1:8000
- **Full Version**: http://127.0.0.1:8001

---

## Differences Between Versions

### Simple Version (Port 8000)
- ✅ Lightweight
- ✅ No database required
- ✅ All 4 content generators
- ❌ No content history
- ❌ No content persistence

### Full Version (Port 8001)
- ✅ Professional architecture
- ✅ SQLite database
- ✅ Content history tracking
- ✅ Save/delete generated content
- ✅ Better for portfolio/recruiters

---

## Stopping the Servers

Press `Ctrl+C` in each terminal window to stop the respective server.
