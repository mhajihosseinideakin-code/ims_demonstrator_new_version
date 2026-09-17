# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for the standalone "IMS Platform Explorer" executable.
#
# Build from the project root (the directory containing ims_platform/):
#     pyinstaller build_scripts/ims_explorer.spec
#
# Output: dist/IMS Platform Explorer/  (onedir build; see BUILD_INSTRUCTIONS.md
# for why onedir is recommended over --onefile for this application).
#
# IMPORTANT, UNTESTED IN THE DEVELOPMENT SANDBOX: this spec file was
# written against documented PyInstaller behaviour (data-file bundling,
# sys._MEIPASS resolution, hidden-import discovery for packages that use
# dynamic imports) but has not been run end-to-end, because neither
# PyInstaller nor a display/Tkinter environment was available in the
# sandbox this project was developed in (no network access to install
# PyInstaller; no Tkinter to verify the GUI path even if it were
# installed). Treat the first build on a real machine as the first real
# test of this file, and see BUILD_INSTRUCTIONS.md's troubleshooting
# section for the specific things most likely to need adjustment.

import sys
from pathlib import Path

block_cipher = None
project_root = Path(SPECPATH).parent  # SPECPATH is provided by PyInstaller at spec-exec time

a = Analysis(
    [str(project_root / "build_scripts" / "launch_entry.py")],
    pathex=[str(project_root)],
    binaries=[],
    datas=[
        (str(project_root / "ims_platform" / "server" / "static"), "ims_platform/server/static"),
    ],
    hiddenimports=[
        # Flask's own import graph is normally auto-discovered, but list
        # it and its own soft dependencies explicitly, since Flask/
        # Werkzeug's use of pkg_resources / dynamic module resolution
        # can trip up PyInstaller's static import scanner.
        "flask", "werkzeug", "jinja2", "click", "itsdangerous", "markupsafe",
        # Scientific stack: numpy/scipy dynamically load compiled
        # extension submodules that PyInstaller's scanner can miss.
        "numpy", "scipy", "scipy.optimize", "scipy.integrate", "scipy.linalg",
        "scipy.special", "scipy.sparse", "sympy",
        # This project's own package tree, in case any submodule is only
        # ever imported dynamically (none currently are, to the authors'
        # knowledge, but the scanner starts from launch_entry.py's single
        # `from ims_platform.launcher import main`, which does not by
        # itself statically reach every submodule server.app imports at
        # call time).
        "ims_platform", "ims_platform.core", "ims_platform.core.system", "ims_platform.core.simulator",
        "ims_platform.engine", "ims_platform.engine.symbolic",
        "ims_platform.ims", "ims_platform.ims.manifold", "ims_platform.ims.recoverability",
        "ims_platform.control", "ims_platform.control.mrc", "ims_platform.control.mrc_synthesis",
        "ims_platform.models", "ims_platform.models.grid_forming_inverter",
        "ims_platform.models.dc_microgrid_cpl", "ims_platform.models.converter_cpl_paper",
        "ims_platform.network", "ims_platform.network.assembler", "ims_platform.network.converter",
        "ims_platform.network.converter_topologies", "ims_platform.network.converter_cpl_electrical_model",
        "ims_platform.server", "ims_platform.server.app",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="IMS Platform Explorer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,   # windowed: no console flash on double-click (see BUILD_INSTRUCTIONS.md
                      # for the console=True debug variant if the windowed build shows nothing)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,        # add an .ico (Windows) / .icns (macOS) path here for a custom icon
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="IMS Platform Explorer",
)
