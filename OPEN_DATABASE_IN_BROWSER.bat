@echo off
cd /d "%~dp0"
title Opening Live Database in Browser...
py generate_db_html.py >nul 2>&1
start "" "VIEW_DATABASE.html"
exit
