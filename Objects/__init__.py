import os

def Load(file, variables):
    print("Loading "+file)
    try:
        exec(compile(open(file).read(), file, "exec"), variables)

    except Exception as E:
        print("Error loading "+file+": "+str(E))

def LoadScripts(path, variables):

    fileList = [p for p in os.listdir(path) if p.endswith(".py")]

    try:
        dependencies = open(path+"Dependencies.txt").readlines()

    except Exception as e:
        print(path+"/Dependencies.txt not found."+str(e))
        dependencies = ''

    for file in (p.strip() for p in dependencies\
                 if not p.startswith("#") and p.strip()):
        
        if file in fileList:
            fileList.remove(file)
        
        if file[0] != '!':
            Load(path+file, variables)

        else:
            fileList.remove(file[1:])

    for file in fileList:
        Load(path+file, variables)

    print variables["UnknownImage"]
