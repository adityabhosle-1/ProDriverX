import os
import math
import random
from pdx.execute import Xqtr

def takeSS(filename):
    cmd = 'gnome-screenshot -w -d 5 -f ' + filename + '.png'
    os.system(cmd)
    cmd2 = "mv " + filename + ".png " + "~/Screenshots/" + filename + ".png"
    os.system(cmd2)

def beginSS(filename, ext):
    # TermLines: Number of lines in the current terminal window (ViewFrame)
    TermLines = int(os.popen("tput lines").read())

    os.system("echo -e '\\0033\\0143'")
    exLines = int(Xqtr(filename, ext))
    ratio = float(exLines) / TermLines

    if ratio <= 1:
        noSS = 1
        for i in range(1, exLines + 1 + 5):
            os.system("xdotool key Control_L+Shift_L+Up")
        photoname = "Testing_" + str(random.randint(0, 25))
        takeSS(photoname)
    else:
        noSS = math.ceil(ratio)
        print("This is no of screenshots")
        print(noSS)
        # go up * exlines
        for i in range(1, exLines + 1):
            os.system("xdotool key Control_L+Shift_L+Up")
        photoname = "Tesiting" + str(random.randint(0, 255))
        takeSS(photoname)
        while noSS > 1:
            # go down * tLines
            for i in range(1, TermLines + 1):
                os.system("xdotool key Control_L+Shift_L+Down")
            # Screenshot
            photoname = "Testing_" + str(random.randint(0, 25))
            takeSS(photoname)
            # Updating dummy
            noSS -= 1

if __name__ == "__main__":
    filename = "your_file_name"  # Replace with your filename
    ext = "your_file_extension"  # Replace with your file extension
    beginSS(filename, ext)
