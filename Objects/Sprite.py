class Sprite(SubSurface):
    def __init__(self, *args):
        SubSurface.__init__(self, *args)
        self.Angle = 0
        self.ModX  = 0
        self.ModY  = 0

    def Blit(self):
        self.Parent.blit(self.Image, (self.X+self.ModX
                                      , self.Y+self.ModY))

    def SetImage(self, image):
        self.Orig  = image
        self.Image = image.copy()
        self.Size  = image.get_size()

    def Move(self, x, y):
        self.X += x
        self.Y += y

    def Forward(self, distance):
        self.X += distance*sin(self.Angle)
        self.Y += distance*cos(self.Angle)
        pass

    def Turn(self, amount):
        self.Angle -= amount
        self.Angle %= 360
        self.Image  = pygame.transform.rotate(self.Orig, self.Angle)
        newSize     = self.Image.get_size()
        self.ModX   = -(newSize[0]-self.Size[0])/2
        self.ModY   = -(newSize[1]-self.Size[1])/2
