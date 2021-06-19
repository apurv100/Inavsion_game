# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['game.py'],
             pathex=['C:\\Users\\apurva\\Desktop\\work'],
             binaries=[],
             datas=[('asset/laser.wav','asset'),('asset/background.wav','asset'),('asset/explosion.wav','asset'),('asset/background.png','asset'),('asset/alien.png','asset'),('asset/player.png','asset'),('asset/ufo.png','asset'),('asset/bullet.png','asset')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
