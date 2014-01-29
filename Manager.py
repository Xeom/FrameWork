print("Importing pygame")
import pygame

print("Importing time")
import time

print("Importing Objects")
import Objects

print("Importing Run")
import Run

class Manager:
    TargetTPS = 60
    
    def __init__(self):
        self.Vars     = {"Game":   self, 
                         "pygame": pygame}
                         
        Objects.LoadScripts("/Objects/", self.Vars)
        self.OrigVars = self.Vars.copy()
        
        print("Initiating pygame")
        pygame.init()
        print("... done")

        self.Running = True
        self.Colour = (0xFF, 0xFF, 0xFF)
        self.Children = []

        self.TPS      = pygame.time.Clock()
        self.FPS      = pygame.time.Clock()

        self.Screen   = None
        
        self.Vars = self.OrigVars.copy()
        
        self.Events = Run.LoadScripts("/Tests/", self.Vars)

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
                self.Events["MouseMove"].Exec(MousePos      = event.pos,
                                              MouseRel      = event.rel,
                                              MouseButtons  = event.buttons)

            elif event.type == pygame.KEYDOWN:
                self.Events["KeyDown"].Exec(Unicode=event.unicode,
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

Manager()

    
