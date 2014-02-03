class SubSurface(object):
    def __init__(self, parent):
        self.Parent    = parent
        self.X, self.Y = 0, 0
        self.SetImage(pygame.Surface((10, 10), pygame.SRCALPHA))
        self.Image.fill((255, 0, 0))

    def GetPos(self):
        return self.X, self.Y

    def GetRect(self):
        return self.GetPos()+self.Image.get_size()

    def SetImagePath(self, path):
        try:
            image = pygame.image.load(path)

        except:
            print(path+" is invalid image")
            
        else:
            self.SetImage(image.convert_alpha())

    def SetImage(self, Image):
        self.Image = Image
        self.UpdateMask()

    def Blit(self):
        self.Parent.blit(self.Image, self.GetPos())

    def SetPos(self, x, y):
        self.X = x
        self.Y = y

    def Set(self, x, y, colour):
        self.SetImage(pygame.Surface((x, y), pygame.SRCALPHA))
        self.Fill(colour)

    def Fill(self, colour):
        self.Image.fill(GetColour(colour))
        self.UpdateMask()

    def UpdateMask(self):
        self.Mask = pygame.mask.from_surface(self.Image)

