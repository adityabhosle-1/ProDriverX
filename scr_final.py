import os
import math
from execute import Xqtr
import random
def takeSS(filename):
	cmd='gnome-screenshot -w -d 5 -f ' + filename + '.png' 
	os.system(cmd)
	cmd2="mv "+ filename+".png "+"~/Screenshots/"+filename+".png" 
	os.system(cmd2)

#from testing import givePath
# RcmdF = os.popen(cmdF)
# terFont =int(RcmdF.read().split(" ")[1].replace("'",""))
#print("Phont: "+terFont)

# RcmdH = os.popen(cmdH)
# terH = int(RcmdH.read().split("\n")[8].strip().split(" ")[1])
#print("hit: " + terH)
def beginSS(filename,ext):
	# TermLines: Number of lines in the current terminal window (ViewFrame)
	TermLines = int(os.popen("tput lines").read())
	#print(TermLines)

	# exLines: Number of lines in the code output, to be fetched from the exec module

	os.system("echo -e '\\0033\\0143'")
	exLines = int(Xqtr(filename,ext))
	ratio = float(exLines)/TermLines
	print("the ratio is "+str(ratio))

	if ratio <= 1:
		noSS = 1
		for i in range (1, exLines + 1+5):
			os.system("xdotool key Control_L+Shift_L+Up")
	   	photoname="Testing_"+str(random.randint(0,25))
		takeSS(photoname)
	else:
		noSS = math.ceil(ratio)
		print("This is no of sscrenshtos")
		print(noSS)
		# go up * exlines
		for i in range (1, exLines + 1):
			os.system("xdotool key Control_L+Shift_L+Up")
		photoname="Tesiting"+str(random.randint(0,255))
		takeSS(photoname)
		while(noSS>1):
			# go down * tLines
			for i in range (1, TermLines + 1):
				os.system("xdotool key Control_L+Shift_L+Down")
			# Screenshot
	   		photoname="Testing_"+str(random.randint(0,25))
			takeSS(photoname)
			# Updating dummy
			noSS -= 1
		#if(dummy < 24):
			#for i in range (1, dummy + 3):
		#os.system("xdotool key Control_L+Shift_L+Down")
			# Screenshot
   			#photoname="Testing_"+str(random.randint(0,25))
			#takeSS(photoname)
			# Updating dummy
			#dummy -= TermLines


# if exLines > TermLines:
# 	print("THIS IS UNDER DEV")
# 	# Multiple ScreenShot shit
# else:
# 	#single screenshot only
# 	os.system("clear")
# 	print("hello1")
# 	for i in range(1, 31):
#                 print("hello")
# 	os.system("gnome-screenshot -w -d 5")
