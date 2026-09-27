@echo off
setlocal
echo =======================================================
echo    Next-Gen AI Employee Preparation Platform
echo         Download Microsoft Word Report (.docx)
echo =======================================================
echo.

set "SRC=%~dp0FINAL_PROJECT_REPORT.docx"
set "DEST_DOWNLOADS=%USERPROFILE%\Downloads\FINAL_PROJECT_REPORT.docx"
set "DEST_DESKTOP=%USERPROFILE%\Desktop\FINAL_PROJECT_REPORT.docx"

echo [1/3] Copying latest Word Report to your Downloads folder...
copy /Y "%SRC%" "%DEST_DOWNLOADS%" >nul

echo [2/3] Copying latest Word Report to your Desktop screen...
copy /Y "%SRC%" "%DEST_DESKTOP%" >nul

echo [3/3] Opening file location in Windows Explorer...
echo.
echo SUCCESS! Your Word file is ready at:
echo 1. Downloads: %DEST_DOWNLOADS%
echo 2. Desktop:   %DEST_DESKTOP%
echo.
echo Opening your Downloads folder now...
explorer.exe /select,"%DEST_DOWNLOADS%"

echo.
echo Opening Word document in Microsoft Word...
start "" "%DEST_DESKTOP%"

exit /b 0
