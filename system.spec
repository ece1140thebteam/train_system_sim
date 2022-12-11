# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['system.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("C:\\Users\\SHR77\\ece1140\\train_system_sim\\track_model\\track_model_qc\\form.ui", ".\\track_model\\track_model_qc\\."),
        ("C:\\Users\\SHR77\\ece1140\\train_system_sim\\track_model\\TrackModelTestUI\\form.ui", ".\\track_model\\TrackModelTestUI\\."),
        ("C:\\Users\\SHR77\\ece1140\\train_system_sim\\CTCOffice\\DataFiles\\Track Layout & Vehicle Data vF2.xlsx", ".\\CTCOffice\\DataFiles\\."),
        ("C:\\Users\\SHR77\\ece1140\\train_system_sim\\track_model\\track_model_qc\\default_track.csv", ".\\track_model\\track_model_qc\\.")
    ],
    hiddenimports=['PyQt6.sip', 'pandas', 'PyQt6', 'PySide6', 'PySide6.sip', 'openpyxl'],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='system',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
