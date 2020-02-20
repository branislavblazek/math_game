from cx_Freeze import setup, Executable

setup(name = "Hejmat!",
    options = {"build_exe": {'packages': ['pygame', 'krokovanie', 'zabky', 'files']}},
    executables = [Executable("main.py")])
