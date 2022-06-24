import os
from ol_predict import output_counter
# os.system("xdotool key Alt+F10") REMOVE COMMENT BEFORE PUSHING
#cmd = raw_input("command: ")
#spl = cmd.split(" ")
# print(spl[1])
#spl2 = spl[1].split(".")
# print(spl2)
#fileName = spl2[0]
#ext = spl2[1]

#print(fileName)
#print(ext)

def getFileName():
    return fileName

def Xqtr(fileName, ext):
    if ext == 'c':
        #print("This is c")
        os.system("gcc " +os.path.join(os.getcwd(),fileName) + ".c")
        os.system('script -c "./a.out" -q output.txt')
        noLines = output_counter()
        #print("The number of lines in the output is: ")
        return noLines
    elif ext == 'py':
        print("This is Python")
        os.system("python " + fileName + ".py")
        noLines = os.system("python " + fileName + ".py | wc -l")
    elif ext == 'java':
        print("this is java")
    elif ext == 'cpp':
        print("This is C++")
        os.system("g++ {fileName}.cpp")
        os.system("./a.out")
    else:
        print("ProDriverX does not support that Language currently")


