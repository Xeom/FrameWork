import os
import pygame

class Event(object):
    def __init__(self, API):
        self.Events = []
        self.API = API

class KeyDown:
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

    def Exec(self, event):
        self.API["Modifiers"] = event.mod
        self.RunCode(event)
        del self.API["Modifiers"]

    def RunCode(self, event):
        name = pygame.key.name(event.key)
        code = self.Events.get(name)

        if code:
            for compiled in code:
                print(compiled)
                exec(compiled, self.API)

        code = self.Events.get("any")

        if code:
            for compiled in code:
                exec(compiled, self.API)

class Forever(Event):
    def New(self, code, head):
        self.Events.append(compile(code, "<string>", "exec"))

    def Exec(self):
        for compiled in self.Events:
            exec(compiled, self.API)

class KeyUp(KeyDown):
    def Exec(self, event):
        self.RunCode(event)

class MouseMove(Event):pass

def LoadScripts(path, API):
    Events = {
        "MouseMove" : MouseMove(API),
        "Forever"   : Forever(API),
        "KeyDown"   : KeyDown(API),
        "KeyUp"     : KeyUp(API)}
    
    scriptPath = os.getcwd()+"/Tests/"

    for path in os.listdir(scriptPath):
        fullPath = scriptPath+path
        raw = open(fullPath).read()
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
