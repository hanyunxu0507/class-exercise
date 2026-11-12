@echo off
rem ---------------------------------------------------------------
rem  Start the hands-on 1 Flask app on port 2027, reachable on LAN.
rem  Change PORT below if you want a different port (e.g. 8080).
rem ---------------------------------------------------------------
cd /d "%~dp0"
set PORT=2027

rem Prefer the real Python interpreter (the Store alias silently fails).
set PY=C:\Users\26430\AppData\Local\Python\pythoncore-3.14-64\python.exe
if not exist "%PY%" set PY=python

echo Starting hands-on 1 on port %PORT% ...
"%PY%" app.py

echo.
echo Server stopped. Press any key to close.
pause >nul
