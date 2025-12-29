@echo off
cd /d "%~dp0"
title Local AI Launcher

echo =================================================
echo      Local AI Content Generator - Auto Run
echo =================================================

echo.
echo [Step 1] Installing Python Libraries...
pip install -r requirements.txt

echo.
echo [Step 2] Starting Ollama Server...
echo (This will open in a separate window. Do not close it!)
start "Ollama Server" cmd /k "%~dp0start_ollama_server.bat"

echo.
echo Waiting 10 seconds for server to wake up...
timeout /t 10 /nobreak >nul

echo.
echo [Step 3] Checking AI Model...
call install_model.bat

echo.
echo [Step 4] Starting Streamlit App...
streamlit run app.py
pause