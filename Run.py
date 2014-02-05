import os
import pygame
import traceback

def TryExec(code, API):
    try:
        exec(code, API)
                
    except Exception as E:
        print("Error running script: ",str(E))
        traceback.print_exc()
            

class Event:
    """Holds and calls scripts relating to a specific event.

       API is a reference to the dict of global variables."""
    
    def __init__(self, API):
        self.Events = []
        self.API = API

    def New(self, code, head, path):
        """Adds a new piece of code.

        code is the code in a string.
        head is the flag preceding the code.
        path is the path the code came from."""
        
        self.Events.append(compile(code, path, "exec"))
        
    def Exec(self):
        """Executes all code for this event"""
        
        for compiled in self.Events:
            TryExec(compiled, self.API)
            


class KeyEvent:
    def __init__(self, API):
        self.Events = {}
        self.API = API
        
    def New(self, code, head, path):
        """Adds a new piece of code.

        code is the code in a string.
        head is the flag preceding the code.
        path is the path the code came from."""
        
        if head:
            key = head[1].lower()

        else:
            key = "any"
                
        if key not in self.Events:
            self.Events[key] = []

        self.Events[key].append(compile(code, path, "exec"))

    def Exec(self, key):
        """Executes all code for a key.

        key is the key to use code from."""
        
        code = self.Events.get(key)

        if code:
            for compiled in code:
                TryExec(compiled, self.API)
                

        code = self.Events.get("any")

        if code:
            for compiled in code:
                TryExec(compiled, self.API)

def LoadScripts(path, API):
    """Loads all scripts from a directory.

    path is the directory from which to load.
    API is a reference to the dict of global vars."""
    
    Events = {
        "Quit"      : Event(API),
        "Forever"   : Event(API),
        "MouseMove" : Event(API),
        "MouseDown" : Event(API),
        "MouseUp"   : Event(API),
        "KeyPress"  : Event(API),
        "MouseDown" : Event(API),
        "MouseUp"   : Event(API),
        "KeyDown"   : KeyEvent(API),
        "KeyUp"     : KeyEvent(API)}
        
    try:
        files = os.listdir(path)

    except Exception as E:
        print("Error reading "+path+" directory: "+str(E))
        
    for subPath in os.listdir(path):
        filePath = path+subPath
        
        if not filePath.endswith(".py"):
            continue

        print("Loading "+filePath)

        raw = open(filePath).read()

        sections = raw.split("##")[1:]

        for script in sections:
            lineEnd = script.find("\n")
            head = script[:lineEnd].split()

            if head:
                event = Events.get(head[0])
                if event:
                    event.New(script[lineEnd:], head, filePath)

                else:
                    Exception(filePath+": "+head[0]+" is not a valid event.")

            else:
                exec(compile(script, filePath, "exec"), API)

    return Events
