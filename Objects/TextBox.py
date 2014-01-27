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
        if isinstance(colour, str):
            self.Colour = list((int(colour[x:x+2], 16)\
                                 for x in range(0, len(colour), 2)))

        elif isinstance(colour, int):
            for x in range(0, 3, -1):
                print(x)
                print(colour)
                self.Colour[x] = colour & 0xFF
                colour >>= 8
            print(self.Colour)
                
        else:
            self.Colour = colour

    def UpdateFont(self):
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
        
