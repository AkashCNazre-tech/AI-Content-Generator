@echo off
cd /d "%~dp0"
echo Starting AI Content Generation Platform - Full Version (with Database)
echo Server will run on http://127.0.0.1:8001
echo.
uvicorn main:app --reload --port 8001
pause
