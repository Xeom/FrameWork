import pygame
import time

import Objects
import Run

class Manager:
    TargetTPS = 120
    
    def __init__(self):
        pygame.init()

        self.Children = []

        self.TPS      = pygame.time.Clock()
        self.FPS      = pygame.time.Clock()

        self.Screen   = None

        self.Vars     = {"Game":   self, 
                         "pygame": pygame}

        Objects.LoadScripts("/Objects/", self.Vars)
        self.ReadyToRun = self.Vars.copy()
        self.Events = Run.LoadScripts("/Tests/", self.Vars)

        while True:
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
            if   event.type == pygame.KEYDOWN:
                self.Events["KeyDown"].Exec(event)
                self.Events["KeyPress"].Exec(event)
                
            elif event.type == pygame.KEYUP:
                self.Events["KeyUp"].Exec(event)
Manager()    
    
