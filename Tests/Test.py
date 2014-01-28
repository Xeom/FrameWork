##
Game.CreateScreen(500,500)

Box = Game.New(Sprite)
Box.Set(100, 10, 0xFF0000)
Box2 = Game.New(SubSurface)
Box2.Set(100, 10, 0xFF0000)
Box2.SetPos(200,200)

def Update():
    if Box.IsColliding(Box2):
        print(Box.IsColliding(Box2))
    Game.Draw()
    Game.Update()

V = 0
A = 0

## Forever
Box.Forward(V)
Box.Turn(A)
Update()

## KeyDown w
V += 1

## KeyDown d
A += 0.1

## KeyDown a
A -= 0.1

## KeyDown s
V -= 1
