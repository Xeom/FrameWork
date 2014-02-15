import Manager
import traceback
import sys

LIBS = "/Objects/"
def Input(string):
    print(string)
    return sys.stdin.readline()

GAME = Input("Game Directory:")

try:
    Manager.Manager(LIBS, GAME.strip())

except Exception as E:
    print("Error encounted!")
    traceback.print_exc()
    print("This is not a good thing.")
    Manager.pygame.quit()
    Input("Press enter to exit...")

