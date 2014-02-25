import math as Math
from random import randint as Rand

UnknownImage = pygame.image.load("Assets/Unknown.png")

Icon = pygame.Surface((32,32))
Icon.fill((255, 255, 255))
Icon.blit(UnknownImage, (0, 0))

pygame.display.set_icon(Icon)

del Icon

class CanvasObject(object):
    """Used to mark an object that writes to the canvas"""
    pass

