@echo off
REM SGX Downloader batch script cho Windows

echo SGX Data Downloader
echo ==================

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python khong tim thay! Cai Python truoc.
    pause
    exit /b 1
)

REM Install requirements nếu cần
if not exist "downloads" mkdir downloads

echo Chon tuy chon:
echo 1. Tai file hom nay
echo 2. Tai file ngay cu the
echo 3. Test he thong

set /p choice="Nhap lua chon (1-3): "

if "%choice%"=="1" (
    python main.py --today --verbose
) else if "%choice%"=="2" (
    set /p date_input="Nhap ngay (YYYY-MM-DD): "
    python main.py --date %date_input% --verbose
) else if "%choice%"=="3" (
    python test.py
) else (
    echo Lua chon khong hop le!
)

pause
