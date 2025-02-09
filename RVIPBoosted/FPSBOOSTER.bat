@echo off
:: Check if Python is installed
python --version >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Installing Python...
    :: Download Python installer
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.4/python-3.11.4.exe -OutFile python_installer.exe"
    :: Run Python installer
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    echo Python installation completed.
) ELSE (
    echo Python is already installed.
)

:: Check if pip is installed
python -m pip --version >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Installing pip...
    :: Ensure the correct version of pip is installed
    python -m ensurepip --upgrade
    echo pip installation completed.
) ELSE (
    echo pip is already installed.
)

:: Clean up
del /f /q python_installer.exe

:: Wait for 2 seconds and then clear screen
timeout /t 2 >nul
cls

:: Navigate to the specified directory and run the Python script
cd C:\Users\nonoh\OneDrive\Desktop\RVIPBoosted\DO-NOT-TOUCH
py R_VIP_BOOSTED.py

pause
