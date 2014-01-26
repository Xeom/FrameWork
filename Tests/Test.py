##
Game.CreateScreen(600, 600)

Cat = Game.New(Sprite)
Cat.SetImagePath("Cat.jpg")

Speed = 0
ASpeed = 0

## KeyDown w
Speed += 0.1

## KeyDown a
ASpeed -= 0.1

## KeyDown s
Speed -= 0.1

## KeyDown d
ASpeed += 0.1

## Forever
Cat.Forward(Speed)
Cat.Turn(ASpeed)
Game.Draw()
Game.Update()
