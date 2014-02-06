pygame.font.init()

class TextBox(SubSurface):
    """A SubSurface to contain a line of text.

    parent is the Surface to render onto.
    font is the font to use (system default by default).
    size is the fontsize to use."""
    
    def __init__(self, parent, font=None, size=10, **kwargs):
        self.Size    = size

        if font:
            self.FontName = font

        else:
            self.FontName = pygame.font.get_default_font()

        self.Text = ''

        self.Colour = [0,0,0]
        
        SubSurface.__init__(self, parent, **kwargs)

        self.UpdateFont()
        self.Write('')

    def SetColour(self, colour):
        """Sets the colour of the font.

        colour is the colour to use."""
        self.Colour = GetColour(colour)

    def UpdateFont(self):
        """Used internally to update the font or its size."""
        
        try:
            self.Font = pygame.font.SysFont(self.FontName,
                                            self.Size) 

        except:
            print("Font "+self.FontName+" not found using default")
            self.FontName = pygame.font.get_default_font()
            self.Font = pygame.font.SysFont(self.FontName,
                                            self.Size) 
           

    def SetFontAndSize(self, font, size):
        """Give the textbox a new font and fontsize.

        font is the name of the font to try and use.
        size is the font's size."""
        
        self.FontName = font
        self.Size     = size
        self.UpdateFont()

    def SetSize(self, size):
        """Give the textbox a new size.

        size is the font's size."""
        
        self.Size     = size
        self.UpdateFont()

    def SetFont(self, font):
        """Give the textbox a new font.

        font is the name of the font to try and use."""
        
        self.FontName = font
        self.UpdateFont()

    def SetText(self, text):
        """Sets the text to display in the textbox.

        text is the text to display."""
        
        if isinstance(text, str):
            self.Text = text
            
        else:
            self.Text = str(text)

        self.UpdateImage()
        
    def Write(self, text):
        """Append to the existing text in the textbox.

        text is the text to append."""
        
        if isinstance(text, str):
            self.Text += text
            
        else:
            self.Text += str(text)
            
        self.UpdateImage()

    def Delete(self, amount=1):
        """Remove the final charater(s) from the text.

        amount is how many to delete. This is 1 by default."""
        
        self.Text = self.Text[:-amount]
        self.UpdateImage()

    def UpdateImage(self):
        """Render new text to an image."""
        self.Image = self.Font.render(self.Text, False, self.Colour)
        
