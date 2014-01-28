import math as Math
from random import randint as Rand

def GetColour(colour):
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
