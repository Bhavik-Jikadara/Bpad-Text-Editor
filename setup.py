from cx_freeze import setup,executables
import os
import sys
base = None

if sys.platform == 'win64':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Bhavik Jikadara\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Bhavik Jikadara\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_freeze.Executable("Bpad.py", base=base, icon="icon.ico")]


cx_freeze.setup(
    name = "Bpad Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
