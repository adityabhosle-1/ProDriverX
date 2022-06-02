
# Importing required module
import os
  
# Using system() method to execute
# shell commands
cmd="gcc trial.c"
result=os.popen(cmd)
cmd2="./a.out"
result2=os.popen(cmd2)
print(result2.read())