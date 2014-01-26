import os

def Load(file, variables):
    try:
        exec(compile(open(file).read(), file, "exec"), variables)

    except Exception as E:
        print("Error loading "+file+": "+str(E))

def LoadScripts(path, variables):
    cwd     = os.getcwd()+"/Objects/"

    fileList = [cwd+p for p in os.listdir(cwd)\
                if p.endswith(".py") and not p.startswith("_")]

    try:
        dependencies = open(cwd+"Dependencies.txt").readlines()

    except Exception as e:
        print("Objects/Dependencies.txt not found."+str(e))
        dependencies = ''

    for file in (cwd+p.strip() for p in dependencies):
        if file in fileList:
            fileList.remove(file)
        Load(file, variables)

    for file in fileList:
        Load(file, variables)