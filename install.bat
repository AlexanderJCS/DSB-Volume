@echo off
setlocal

:: Check for admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -WorkingDirectory '%~dp0' -Verb RunAs"
    exit /b
)

set "SCRIPT_DIR=%~dp0"

set "DRAGONFLY_PROGRAMDATA=C:\ProgramData\Comet\Dragonfly2025.1"
set "DRAGONFLY_INSTALL=C:\Program Files\Dragonfly"

:: Copy files
echo Copying files...
xcopy "%SCRIPT_DIR%*.*" "%DRAGONFLY_PROGRAMDATA%\pythonAllUsersExtensions\Plugins\DSB_Volume_045f5ca4127611f1bb63e0d55e2bb93d" /E /I /Y >nul

:: Install Python dependencies
echo Installing Python dependencies...
"%DRAGONFLY_INSTALL%\Python_env\python.exe" -m pip install -r "%DRAGONFLY_PROGRAMDATA%\pythonAllUsersExtensions\Plugins\DSB_Volume_045f5ca4127611f1bb63e0d55e2bb93d\requirements.txt"

:: echo( is a newline
echo(
echo Complete. Please restart Dragonfly to apply changes.
pause