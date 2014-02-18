class Sprite(SubSurface):
    """A kind of subsurface for moving etc.

    takes the same args as SubSurface."""
    
    def __init__(self, parent, **kwargs):
        SubSurface.__init__(self, parent, **kwargs)
        self.Angle = 0.0
        self.ModX  = 0
        self.ModY  = 0
        self.UpdateMask()       

    def GetPos(self):
        """Get the position of the top left corner
        of this surface relative to its parent."""
        
        return self.X+self.ModX, self.Y+self.ModY

    def SetImage(self, image):
        """Sets the image of this surface.

        image is a pygame.Surface object."""
        
        self.Orig  = image
        self.Image = image.copy()
        self.Size  = image.get_size()

        self.UpdateMask()            

    def Move(self, x, y):
        """Moves this Sprite.

        x is how far to move it horistontally.
        y is how far to move it vertically."""
        
        self.X += x
        self.Y += y

    def Forward(self, distance):
        """Moves this sprite forward in the direction it is facing.

        distance is how far to move it."""
        
        self.Move(distance*Math.sin(Math.radians(self.Angle)),
                  distance*Math.cos(Math.radians(self.Angle)))

    def Fill(self, colour):
        """Fill this surfake with a solid colour.

        colour is the colour to use."""
        
        self.Orig.fill(GetColour(colour))

        if self.Angle:
            self.Turn(0)
        else:
            self.Image = self.Orig.copy()

    def Turn(self, amount):
        """Rotates the Sprite an amount.

        amount is the angle to rotate it by."""
        
        self.Angle -= amount
        self.Angle %= 360

        self.Image = pygame.transform.rotate(self.Orig, self.Angle)
        self.UpdateMask()
        
        newSize     = self.Image.get_size()
        self.ModX   = -(newSize[0]-self.Size[0])/2
        self.ModY   = -(newSize[1]-self.Size[1])/2
