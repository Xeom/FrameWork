class SubSurface(object):
    """A basic image to be rendered onto another,
    this may be the screen.

    parent is the surface to render onto.
    cache=True is to speed up loading multiple image files."""
    
    def __init__(self, parent, cache=False):
        self.Parent    = parent
        self.X, self.Y = 0, 0
        self.SetImage(pygame.Surface((10, 10), pygame.SRCALPHA))
        self.Image.fill((255, 0, 0))

        if cache:
            self.Cache = {}

        else:
            self.Cache = None

    def GetPos(self):
        """Get the position of the top left corner
        of this surface relative to its parent."""
        
        return self.X, self.Y

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

