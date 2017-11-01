#Pedro Gallino
#11/1/17
#tic-tac-toe against computer

from ggame import *

black = Color(0x00000,1)
blackOutline = LineStyle(10,black)

def click(event)


if __name__ == '__main__':
    black = Color(0x00000,1)
    blackOutline = LineStyle(10,black)
    boardV1 = LineAsset(0,450,blackOutline)
    boardH1 = LineAsset(450,0,blackOutline)
    
    Sprite(boardV1,(200,50))
    Sprite(boardV1,(350,50))
    Sprite(boardH1,(50,200))
    Sprite(boardH1,(50,350))
    
    App().run()