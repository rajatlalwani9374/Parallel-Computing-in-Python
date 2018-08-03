import os
import sys

program = "python"
print ("process calling")
argument = ["calledprocess.py"]
os.execvp(program, (program,) +tuple(argument))
print("bye")
