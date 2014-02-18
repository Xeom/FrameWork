class SubSurface(object):
    """A basic image to be rendered onto another,
    this may be the screen.

    parent is the surface to render onto.
    cache=True is to speed up loading multiple image files."""
    
    def __init__(self, parent, cache=False):
        self.Parent    = parent
        self.X, self.Y = 0, 0
        self.SetImage(UnknownImage)

        if cache:
            self.Cache = {}

        else:
            self.Cache = None

    def GetPos(self):
        """Get the position of the top left corner
        of this surface relative to its parent."""
        
        return self.X, self.Y

    def GetCenter(self):
        rect = self.GetRect()
        return rect[0]+rect[2]/2, rect[1]+rect[3]/2

    def GetRect(self):
        """Gets the rectangle that the image takes up.
        
        Returns in the format (X, Y, Width, Height)."""
        
        return self.GetPos()+self.Image.get_size()

    def SetImagePath(self, path):
        """Load and use an image in a directory.

        path is the path to load the image from."""
        
        try:
            if self.Cache != None:
                if path in self.Cache:
                    image = self.Cache[path]

                else:
                    image = pygame.image.load(path)
                    self.Cache[path] = image
            else:
                image = pygame.image.load(path)

        except:
            print(path+" is invalid image")
            
        else:
            self.SetImage(image.convert_alpha())

    def SetImage(self, image):
        """Sets the image of this surface.

        image is a pygame.Surface object."""
        
        self.Image = image
        self.UpdateMask()

    def Blit(self):
        """Renders this surface onto its parent."""
        
        self.Parent.blit(self.Image, self.GetPos())

    def IsColliding(self, other):
        """Checks if the surface is colliding with another.
        Returns None if it is not colliding, the coordinates
        of the first collision if it is.

        other is another SubSurface object to check collision with, or a position"""
     
        if isinstance(other, SubSurface):
            pos    = other.GetPos()
            ownpos = self. GetPos()
            offset = (int(pos[0]-ownpos[0]), int(pos[1]-ownpos[1]))
            
            return bool(self.Mask.overlap(other.Mask, offset))
            
        else:
            if len(other)== 2:
                rect = self.GetRect()
                if IsIn(other, rect):
                    return bool(self.Mask.get_at((int(other[0]-rect[0]),
                                                  int(other[1]-rect[1]))))
                
            elif len(other) == 4:
                pass


    def SetPos(self, x, y):
        """Set this surfaces location on its parent.

        x is the x coordinate to set.
        y is the y coordinate to set."""
        
        self.X = x
        self.Y = y

    def Set(self, x, y, colour):
        """Set this image to a blank rectangle of any colour.

        x is the width of the rectangle.
        y is the height of the rectangle.
        colour is the colour to use."""
        
        self.SetImage(pygame.Surface((x, y), pygame.SRCALPHA))
        self.Fill(colour)

    def Fill(self, colour):
        """Fill this surfake with a solid colour.

        colour is the colour to use."""
        
        self.Image.fill(GetColour(colour))
        self.UpdateMask()

    def UpdateMask(self):
        """Update the collision mask of this surface."""
        
        self.Mask = pygame.mask.from_surface(self.Image)

