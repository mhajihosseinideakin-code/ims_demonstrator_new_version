@echo off
REM Build the standalone Windows executable for IMS Platform Explorer.
REM Run this from the project root (the folder containing ims_platform\).
REM
REM Prerequisites:
REM   - Python 3.9+ from python.org (includes Tkinter by default -- do
REM     NOT use a minimal/embeddable Python build, which excludes it)
REM   - This package installed: pip install -e .
REM   - PyInstaller:             pip install pyinstaller

echo Installing the package and PyInstaller...
pip install -e . || goto :error
pip install pyinstaller || goto :error

echo Building...
pyinstaller build_scripts\ims_explorer.spec --noconfirm || goto :error

echo.
echo Build complete. Find it at: dist\IMS Platform Explorer\IMS Platform Explorer.exe
echo Zip the whole "dist\IMS Platform Explorer" folder to distribute it --
echo the executable depends on the other files PyInstaller placed alongside it.
goto :eof

:error
echo.
echo Build FAILED. See BUILD_INSTRUCTIONS.md's troubleshooting section.
exit /b 1
