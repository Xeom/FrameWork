print("Importing pygame")
import pygame

print("Importing time")
import time

print("Importing Objects")
import Objects

print("Importing Run")
import Run

import os

class Manager:
    TargetTPS = 120
    
    def __init__(self, ObjectPath, GamePath):
        cwd = os.getcwd()
        
        self.ObjectPath = cwd+ObjectPath
        self.GamePath   = cwd+GamePath
        
        self.Vars     = {"Game":   self, 
                         "pygame": pygame}
                         
        Objects.LoadScripts(self.ObjectPath, self.Vars)

        print("Initiating pygame")
        pygame.init()
        print("... done")

        self.Running = True

        self.Children = []

        self.TPS      = pygame.time.Clock()
        self.FPS      = pygame.time.Clock()

        self.Screen   = None
        
        self.Events = Run.LoadScripts(self.GamePath, self.Vars)

        while self.Running:
            self.Tick()

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
        self.Children.append(new)

        return new
        
    def ClearScreen(self):
        self.FillScreen(0xFF, 0xFF, 0xFF)

    def FillScreen(self, R, G, B):
        self.CheckScreen()
        self.Screen.fill((R, G, B))

    def Tick(self):
        self.TPS.tick(self.TargetTPS)
        
        self.Events["Forever"].Exec()
        
        for event in pygame.event.get():
            if    event.type == pygame.MOUSEMOTION:
                self.Events["MouseMove"].Exec(MousePos      = event.pos,
                                              MouseRel      = event.rel,
                                              MouseButtons  = event.buttons)

            elif event.type == pygame.KEYDOWN:
                self.Events["KeyDown"].Exec(Key=event.key,
                                            Unicode=event.unicode,
                                            Mod=event.mod)
                
                self.Events["KeyPress"].Exec(Unicode=event.unicode)
                
            elif event.type == pygame.KEYUP:
                self.Events["KeyUp"].Exec(Key=event.key,
                                          Mod=event.mod)


            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.Events["MouseDown"].Exec(MousePos = event.pos,
                                              MouseButton = event.button)

            elif event.type == pygame.MOUSEBUTTONUP:
                self.Events["MouseUp"].Exec(MousePos = event.pos,
                                            MouseButton = event.button)
            



            elif event.type == pygame.QUIT:
                self.Events["Quit"].Exec()
                self.Running = False
                pygame.quit()

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

Manager()
    
