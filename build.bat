@echo off
echo ============================================
echo   Building Focus ELO Desktop App
echo ============================================
echo.

:: Install PyInstaller if needed
echo [1/2] Installing PyInstaller...
pip install pyinstaller >nul 2>&1
echo        Done.
echo.

:: Build single-file exe with the HTML bundled
echo [2/2] Building FocusELO.exe ...
pyinstaller --onefile --noconsole --name FocusELO --icon=NONE --add-data "index.html;." app.py

echo.
echo ============================================
if exist "dist\FocusELO.exe" (
    echo   SUCCESS! Your app is at:
    echo   dist\FocusELO.exe
) else (
    echo   Build failed. Check errors above.
)
echo ============================================
echo.
pause
