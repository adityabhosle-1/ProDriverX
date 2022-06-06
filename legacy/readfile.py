import os
def giveFile():
    files=os.listdir("files") # returns list
    print(files[0])
    return files[0]
def readFile():
    filename=giveFile()
    path=os.path.abspath(filename)
    return path