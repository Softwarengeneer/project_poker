# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for PokerBot Windows build

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect ultralytics YAML configs and submodules automatically
ultralytics_datas = collect_data_files('ultralytics')
ultralytics_hiddenimports = collect_submodules('ultralytics')

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('models/*.pt', 'models'),
        ('poker.ico', '.'),
    ] + ultralytics_datas,
    hiddenimports=ultralytics_hiddenimports + [
        'torch',
        'torchvision',
        'cv2',
        'fuzzywuzzy',
        'Levenshtein',
        'treys',
        'PIL',
        'PIL._tkinter_finder',
        'pytesseract',
        'numpy',
        'tkinter',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'torch.distributed',
        'torchaudio',
        'matplotlib',
        'scipy',
        'pandas',
        'IPython',
        'jupyter',
        'notebook',
        'tensorboard',
    ],
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
    name='PokerBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='poker.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PokerBot',
)
