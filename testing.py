import os
import pwd
#for i in range(0,50):
#	os.system("xdotool key Control_L+Shift_L+Up")
os.chdir("/home")
path_str=os.path.join(os.getcwd(),pwd.getpwuid(os.getuid())[0])
print(path_str)
path_str=path_str+"/Screenshots"
print(path_str)
if(os.path.exists(path_str)):
	print("It exits")
else:
	os.mkdir(path_str)
def givePath():
	return os.path
