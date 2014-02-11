import Manager
import traceback

LIBS = "/Objects/"

GAME = input("Game directory:")

try:
    Manager.Manager(LIBS, GAME)

except Exception as E:
    print("Error encounted!")
    traceback.print_exc()
    print("This is not a good thing.")
    Manager.pygame.quit()
    input("Press enter to exit...")

