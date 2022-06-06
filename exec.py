import os

cmd = input("command: ")
spl = cmd.split(" ")
# print(spl[1])
spl2 = spl[1].split(".")
# print(spl2)
fileName = spl2[0]
ext = spl2[1]

# print(fileName)
# print(ext)

if ext == 'c':
    #print("This is C")
    os.system(f"gcc {fileName}.c")
    os.system(f"./a.out")
elif ext == 'py':
    #print("This is Python")
    os.system(f"python3 {fileName}.py")
elif ext == 'java':
    #print("This is Java")
elif ext == 'cpp':
    # print("This is C++")
    os.system(f"g++ {fileName}.cpp")
    os.system("./a.out")
else:
    print("Sorry, We do not support that language currently")
