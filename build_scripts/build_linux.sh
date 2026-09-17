#!/usr/bin/env bash
# Build the standalone Linux executable for IMS Platform Explorer.
# Run this from the project root (the folder containing ims_platform/).
#
# Prerequisites:
#   - Python 3.9+ with Tkinter: on Debian/Ubuntu, `apt install python3-tk`
#     first if `python3 -c "import tkinter"` fails -- most distro Python
#     packages do NOT include Tkinter by default (unlike the Windows/
#     macOS python.org installers), unlike this project's own
#     development sandbox, which lacks it entirely (see
#     BUILD_INSTRUCTIONS.md for what that means for this build).
#   - This package installed: pip install -e .
#   - PyInstaller:             pip install pyinstaller
set -euo pipefail

echo "Installing the package and PyInstaller..."
pip install -e .
pip install pyinstaller

echo "Building..."
pyinstaller build_scripts/ims_explorer.spec --noconfirm

echo ""
echo "Build complete. Find it at: dist/IMS Platform Explorer/IMS Platform Explorer"
echo "Run it directly, or from a file manager if it is marked executable"
echo "(chmod +x if needed)."
