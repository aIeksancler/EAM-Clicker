# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_employee_pl.png;.'],
             pathex=[],
             binaries=[],
             datas=[('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_amazonrme.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_processing.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_checkbox_checked.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_prompt_icon.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_yes_en.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_yes_pl.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_yes_de.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_completed_pl.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_completed_en.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_completed_de.png', '.--add-data'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_employee_en.png', '.'), ('C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/target_employee_de.png', '."C:/Users/asynowie/Desktop/EAM-Checklist-Clicker/EAM Checklist Clicker.py')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='target_employee_pl.png;',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\Users\\asynowie\\Desktop\\EAM-Checklist-Clicker\\EAM Checklist Clicker.ico')