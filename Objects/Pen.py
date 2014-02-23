class Pen(CanvasObject):
    """An object which moves, and can be used
    to draw lines of different thicknesses and colours.

    parent is the surface to render to."""
    
    def __init__(self, parent):
        self.Parent = parent
        
        self.X      = 0
        self.Y      = 0
        
        self.Colour = (0, 0, 0)
        self.Width  = 1
        self.Draw   = True
        
    def GetPos(self):
        """Get the position of the top left corner
        of this pen relative to its parent."""
        
        return self.X, self.Y
    
    def Down(self):
        """Put the pen down - wherever it moves, it will now draw."""
        
        self.Draw = True
        
    def Up(self):
        """Put the pen up - It will no longer draw."""
        
        self.Draw = False
        
    def Blit(self):
        """Draw a point at the location of this pen."""
        
        self.Parent.fill(self.Colour, (self.X - self.Width//2,
                                       self.Y - self.Width//2,
                                       self.Width,
                                       self.Width))
        
        
    def Line(self, prePos):
        """Used internally to draw a line from this pen
        to another location.

        prePos is the position to end the line at."""
        
        if self.Draw:
            pygame.draw.line(self.Parent, self.Colour, prePos, self.GetPos(), self.Width)
        
    def Move(self, x, y):
        """Move the pen, if the Pen is down,
        this will draw a line connecting its starting
        and finishing locations.

        x is how much to change the x-axis.
        y is how much to change the y-axis."""
        
        prePos  = (self.X, self.Y)
        
        self.X += x
        self.Y += y
        
        self.Line(prePos)
        
    def SetPos(self, x, y):
        """Set the postion of the pen relative to its parent,
        if the pen is down, this will draw a line connecting
        its starting and finishing points.

        x is the x position to set it to.
        y is the y position to set it to."""
        
        prePos  = (self.X, self.Y)
        
        self.X  = x
        self.Y  = y
        
        self.Line(prePos)
        
    def SetColour(self, colour):
        """Make the pen draw in a different colour.

        colour is the new colour to use."""

        self.Colour = GetColour(colour)
        
    def SetWidth(self, width):
        """Set the pen to draw in a different width.

        width is the new width to use."""
        
        self.Width = width
