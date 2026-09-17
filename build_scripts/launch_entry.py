"""
Entry point for the standalone "IMS Platform Explorer" executable.
This file is intentionally minimal -- PyInstaller's Analysis needs a
single top-level script to trace imports from; all real logic lives in
`ims_platform.launcher`, which is fully unit-tested independently of
this file (see tests/test_launcher.py).
"""
import sys
from ims_platform.launcher import main

if __name__ == "__main__":
    sys.exit(main())
