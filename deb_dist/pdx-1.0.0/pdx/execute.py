import os
from ol_predict import output_counter
def getFileName():
    return fileName

def Xqtr(fileName, ext):
    if ext == 'c':
        #print("This is c")
        os.system("gcc " +os.path.join(os.getcwd(),fileName) + ".c")
        os.system('script -c "./a.out" -q output.txt')
        noLines = output_counter()
        return noLines
    elif ext == 'py':
        print("This is Python")
       	cmd="python " + fileName + ".py"
	os.system('script -c "'+cmd+'" -q output.txt')
        noLines = output_counter()
        return noLines
    elif ext == 'java':
	os.system("java "+fileName+".java")
	cmd="javac "+fileName+".class"
	os.system('script -c "'+cmd+'" -q output.txt')
        noLines = output_counter()
        return noLines
    elif ext == 'cpp':
        os.system("g++ " +os.path.join(os.getcwd(),fileName) + ".c")
        os.system('script -c "./a.out" -q output.txt')
        noLines = output_counter()
        return noLines
    else:
        print("ProDriverX does not support that Language currently")
	quit()


