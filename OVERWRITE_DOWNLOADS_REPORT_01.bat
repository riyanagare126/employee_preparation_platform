@echo off
setlocal
echo ========================================================
echo   Updating FINAL_PROJECT_REPORT_01.docx in Downloads
echo ========================================================
echo.

set "SRC=%USERPROFILE%\Desktop\FINAL_PROJECT_REPORT_01.docx"
set "DEST=%USERPROFILE%\Downloads\FINAL_PROJECT_REPORT_01.docx"

echo Attempting to overwrite %DEST%...
copy /Y "%SRC%" "%DEST%" >nul 2>&1

if %ERRORLEVEL% EQU 0 (
    echo SUCCESS! The file in your Downloads folder has been updated.
    echo Opening file in Microsoft Word...
    start "" "%DEST%"
) else (
    echo.
    echo NOTE: Please close the Microsoft Word window if you currently have
    echo FINAL_PROJECT_REPORT_01.docx open, and then run this file again!
    echo.
    pause
)
exit /b 0
