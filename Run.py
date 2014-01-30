import os
import pygame

class Event:
    def __init__(self, API):
        self.Events = []
        self.API = API

    def New(self, code, head, path):
        self.Events.append(compile(code, path, "exec"))

    def Exec(self, **kwargs):
        self.API.update(kwargs)
        self.RunCode()

    def RunCode(self):
        for compiled in self.Events:
            exec(compiled, self.API)

class KeyEvent:
    def __init__(self, API):
        self.Events = {}
        self.API = API
        
    def New(self, code, head, path):
        if head:
            key = head[1].lower()

        else:
            key = "any"
                
        if key not in self.Events:
            self.Events[key] = []

        self.Events[key].append(compile(code, path, "exec"))

    def Exec(self, key, **kwargs):
        self.API.update(kwargs)
        self.RunCode(key)

    def RunCode(self, key):
        name = pygame.key.name(key)
        code = self.Events.get(name)

        if code:
            for compiled in code:
                exec(compiled, self.API)

        code = self.Events.get("any")

        if code:
            for compiled in code:
                exec(compiled, self.API)

def LoadScripts(path, API):
    Events = {
        "MouseMove" : Event(API),
        "MouseDown" : Event(API),
        "MouseUp"   : Event(API),
        "Forever"   : Event(API),
        "KeyPress"  : Event(API),
        "Quit"      : Event(API),
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

            print(script)

            if head:
                event = Events.get(head[0])
                if event:
                    event.New(script[lineEnd:], head, filePath)

                else:
                    Exception(filePath+": "+head[0]+" is not a valid event.")

            else:
                exec(compile(script, filePath, "exec"), API)

    return Events
