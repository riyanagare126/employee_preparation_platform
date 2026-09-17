@echo off
setlocal enabledelayedexpansion

echo =========================================================================
echo   AI Employee Preparation Platform - Push to GitHub
echo =========================================================================
echo.

set "GIT_EXE=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
if not exist "%GIT_EXE%" (
    where git >nul 2>nul
    if %errorlevel% equ 0 (
        set "GIT_EXE=git"
    ) else (
        echo [ERROR] Git was not found!
        pause
        exit /b 1
    )
)

set "DEFAULT_REPO=https://github.com/riyanagare126/employee_preparation_platform.git"

echo Target Repository:
echo   %DEFAULT_REPO%
echo.
echo Press any key to start pushing to GitHub...
echo (A browser window will open for 1-click GitHub authorization if not already logged in)
echo.
pause

echo.
echo [1/3] Setting remote origin...
"%GIT_EXE%" remote remove origin >nul 2>nul
"%GIT_EXE%" remote add origin %DEFAULT_REPO%

echo [2/3] Ensuring branch is 'main'...
"%GIT_EXE%" branch -M main

echo [3/3] Pushing to GitHub...
"%GIT_EXE%" push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo =========================================================================
    echo  SUCCESS! Project successfully pushed to GitHub!
    echo =========================================================================
    echo Check your repository:
    echo   https://github.com/riyanagare126/employee_preparation_platform
    echo.
    echo Next Steps:
    echo 1. Login to Supabase (https://supabase.com) with GitHub and run supabase_schema.sql.
    echo 2. Login to Render (https://render.com) with GitHub, create Web Service, and connect this repo!
) else (
    echo.
    echo =========================================================================
    echo [NOTICE] If prompted for GitHub login, please complete the browser login.
    echo If using a Personal Access Token (PAT), you can enter your username and PAT.
    echo =========================================================================
)

echo.
pause
exit /b %errorlevel%
