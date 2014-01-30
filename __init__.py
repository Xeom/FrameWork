import Manager
import traceback

LIBS = "/Objects/"
TPS  = 60

GAME = input("Game directory:")

try:
    Manager.Manager(LIBS, GAME, TPS)

except Exception as E:
    print("Error encounted!")
    traceback.print_exc()
    print("This is not a good thing.")
    
