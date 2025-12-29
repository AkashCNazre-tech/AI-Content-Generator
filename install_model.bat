@echo off
title Install AI Model
echo.
echo Attempting to download 'llama3.2' model...
echo This may take a few minutes (approx 2GB).
echo.

REM Check if Ollama is in PATH
WHERE ollama >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    ollama pull llama3.2
    goto :SUCCESS
)

REM Check default install location
IF EXIST "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" (
    "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" pull llama3.2
    goto :SUCCESS
)

echo [ERROR] Could not find Ollama executable!
echo Please ensure Ollama is installed from ollama.com
pause
exit /b 1

:SUCCESS
echo.
echo Model installed successfully! You can close this window.
pause