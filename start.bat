@echo off
title WPlace Auto Claimer Bot
echo Starting WPlace Auto Claimer Bot...

REM --- Install dependencies ---
echo Installing required packages...
call pip install -r requirements.txt

REM --- Run the bot ---
echo Launching bot...
call python main.py

echo.
echo Bot finished running.
pause
