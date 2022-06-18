import os
def scroa(appname):
    cmd="xdotool search --name --onlyvisible'"+appname+"'"
    windowid=os.popen(cmd)
    cmd2="xdotool windowactivate "+windowid.read().strip()
    os.system(cmd2)
    # Call the function to call the 
