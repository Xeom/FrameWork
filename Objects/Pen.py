class Pen(object):
    def __init__(self, parent):
        self.Parent = parent
        
        self.X      = 0
        self.Y      = 0
        
        self.Colour = (0, 0, 0)
        self.Width  = 1
        self.Draw   = True
        
    def GetPos(self):
        return self.X, self.Y
    
    def Down(self):
        self.Draw = True
        
    def Up(self):
        self.Draw = False
        
    def Stamp(self):
        self.Parent.fill(self.Colour, (self.X - self.Width//2,
                                       self.Y - self.Width//2,
                                       self.Width,
                                       self.Width))
        
        
    def Line(self, prePos):
        if self.Draw:
            pygame.draw.line(self.Parent, self.Colour, prePos, self.GetPos(), self.Width)
        
    def Move(self, x, y):
        prePos  = (self.X, self.Y)
        
        self.X += x
        self.Y += y
        
        self.Line(prePos)
        
    def SetPos(self, x, y):
        prePos  = (self.X, self.Y)
        
        self.X  = x
        self.Y  = y
        
        self.Line(prePos)
        
    def SetColour(self, colour):
        self.Colour = GetColour(colour)
        
    def SetWidth(self, width):
        self.Width = width
