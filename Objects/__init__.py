import os

def Load(file, variables):
    print("Loading "+file)
    try:
        exec(compile(open(file).read(), file, "exec"), variables)

    except Exception as E:
        print("Error loading "+file+": "+str(E))

def LoadScripts(path, variables):
    cwd     = os.getcwd()+path

    fileList = [cwd+p for p in os.listdir(cwd) if p.endswith(".py")]

    try:
        dependencies = open(cwd+"Dependencies.txt").readlines()

    except Exception as e:
        print("Objects/Dependencies.txt not found."+str(e))
        dependencies = ''

    for file in (cwd+p.strip() for p in dependencies):
        if file in fileList:
            fileList.remove(file)
        if file[0] != '!':
            Load(file, variables)

    for file in fileList:
        Load(file, variables)
