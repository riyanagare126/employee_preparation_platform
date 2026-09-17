@echo off
setlocal

echo =========================================================================
echo   AI Employee Preparation Platform - Supabase Connection Tester
echo =========================================================================
echo.

set /p DB_URL="Paste your Supabase Connection URI (or press ENTER to use .env): "

echo.
if "%DB_URL%"=="" (
    echo [INFO] Reading DATABASE_URL from .env file...
    py test_supabase_connection.py
) else (
    echo [INFO] Testing provided Supabase URL...
    py test_supabase_connection.py "%DB_URL%"
)

echo.
pause
exit /b %errorlevel%
