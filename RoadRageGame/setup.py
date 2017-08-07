import cx_Freeze
from cx_Freeze import *
import os

os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tk8.6"

cx_Freeze.setup(
    
    name="Road Rage",
    options = {"build_exe": {"packages": ["pygame"], "include_files": ["images/race_car.png", "images/obstacle.png", "images/asphalt.jpg"]}},
    executables = [
        Executable("game.py",


                   )
    
        ]
    
    )
