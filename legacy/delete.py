import os
import glob
directory='files'
os.chdir(directory)
files=glob.glob('*')
for f in files:
    os.unlink(f)