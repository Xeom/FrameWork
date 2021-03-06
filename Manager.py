print("Importing pygame")
import pygame

print("Importing time")
import time

print("Importing Objects")
import Objects

print("Importing Run")
import Run

import os

class EventContainer:
    """Contains all data for instances at runtime
    a Manager controls these variables.

    The variables controllec here are as follows:
    MousePos - A two long iterable containing the coordinates of the mouse.
    MouseRel - A two long iterable containing the movement of the mouse.
    Unicode - The unicode of the last key typed
    Mod - The modifiers used on the last key typed
    KeyDown - The last key pressed down
    KeyUp - The last key released
    KeysDown - A list of all keys pressed
    MouseButtons - A list of all mouse buttons pressed
    """

    def __init__(self):
        self.MousePos     = [0, 0]
        self.MouseRel     = [0, 0]
        self.Unicode      = ''
        self.Mod          = ()
        self.KeyDown      = ''
        self.KeyUp        = ''
        self.KeysDown     = []
        self.MouseButtons = []

class Manager:
    """Interfaces with pygame, manages events,and calls scripts as needed.

    ObjectPath is the path of the lib directory to load all files from.
    GamePath is the path from which to load the user scripts.
    TPS is the target number of ticks per second."""
    
    def __init__(self, ObjectPath, GamePath):
        self.TargetTPS = 60
        
        cwd = os.getcwd()
        
        self.ObjectPath = cwd+ObjectPath
        self.GamePath   = cwd+GamePath
        
        self.EventVars  = EventContainer()
        
        self.Vars     = {"Game":   self, 
                         "pygame": pygame,
                         "Event": self.EventVars}
                         
        print("Initiating pygame")
        pygame.init()
        pygame.display.init()
        print("... done")

        Objects.LoadScripts(self.ObjectPath, self.Vars)

        self.Running = True
        self.Colour = (0xFF, 0xFF, 0xFF)
        self.Children = []

        self.TPS      = pygame.time.Clock()
        self.FPS      = pygame.time.Clock()

        self.Screen   = None
        
        self.Events = Run.LoadScripts(self.GamePath, self.Vars)

        while self.Running:
            self.Tick()

        pygame.quit()

    def Update(self):
        """Updates the screen."""
        self.Screen.fill(self.Colour)

        for Child in self.Children:
            Child.Blit()

        self.Screen.blit(self.Canvas, (0, 0))

        pygame.display.flip()

        self.FPS.tick()

    def GetFPS(self):
        """Returns the number of times the screen is updated per second."""

        return self.FPS.get_fps()

    def GetTPS(self):
        """Returns the number of ticks per second."""
        
        return self.TPS.get_fps()
    
    def CreateScreen(self, x, y, resizable=False):
        """Initiates a new display window.

        x is the width of the window to be created.
        y is the height of the window to be created."""
        
        flags = 0
        if resizable:
            flags |= pygame.RESIZABLE
        
        self.Screen = pygame.display.set_mode((x, y))
        self.Canvas = pygame.Surface(self.Screen.get_size(), pygame.SRCALPHA)
        
        self.ClearScreen()

    def CheckScreen(self):
        """Used internally to check that a screen exists."""
        
        if not self.Screen:
            print("Please call 'CreateScreen(X, Y)' before '"+\
                  name+"' - Starting with (600, 600) screen")

            self.CreateScreen(600, 600)

    def New(self, cls, **kwargs):
        """Adds a new SubSurface to the screen.

        cls is the class to create an instance of.
        any extra args of keyword args are given to the class."""
        
        self.CheckScreen()
        
        if issubclass(cls, self.Vars["CanvasObject"]):
            new = cls(self.Canvas, **kwargs)
            
        else:
            new = cls(self.Screen, **kwargs)
            self.Children.append(new)

        return new
        
    def ClearScreen(self):
        """Clears the screen. Never could have guessed."""
        self.Screen.fill(self.Colour)

    def ClearCanvas(self):
        """Clears the canvas."""
        self.Canvas.fill((0, 0, 0, 0))

    def Tick(self):
        """Handles all events, and runs all appropriate scripts."""
        
        self.TPS.tick(self.TargetTPS)
        
        self.Events["Forever"].Exec()
        
        for event in pygame.event.get():
            if    event.type == pygame.MOUSEMOTION:
                self.EventVars.MouseRel = event.rel
                self.EventVars.MousePos = event.pos
                
                self.Events["MouseMove"].Exec()

            elif event.type == pygame.KEYDOWN:
                name = pygame.key.name(event.key)
                
                self.EventVars.KeyDown = event.key
                self.EventVars.Unicode = event.unicode
                self.EventVars.Mod     = event.mod
                
                if name not in self.EventVars.KeysDown:
                    self.EventVars.KeysDown.append(name)
                
                self.Events["KeyDown"].Exec(name)
                self.Events["KeyPress"].Exec()
                
            elif event.type == pygame.KEYUP:
                name = pygame.key.name(event.key)
                
                self.EventVars.KeyUp = event.key
                
                if name in self.EventVars.KeysDown:
                    self.EventVars.KeysDown.remove(name)
                
                self.Events["KeyUp"].Exec(name)


            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.EventVars.MousePos    = event.pos
                self.EventVars.MouseButton = event.button
                
                if event.button not in self.EventVars.MouseButtons:
                    self.EventVars.MouseButtons.append(event.button)
                
                self.Events["MouseDown"].Exec()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.EventVars.MousePos    = event.pos
                self.EventVars.MouseButton = event.button
                
                if event.button in self.EventVars.MouseButtons:
                    self.EventVars.MouseButtons.remove(event.button)
                
                self.Events["MouseUp"].Exec()
            
            elif event.type == pygame.QUIT:
                self.Events["Quit"].Exec()
                self.Running = False

    def GetSize(self):
        """Get the size of the display surface"""
        
        return self.Screen.get_size()
        
"""    
QUIT             none
ACTIVEEVENT      gain, state
KEYDOWN          unicode, key, mod
KEYUP            key, mod
MOUSEMOTION      pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
JOYAXISMOTION    joy, axis, value
JOYBALLMOTION    joy, ball, rel
JOYHATMOTION     joy, hat, value
JOYBUTTONUP      joy, button
JOYBUTTONDOWN    joy, button
VIDEORESIZE      size, w, h
VIDEOEXPOSE      none
USEREVENT        code
"""
    
