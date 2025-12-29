@echo off
cd /d "%~dp0"
echo Starting Local AI Content Generator...
echo Ensure Ollama is running in the background!
echo.
streamlit run app.py
pause