@echo off
cd /d "%~dp0"
title Employee Preparation Platform - Live Database Viewer
color 0A
echo ========================================================
echo   AI EMPLOYEE PREPARATION PLATFORM - DATABASE VIEWER
echo ========================================================
echo.
py view_database.py
if %ERRORLEVEL% NEQ 0 (
    python view_database.py
)
echo.
pause
