#Pedro Gallino
#11/1/17
#tic-tac-toe against computer

from ggame import *

black = Color(0x00000,1)
blackOutline = LineStyle(10,black)

#Does SOmething when someone clicks the hand
def mouseClick(event):
    if event.x < 200 and event.x > 50:
        if event.y < 200 and event.y > 50:
            Sprite(x1,(50,50))
            Sprite(x2,(50,100))


if __name__ == '__main__':
    black = Color(0x00000,1)
    blackOutline = LineStyle(10,black)
    boardV1 = LineAsset(0,450,blackOutline)
    boardH1 = LineAsset(450,0,blackOutline)
    
    x1 = LineAsset(40,-40,blackOutline)
    x2 = LineAsset(40,40,blackOutline)
    
    #Desplays the board
    Sprite(boardV1,(200,50))
    Sprite(boardV1,(350,50))
    Sprite(boardH1,(50,200))
    Sprite(boardH1,(50,350))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()