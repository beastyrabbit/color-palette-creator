# -*- mode: python ; coding: utf-8 -*-
import os

# -*- mode: python ; coding: utf-8 -*-

import os

base_path = os.getcwd()  # Use the current working directory as the base path

from PyInstaller.utils.hooks import collect_data_files

# Collect all data files from sv_ttk
datas = collect_data_files('sv_ttk')

a = Analysis(
    [os.path.join(base_path, 'src', 'color_palette_analysis.py')],
    pathex=[base_path],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='color_palette_analysis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[os.path.join(base_path, 'assets', 'appl.ico')],
)


from PyInstaller.utils.hooks import collect_data_files

# Collect all data files from sv_ttk
datas = collect_data_files('sv_ttk')

a = Analysis(
    [os.path.join(base_path, 'src', 'color_palette_analysis.py')],
    pathex=[base_path],
    binaries=[],
    datas=collect_data_files('sv_ttk'),
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='color_palette_analysis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[os.path.join(base_path, 'assets', 'appl.ico')],
)
