import os

def searchFiles(myString,extension):
    l = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(extension):
                if myString in open(os.path.join(root,file)).read():
                    l.append(file)
    return l
