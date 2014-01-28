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
        ownpos = self. GetPos()
        offset = (int(pos[0]-ownpos[0]), int(pos[1]-ownpos[1]))
        return self.Mask.overlap(other.Mask, offset)

    def Move(self, x, y):
        self.X += x
        self.Y += y

    def Forward(self, distance):
        self.Move(distance*Math.sin(Math.radians(self.Angle)),
                  distance*Math.cos(Math.radians(self.Angle)))

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
