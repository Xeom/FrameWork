class Sprite(SubSurface):
    def __init__(self, *args):
        SubSurface.__init__(self, *args)
        self.Angle = 0
        self.ModX  = 0
        self.ModY  = 0
        self.UpdateMask()       

    def GetPos(self):
        return self.X+self.ModX, self.Y+self.ModY

    def SetImage(self, image):
        self.Orig  = image
        self.Image = image.copy()
        self.Size  = image.get_size()

        self.UpdateMask()

    def IsColliding(self, other):
        pos    = other.GetPos()
        offset = (int(pos[0]-self.X), int(pos[1]-self.Y))
        return self.Mask.overlap(other.Mask, offset)

    def Move(self, x, y):
        self.X += x
        self.Y += y

    def Forward(self, distance):
        self.Move(distance*math.sin(math.radians(self.Angle)),
                  distance*math.cos(math.radians(self.Angle)))

    def Fill(self, colour):
        self.Orig.fill(GetColour(colour))

        if self.Angle:
            self.Turn()
        else:
            self.Image = self.Orig.copy()

    def Turn(self, amount):
        self.Angle -= amount
        self.Angle %= 360

        self.Image = pygame.transform.rotate(self.Orig, self.Angle)
        self.UpdateMask()
        
        newSize     = self.Image.get_size()
        self.ModX   = -(newSize[0]-self.Size[0])/2
        self.ModY   = -(newSize[1]-self.Size[1])/2
