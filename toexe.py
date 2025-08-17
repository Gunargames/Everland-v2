import cx_Freeze
from cx_Freeze import *
import sys

sys.argv.append("build")

setup(
    name='Everland',
    options={"build_exe": {"packages": ['ursina', 'pygame', 'math', 'random']}},
    executables=[
        Executable(
            "main1234.py"
        )
    ]
)