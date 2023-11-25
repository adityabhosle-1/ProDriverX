import os
from pdx.ol_predict import output_counter

def getFileName():
    return fileName

def Xqtr(fileName, ext):
    if ext == 'c':
        # Compile and execute a C program
        os.system("gcc " + os.path.join(os.getcwd(), fileName) + ".c")
        os.system('script -c "./a.out" -q output.txt')
        noLines = output_counter()
        return noLines
    elif ext == 'py':
        # Execute a Python program
        cmd = "python " + fileName + ".py"
        os.system('script -c "' + cmd + '" -q output.txt')
        noLines = output_counter()
        return noLines
    elif ext == 'java':
        # Compile and execute a Java program
        os.system("java " + fileName + ".java")
        cmd = "javac " + fileName + ".class"
        os.system('script -c "' + cmd + '" -q output.txt')
        noLines = output_counter()
        return noLines
    elif ext == 'cpp':
        # Compile and execute a C++ program
        os.system("g++ " + os.path.join(os.getcwd(), fileName) + ".c")
        os.system('script -c "./a.out" -q output.txt')
        noLines = output_counter()
        return noLines
    else:
        print("ProDriverX does not support that Language currently")
        quit()

# Example usage
if __name__ == "__main__":
    fileName = "your_file_name"  # Replace with your file name
    fileExt = "your_file_extension"  # Replace with your file extension
    result = Xqtr(fileName, fileExt)
    print("Number of lines:", result)

