import math

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

    def SetPosition(self, X, Y):
        self.X = X
        self.Y = Y

def sin(value):
    return math.sin(math.radians(value))

def cos(value):
    return math.cos(math.radians(value))
