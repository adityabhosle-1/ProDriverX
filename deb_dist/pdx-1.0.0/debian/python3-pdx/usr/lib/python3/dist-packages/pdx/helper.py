import os
import pwd
import glob
import time
def dirmake():
	os.chdir("/home")
	path_str=os.path.join(os.getcwd(),pwd.getpwuid(os.getuid())[0])
	path_str=path_str+"/Screenshots"
	if(os.path.exists(path_str)):
		path_str=path_str
	else:
		os.mkdir(path_str)
	return os.path.abspath(path_str)


def giveFileNames():
	filePaths=[]
	filenames=os.listdir(dirmake())
	for i in range(0,len(filenames)):
		filePaths.append(os.path.join(dirmake(),filenames[i]))
	return filePaths


def deletestuff():
	os.system("rm credentials.json")
	os.system("rm token.json")
	directory=dirmake()
	os.chdir(directory)
	files=glob.glob('*')
	for f in files:
	    os.unlink(f)
	
	


def downlaodcreds():
	os.system("curl https://sokumon.000webhostapp.com/credentials.json > credentials.json")
	time.sleep(5)
