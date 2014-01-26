##
Game.CreateScreen(500,100)

Box = Game.New(TextBox, size=16)
Box.SetPosition(0, 50)

## KeyPress
if Key == "\b":
    Box.Delete()
    
else:
    Box.Write(Key)
    
Game.Draw()
Game.Update()

