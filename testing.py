import os
import pwd

def dirmake():
	os.chdir("/home")
	path_str=os.path.join(os.getcwd(),pwd.getpwuid(os.getuid())[0])
	print(path_str)
	path_str=path_str+"/Screenshots"
	print(path_str)
	if(os.path.exists(path_str)):
		path_str=path_str
	else:
		os.mkdir(path_str)
	return os.path.abspath(path_str)


def giveFileNames():
	filePaths=[]
	filenames=os.listdir(dirmake())
	for i in range(0,len(filenames)):
		filePaths.append(os.path.join(dirmake(),filenames))
	return filePaths
	


