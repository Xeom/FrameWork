##
CreateScreen(600, 600)
Cat = Sprite(Manager.Screen)
Cat.SetImagePath("Cat.jpg")
Cat.Move(100, 100)
Direction = 1
## Forever
Cat.Turn(Direction)
Manager.ClearScreen()
Cat.Blit()
Manager.Update()
## KeyDown ]
Direction -= 2
## KeyDown [
Direction += 2

