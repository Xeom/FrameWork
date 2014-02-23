##
print(help(Game))
Game.CreateScreen(500,500)

Box = Game.New(Sprite)
Box.Set(100, 10, 0xFF0000)

Box2 = Game.New(SubSurface)
Box2.SetImagePath("Cat.jpg.OHSHIT")
Box2.SetPos(200,200)
Text = Game.New(TextBox)
Text.SetFontAndSize("verdana", 16)
V = 0
A = 0
Over = False
Line = Game.New(Pen)

print("HI")

## Forever
0/0
if Text.IsColliding(Event.MousePos):
    Text.SetColour(0xFF0000)

else:
    Text.SetColour(0x000000)
if Box.IsColliding(Event.MousePos):
    if 1 in Event.MouseButtons:
        Box.Fill(0xFFFF00)
    else:
        Box.Fill(0xFF7700)
    Over = True

else:
    Box.Fill(0xFF0000)
    Over = False

Line.Up()
Line.SetPos(0, 0)
Line.Down()
Line.SetPos(*Box.GetCenter())

if Box.IsColliding(Box2):
    V = -V
    A = -A


Box.Forward(V)
Box.Turn(A)


Text.SetText(str(int(Game.GetFPS())))

Game.Update()
Game.ClearCanvas()

V *= 0.99
A *= 0.99

if "w" in Event.KeysDown:
    V += 0.1

if "a" in Event.KeysDown:
    A += 0.1

if "s" in Event.KeysDown:
    V -= 0.1

if "d" in Event.KeysDown:
    A -= 0.1

