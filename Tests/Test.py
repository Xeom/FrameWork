##
Game.CreateScreen(500,500)

Box = Game.New(Sprite)
Box.Set(100, 10, 0xFF0000)
Box2 = Game.New(SubSurface, cache=False)
Box2.SetImagePath("Cat.jpg")
Box2.SetPos(200,200)
Text = Game.New(TextBox)
Text.SetFontAndSize("verdana", 16)
V = 0
A = 0
I = False
## Forever
if I:
    Box2.SetImagePath("Cat.jpg")
else:
    Box2.SetImagePath("Cat2.jpg")

I = not I

Box.Forward(V)
Box.Turn(A)
if Box.IsColliding(Box2):
    V = -V
    A = -A
Text.SetText(str(int(Game.GetFPS())))
Text.UpdateImage()
Game.Draw()
Game.Update()
if "w" in Event.KeysDown:
    V += 0.01

if "a" in Event.KeysDown:
    A += 0.01

if "s" in Event.KeysDown:
    V -= 0.01

if "d" in Event.KeysDown:
    A -= 0.01

