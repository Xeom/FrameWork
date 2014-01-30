pygame.font.init()

class TextBox(SubSurface):
    def __init__(self, parent, font=None, size=10):
        self.Size    = size

        if font:
            self.FontName = font

        else:
            self.FontName = pygame.font.get_default_font()

        self.Text = ''

        self.Colour = [0,0,0]
        
        SubSurface.__init__(self, parent)

        self.UpdateFont()
        self.Write('')

    def SetColour(self, colour):
        self.Colour = GetColour(colour)

    def UpdateFont(self):
        try:
            self.Font = pygame.font.SysFont(self.FontName,
                                            self.Size) 

        except:
            print("Font "+self.FontName+" not found using default")
            self.FontName = pygame.font.get_default_font()
            self.Font = pygame.font.SysFont(self.FontName,
                                            self.Size) 
           

    def SetFontAndSize(self, font, size):
        self.FontName = font
        self.Size     = size
        self.UpdateFont()

    def SetSize(self, size):
        self.Size     = size
        self.UpdateFont()

    def SetFont(self, font):
        self.FontName = font
        self.UpdateFont()

    def SetText(self, text):
        self.Text = text
        self.UpdateImage()
        
    def Write(self, text):     
        self.Text += text
        self.UpdateImage()

    def Delete(self, amount=1):
        self.Text = self.Text[:-amount]
        self.UpdateImage()

    def UpdateImage(self):
        self.Image = self.Font.render(self.Text, False, self.Colour)
        
