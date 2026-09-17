@echo off
title AI Employee Preparation Platform Launcher
color 0A

echo ======================================================================
echo          AI EMPLOYEE PREPARATION PLATFORM - COLLEGE DEMO
echo ======================================================================
echo.

:: 1. Verify Python Installation
echo [1/4] Checking Python environment...
if exist "%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe" (
    set "PY_CMD=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
) else if exist "C:\Users\JOHN\AppData\Local\Python\pythoncore-3.14-64\python.exe" (
    set "PY_CMD=C:\Users\JOHN\AppData\Local\Python\pythoncore-3.14-64\python.exe"
) else (
    py --version >nul 2>&1
    if %errorlevel% equ 0 (
        set PY_CMD=py
    ) else (
        python --version >nul 2>&1
        if %errorlevel% equ 0 (
            set PY_CMD=python
        ) else (
            color 0C
            echo [ERROR] Python is not found on your system!
            echo Please install Python 3.10+ from python.org.
            pause
            exit /b 1
        )
    )
)
echo [✔] Using Python executable: %PY_CMD%

:: 2. Initialize Database & Seed Demo Data
echo.
echo [2/4] Initializing SQLite database and verifying seeds...
%PY_CMD% -c "from backend.database import init_db; init_db(); print('✔ Database initialized with full schema and demo candidate.')"
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Failed to initialize database!
    pause
    exit /b 1
)

:: 3. Kill any lingering process on port 5000 (clean restart)
echo.
echo [3/4] Preparing network port 5000...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":5000" ^| findstr "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

:: 4. Launch Chrome Browser after 2-second delay in background
echo.
echo [4/4] Starting Web Server and launching Google Chrome...
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://localhost:5000"

echo.
echo ======================================================================
echo ✔ Platform is now LIVE at: http://localhost:5000
echo ✔ Chrome will open automatically!
echo.
echo [DEMO CREDENTIALS]
echo   Student: student@prep.com  / Password: Student123!
echo   Admin:   admin@prep.com    / Password: AdminPassword123!
echo.
echo (Press Ctrl + C in this window to stop the server when finished)
echo ======================================================================
echo.

%PY_CMD% run.py
pause
