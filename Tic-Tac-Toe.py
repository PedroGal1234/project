#Pedro Gallino
#11/1/17
#tic-tac-toe against computer

from ggame import *

#Does Something when someone clicks On an open Sace
def mouseClick(event):
#Prints out things when clicks in first column
    if event.x < 200 and event.x > 50:
        if event.y < 200 and event.y > 50:
            Sprite(x1,(80,175))
            Sprite(x2,(80,75))
        elif event.y < 350 and event.y > 200:
            Sprite(x1,(80,320))
            Sprite(x2,(80,220))
        elif event.y < 650 and event.y > 350:
            Sprite(x1,(80,465))
            Sprite(x2,(80,365))
#Prints out things when clicks in second column  
    elif event.x < 350 and event.x > 50:
        if event.y < 200 and event.y > 50:
            Sprite(x1,(225,175))
            Sprite(x2,(225,75))
        elif event.y < 350 and event.y > 200:
            Sprite(x1,(225,320))
            Sprite(x2,(225,220))
        elif event.y < 650 and event.y > 350:
            Sprite(x1,(225,465))
            Sprite(x2,(225,365))
#Prints out things when clicks in third column
    elif event.x < 500 and event.x > 350:
        if event.y < 200 and event.y > 50:
            Sprite(x1,(370,175))
            Sprite(x2,(370,75))
        elif event.y < 350 and event.y > 200:
            Sprite(x1,(370,320))
            Sprite(x2,(370,220))
        elif event.y < 650 and event.y > 350:
            Sprite(x1,(370,465))
            Sprite(x2,(370,365))

    
    
    if event.x < 500 and event.x > 350:
        if event.y < 350 and event.y > 200:
            Sprite(x1,(370,320))
            Sprite(x2,(370,220))


if __name__ == '__main__':
    black = Color(0x00000,1)
    blackOutline = LineStyle(10,black)
    boardV1 = LineAsset(0,450,blackOutline)
    boardH1 = LineAsset(450,0,blackOutline)
    
    x1 = LineAsset(100,-100,LineStyle(8,black))
    x2 = LineAsset(100,100,LineStyle(8,black))
    o1 = 
    o2 = 
    
    #Desplays the board
    Sprite(boardV1,(200,50))
    Sprite(boardV1,(350,50))
    Sprite(boardH1,(50,200))
    Sprite(boardH1,(50,350))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()