import random
import os
from pdx.scr_final import takeSS
def scroa(appname):
    cmd="xdotool search --class --onlyvisible '"+appname+"'"
    windowid=os.popen(cmd)
    cmd2="xdotool windowactivate "+windowid.read().strip()
    os.system(cmd2)
    photoname="Testing_"+str(random.randint(0,25))
    takeSS(photoname)
    # Call the function to call the 
