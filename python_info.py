#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import struct, os

# decoration
print(stylize("\n---- | Python information | ----\n", fg("red")))

# function
def py_shell_executing_mode():
    return struct.calcsize("P") * 8

mode = py_shell_executing_mode()

# output
os.system("python -V")
os.system("python3 -V")
print(f"Shell executing mode: {mode} bit\n")
