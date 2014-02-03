import Manager
import traceback

LIBS = "/Objects/"
TPS  = 0

GAME = input("Game directory:")

try:
    Manager.Manager(LIBS, GAME, TPS)

except Exception as E:
    print("Error encounted!")
    traceback.print_exc()
    print("This is not a good thing.")
    Manager.pygame.quit()
    input("Press enter to exit...")

