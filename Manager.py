import pygame
import Run
import time

class Manager:
    def __init__(self):
        pygame.init()
        self.Time   = pygame.time.Clock()
        self.Screen = None
        self.Vars   = {"Update":self.Update,
                       "Manager":self,
                       "CreateScreen":self.CreateScreen,
                       "Surface":SubSurface,
                       "Sprite":Sprite}
        
        self.Events = Run.LoadScripts(None, self.Vars)

        C = 0
        while True:
            self.Time.tick()
            self.Tick()

    def Update(self):
        pygame.display.flip()
    
    def CreateScreen(self, X, Y):
        self.Screen = pygame.display.set_mode((X, Y))
        self.ClearScreen()
        self.Update()

    def CheckScreen(self):
        if not self.Screen:
            print("Please call 'CreateScreen(X, Y)' before '"+\
                  name+"' - Starting with (600, 600) screen")
            self.CreateScreen(600, 600)

    def ClearScreen(self):
        self.FillScreen(0xFF, 0xFF, 0xFF)

    def FillScreen(self, R, G, B):
        self.CheckScreen()
        self.Screen.fill((R, G, B))

    def Tick(self):
        self.Events["Forever"].Exec()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.Events["KeyDown"].Exec(event)
        
class SubSurface(object):
    def __init__(self, parent):
        self.Parent    = parent
        self.X, self.Y = 0, 0

    def SetImagePath(self, path):
        try:
            image = pygame.image.load(path)

        except:
            print(path+" is invalid image")
            self.SetImage(pygame.Surface((10, 10)))
            self.Image.fill((255, 0, 0))

        else:
            self.SetImage(image.convert_alpha())

    def SetImage(self, Image):
        self.Image = Image

    def Blit(self):
        self.Parent.blit(self.Image, (self.X, self.Y))

class Sprite(SubSurface):
    def __init__(self, *args):
        SubSurface.__init__(self, *args)
        self.Angle = 0
        self.ModX  = 0
        self.ModY  = 0

    def Blit(self):
        self.Parent.blit(self.Image, (self.X+self.ModX
                                      , self.Y+self.ModY))

    def SetImage(self, Image):
        self.Orig  = Image
        self.Image = Image.copy()
        self.Size  = Image.get_size()

    def Move(self, X, Y):
        self.X += X
        self.Y += Y

    def Forwards(self, Distance):
        self.X += Distance
        pass#Do some X += sin(angle)*distance things here

    def Turn(self, Amount):
        self.Angle += Amount
        self.Angle %= 360 #Ugh, I really want to use radians here
        self.Image  = pygame.transform.rotate(self.Orig, self.Angle)
        newSize     = self.Image.get_size()
        self.ModX   = -(newSize[0]-self.Size[0])/2
        self.ModY   = -(newSize[1]-self.Size[1])/2

Manager()    
    
