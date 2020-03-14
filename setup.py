from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ['pygame', 'krokovanie', 'zabky', 'files', 'opicky'],
                     "excludes": ['tkinter']}

setup(name = "Hejmat",
    options = {"build_exe": build_exe_options},
    executables = [Executable(script="hejmat.py")]
    )
