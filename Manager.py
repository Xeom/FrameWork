print("Importing pygame")
import pygame

print("Importing time")
import time

print("Importing Objects")
import Objects

print("Importing Run")
import Run

import os

class EventContainer:
    def __init__(self):
        self.MousePos     = None
        self.MouseRel     = None
        self.Unicode      = None
        self.Mod          = None
        self.Key          = None
        self.KeysDown     = []
        self.MouseButtons = []

class Manager:
    def __init__(self, ObjectPath, GamePath, TPS):
        self.TargetTPS = TPS
        
        cwd = os.getcwd()
        
        self.ObjectPath = cwd+ObjectPath
        self.GamePath   = cwd+GamePath
        
        self.EventVars  = EventContainer()
        
        self.Vars     = {"Game":   self, 
                         "pygame": pygame,
                         "Event": self.EventVars}
                         
        
        Objects.LoadScripts(self.ObjectPath, self.Vars)

        print("Initiating pygame")
        pygame.init()
        print("... done")

        self.Running = True
        self.Colour = (0xFF, 0xFF, 0xFF)
        self.Children = []

        self.TPS      = pygame.time.Clock()
        self.FPS      = pygame.time.Clock()

        self.Screen   = None
        
        self.Events = Run.LoadScripts(self.GamePath, self.Vars)

        while self.Running:
            self.Tick()

        pygame.quit()

    def Draw(self):
        for Child in self.Children:
            Child.Blit()

    def Update(self):
        self.FPS.tick()
        pygame.display.flip()
        self.ClearScreen()

    def GetFPS(self):
        return self.FPS.get_fps()

    def GetTPS(self):
        return self.TPS.get_fps()
    
    def CreateScreen(self, X, Y):
        self.Screen = pygame.display.set_mode((X, Y))
        self.ClearScreen()

    def CheckScreen(self):
        if not self.Screen:
            print("Please call 'CreateScreen(X, Y)' before '"+\
                  name+"' - Starting with (600, 600) screen")

            self.CreateScreen(600, 600)

    def New(self, cls, *args, **kwargs):
        self.CheckScreen()
        new = cls(self.Screen, *args, **kwargs)
        self.CheckScreen()
        self.Children.append(new)

        return new
        
    def ClearScreen(self):
        self.FillScreen(*self.Colour)

    def FillScreen(self, R, G, B):
        self.CheckScreen()
        self.Screen.fill((R, G, B))

    def Tick(self):
        self.TPS.tick(self.TargetTPS)
        
        self.Events["Forever"].Exec()
        
        for event in pygame.event.get():
            if    event.type == pygame.MOUSEMOTION:
                self.EventVars.MouseRel = event.rel
                self.EventVars.MousePos = event.pos
                
                self.Events["MouseMove"].Exec()

            elif event.type == pygame.KEYDOWN:
                name = pygame.key.name(event.key)
                
                self.EventVars.Key     = event.key
                self.EventVars.Unicode = event.unicode
                self.EventVars.Mod     = event.mod
                
                if name not in self.EventVars.KeysDown:
                    self.EventVars.KeysDown.append(name)
                
                self.Events["KeyDown"].Exec(name)
                self.Events["KeyPress"].Exec()
                
            elif event.type == pygame.KEYUP:
                name = pygame.key.name(event.key)
                
                self.EventVars.Mod = event.mod
                
                if name in self.EventVars.KeysDown:
                    self.EventVars.KeysDown.remove(name)
                
                self.Events["KeyUp"].Exec(name)


            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.EventVars.MousePos    = event.pos
                self.EventVars.MouseButton = event.button
                
                if event.button not in self.EventVars.MouseButtons:
                    self.EventVars.MouseButtons.append(event.button)
                
                self.Events["MouseDown"].Exec()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.EventVars.MousePos    = event.pos
                self.EventVars.MouseButton = event.button
                
                if event.button in self.EventVars.MouseButtons:
                    self.EventVars.MouseButtons.remove(event.button)
                
                self.Events["MouseUp"].Exec()
            
            elif event.type == pygame.QUIT:
                self.Events["Quit"].Exec()
                self.Running = False
"""    
QUIT             none
ACTIVEEVENT      gain, state
KEYDOWN          unicode, key, mod
KEYUP            key, mod
MOUSEMOTION      pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
JOYAXISMOTION    joy, axis, value
JOYBALLMOTION    joy, ball, rel
JOYHATMOTION     joy, hat, value
JOYBUTTONUP      joy, button
JOYBUTTONDOWN    joy, button
VIDEORESIZE      size, w, h
VIDEOEXPOSE      none
USEREVENT        code
"""
    
