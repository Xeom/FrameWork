import os
import pygame

class Event(object):
    def __init__(self, API):
        self.Events = []
        self.API = API

    def New(self, code, head):
        self.Events.append(compile(code, "<string>", "exec"))

    def Exec(self, **kwargs):
        self.API.update(kwargs)
        self.RunCode()

    def RunCode(self):
        for compiled in self.Events:
            exec(compiled, self.API)

class KeyEvent(Event):
    def __init__(self, API):
        self.Events = {}
        self.API = API
        
    def New(self, code, head):
        if head:
            key = head[1].lower()

        else:
            key = "any"
                
        if key not in self.Events:
            self.Events[key] = []

        self.Events[key].append(compile(code, "<string>", "exec"))

    def RunCode(self, ):
        name = pygame.key.name(self.API["Key"])
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
    
    scriptPath = os.getcwd()+path

    try:
        files = os.listdir(scriptPath)

    except Exception as E:
        print("Error reading "+scriptPath+": "+str(E))

    for raw in (open(scriptPath+p).read()\
                 for p in os.listdir(scriptPath)\
                 if p.endswith(".py")):

        sections = raw.split("##")[1:]

        for script in sections:
            lineEnd = script.find("\n")
            head = script[:lineEnd].split()

            if head:
                event = Events.get(head[0])
                if event:
                    event.New(script[lineEnd:], head)

                else:
                    Exception(head[0]+" is not a valid event.")

            else:
                exec(compile(script, "<string>", "exec"), API)

    return Events
