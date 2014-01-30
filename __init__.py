import Manager
import traceback

LIBS = "/Objects/"

GAME = input("Game directory:")

try:
    Manager.Manager(LIBS, GAME)

except Exception as E:
    print("Error encounted!")
    traceback.print_exc()
    print(str(E))
    
