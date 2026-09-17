# Building the Standalone IMS Platform Explorer Executable

## What this is, and an important limitation stated upfront

This produces a double-click executable with the user experience:

```
Double-click "IMS Platform Explorer"
        -> splash screen ("Starting IMS Platform Explorer...")
        -> browser opens automatically once the backend is ready
        -> Project Manager appears
```

**This must be built on the same operating system you want the executable for.** PyInstaller (the tool used here) does not cross-compile: running it on Linux produces a Linux executable, running it on Windows produces a Windows `.exe`, running it on macOS produces a macOS app. There is no way to produce a Windows `.exe` from a Linux machine without a full Windows environment (a real Windows machine, a VM, or Windows CI such as a GitHub Actions `windows-latest` runner).

**What has and has not been tested.** This project was developed in a Linux sandbox with no network access, where neither PyInstaller nor Tkinter (Python's bundled GUI toolkit, used for the splash/status window) could be installed. Concretely, that means:

| Component | Status |
|---|---|
| `launcher.ExplorerServer` (server startup, readiness polling, port/already-running detection) | **Tested** -- 8 automated tests, `tests/test_launcher.py`, including a full start-to-shutdown cycle |
| `launcher.run_console_mode` (console banner + blocking loop, used if Tkinter is unavailable) | **Tested** -- same suite, exercised end to end |
| `launcher.run_gui_mode` / the Tkinter splash and status windows | **Not tested.** Built from documented Tkinter APIs and kept deliberately simple, but this sandbox has no Tkinter to run it against. Treat your first build as the first real test of this code path specifically. |
| `build_scripts/ims_explorer.spec` (the PyInstaller build configuration) | **Not tested.** PyInstaller itself could not be installed here (no network access). Written against documented PyInstaller behaviour; see Troubleshooting below for the specific things most likely to need adjusting on a real build. |

None of this affects the underlying engine (all 59 platform tests, covering the Symbolic Engine, network assembly, converter topologies, and the full Explorer API, pass and are unaffected by any of the above) -- it is specifically the packaging/launcher layer that is unverified beyond what is stated in the table.

## Prerequisites

- Python 3.9 or later, **with Tkinter available** (`python3 -c "import tkinter"` should succeed with no error):
  - Windows/macOS: the standard installer from python.org includes Tkinter by default. Do not use a "minimal" or "embeddable" Python build.
  - Linux: install it explicitly first, e.g. `sudo apt install python3-tk` (Debian/Ubuntu) or the equivalent for your distribution.
  - If Tkinter genuinely isn't available at build time, the executable will still build and run, but will silently fall back to console mode (a visible console window with a text banner, not a splash screen) -- see the table above.
- This package's own dependencies (numpy, scipy, sympy, flask, etc.), installed via `pip install -e .` from the project root.
- PyInstaller: `pip install pyinstaller`.

## Building

From the project root (the folder containing `ims_platform/`):

**Windows:** double-click `build_scripts\build_windows.bat`, or run it from a command prompt.

**macOS / Linux:**
```bash
bash build_scripts/build_macos.sh   # or build_linux.sh
```

Each script installs dependencies and runs:
```bash
pyinstaller build_scripts/ims_explorer.spec --noconfirm
```

Output lands in `dist/IMS Platform Explorer/`, an **onedir** build (a folder containing the executable plus its dependencies), not a single `--onefile` executable. This is deliberate: onefile builds unpack themselves to a temporary directory on every launch, which is slower and, for an application bundling numpy/scipy/sympy, adds several seconds to every startup. Onedir starts faster and is easier to debug if something goes wrong. To distribute it, zip the whole `IMS Platform Explorer` folder -- the executable will not run correctly on its own, separated from the files PyInstaller placed alongside it.

## First-run checklist

After building, before considering it done:

1. Run the executable. You should see either the Tkinter splash window or (if Tkinter wasn't available at build time) a console window with a text banner -- either way, something should appear within a second or two.
2. Within ~20 seconds, your default browser should open to the Project Manager automatically.
3. Open a project (e.g. Buck Converter) and run it through all five pipeline stages, to confirm the bundled static files (`explorer.html`) and the full scientific stack (numpy/scipy/sympy) are correctly bundled and importable from inside the frozen executable.
4. Close the app (the Quit button / closing the status window in GUI mode, or Ctrl+C in console mode) and confirm the process actually exits (check Task Manager / Activity Monitor / `ps`) rather than leaving an orphaned server running.
5. Double-click the executable a second time while the first instance is still running, and confirm it opens a new browser tab against the *existing* instance rather than failing or starting a second server on a different port silently.

## Troubleshooting

**Build fails with a `ModuleNotFoundError` for something at runtime, despite building successfully.** PyInstaller's static import scanner can miss dynamically-loaded submodules, particularly in scipy/sympy. Add the missing module's dotted name to the `hiddenimports` list in `ims_explorer.spec` and rebuild.

**The windowed build shows nothing at all on launch (no splash, no browser, no error).** Rebuild with `console=True` in `ims_explorer.spec` (temporarily) to see console output and tracebacks, since `console=False` windowed builds swallow stderr by default. This is the fastest way to diagnose the untested GUI path from the table above.

**`explorer.html` returns a 404, or the app opens to a blank/error page.** The `datas` entry in `ims_explorer.spec` bundles `ims_platform/server/static/`; confirm the built `dist/IMS Platform Explorer/_internal/ims_platform/server/static/explorer.html` (path may vary slightly by PyInstaller version) actually exists after building. `server/app.py`'s `_static_dir()` function is what resolves this path at runtime via `sys._MEIPASS`; if PyInstaller's internal layout differs from what that function assumes, that is the first place to adjust.

**macOS: "app is damaged and can't be opened" / Gatekeeper blocks it.** Expected for an unsigned build. For local testing: System Settings -> Privacy & Security -> allow it explicitly after the first blocked attempt, or run `xattr -cr "dist/IMS Platform Explorer"` before launching. For distribution to others, the build needs an Apple Developer ID and `codesign`/notarization, which is outside this document's scope.

**Windows Defender / antivirus flags the executable.** Common and expected for unsigned PyInstaller executables (the bootloader pattern is a known, if usually harmless, false-positive trigger). Code-signing with a real certificate resolves this for distribution; for local testing, an exclusion is sufficient.
