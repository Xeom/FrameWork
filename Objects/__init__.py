import os

for file in (for p in os.listdir(os.getcwd) if p.endswith('.py')):
    try:
        exec "from "+file+" import *"

    except Exception as E:
        print("Error loading "+file+" : "+str(E))
