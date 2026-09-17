#!/usr/bin/env bash
# Build the standalone macOS app bundle for IMS Platform Explorer.
# Run this from the project root (the folder containing ims_platform/).
#
# Prerequisites:
#   - Python 3.9+ from python.org (includes Tkinter by default) --
#     the Python bundled with Xcode Command Line Tools or Homebrew's
#     `python3` may need `brew install python-tk` for Tkinter support.
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
echo "On first launch, macOS Gatekeeper will likely block an unsigned build --"
echo "see BUILD_INSTRUCTIONS.md for how to allow it (or codesign it) before distributing."
