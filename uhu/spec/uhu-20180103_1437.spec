# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\nehart\\Development\\bla1\\uhu\\__init__.py'],
             pathex=['C:\\Users\\nehart\\Development\\bla1\\uhu/spec'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='uhu-20180103_1437',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
