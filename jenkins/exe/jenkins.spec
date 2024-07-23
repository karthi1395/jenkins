# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['..\\manage.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['django.contrib.admin.apps', 'django.contrib.auth.apps', 'django.contrib.contenttypes.apps', 'django.contrib.sessions.apps', 'django.contrib.messages.apps', 'django.contrib.staticfiles.apps', 'django.contrib.messages.middleware', 'django.contrib.sessions.middleware', 'django.contrib.sessions.serializers', 'django.template.loaders', 'django.contrib.auth.context_processors', 'django.contrib.messages.context_processors'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='jenkins',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='jenkins',
)
