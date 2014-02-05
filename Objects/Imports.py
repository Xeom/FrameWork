import math as Math
from random import randint as Rand

def GetColour(colour):
    """Convert a colour from either the 0xRRGGBB, "RRGGBB" or "RRGGBBAA" to a tuple.

    colour is the object to convert"""
    
    if isinstance(colour, str):
        return list((int(colour[x:x+2], 16)\
                     for x in range(0, len(colour), 2)))

    elif isinstance(colour, int):
        col = [0, 0, 0]

        for x in range(0, 3)[::-1]:
            col[x] = colour & 0xFF
            colour >>= 8

        return col
            
    else:
        return colour

def IsIn(pos, rect):
    """Reterns if a position is in a rect.
    
    pos is the position to check.
    rect is the rect to check if the pos is in."""
    
    return pos[0] >= rect[0] and\
           pos[1] >= rect[1] and\
           pos[0] <= rect[0]+rect[2] and\
           pos[1] <= rect[1]+rect[3]
