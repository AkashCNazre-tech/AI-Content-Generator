@echo off
title Ollama Server
echo Checking for Ollama installation...

REM Try running via global command
WHERE ollama >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    echo Ollama found in PATH. Starting server...
    ollama serve
    goto :EOF
)

REM Try running via direct path (Default Windows Install Location)
IF EXIST "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" (
    echo Ollama found in AppData. Starting server...
    "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" serve
) ELSE (
    echo [ERROR] Ollama not found!
    echo Please install it from: https://ollama.com/download/windows
    pause
)