# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\nehart\\Development\\bla1\\jep\\__init__.py'],
             pathex=['C:\\Users\\nehart\\Development\\bla1\\jep/spec'],
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
          name='jep-20180103_1600',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
