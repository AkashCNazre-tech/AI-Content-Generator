@echo off
cd /d "%~dp0"
echo Starting both AI Content Generation Servers...
start "Simple Server" start_simple.bat
start "Full Server" start_full.bat
echo Servers launched in separate windows.
pause