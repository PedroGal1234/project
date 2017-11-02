#Pedro Gallino
#11/1/17
#tic-tac-toe against computer

from ggame import *
from random import randint

#Does Something when someone clicks On an open Sace
def mouseClick(event):
#Prints out things when clicks in first column
    if event.x < 200 and event.x > 50:
        if event.y < 200 and event.y > 50:
            Sprite(data['x1'],(80,175))
            Sprite(data['x2'],(80,75))
        elif event.y < 350 and event.y > 200:
            Sprite(data['x1'],(80,320))
            Sprite(data['x2'],(80,220))
        elif event.y < 650 and event.y > 350:
            Sprite(data['x1'],(80,465))
            Sprite(data['x2'],(80,365))
#Prints out things when clicks in second column  
    elif event.x < 350 and event.x > 50:
        if event.y < 200 and event.y > 50:
            Sprite(data['x1'],(225,175))
            Sprite(data['x2'],(225,75))
        elif event.y < 350 and event.y > 200:
            Sprite(data['x1'],(225,320))
            Sprite(data['x2'],(225,220))
        elif event.y < 650 and event.y > 350:
            Sprite(data['x1'],(225,465))
            Sprite(data['x2'],(225,365))
#Prints out things when clicks in third column
    elif event.x < 500 and event.x > 350:
        if event.y < 200 and event.y > 50:
            Sprite(data['x1'],(370,175))
            Sprite(data['x2'],(370,75))
        elif event.y < 350 and event.y > 200:
            Sprite(data['x1'],(370,320))
            Sprite(data['x2'],(370,220))
        elif event.y < 650 and event.y > 350:
            Sprite(data['x1'],(370,465))
            Sprite(data['x2'],(370,365))
    
    place = randint(1,9)
    if place == 1:
        Sprite(data['o'],(110,110))
    elif place == 2:
        Sprite(data['o'],(275,110))
    elif place == 3:
        Sprite(data['o'],(425,110))
    elif place == 4:
        Sprite(data['o'],(110,275))
    elif place == 5:
        Sprite(data['o'],(275,275))
    elif place == 6:
        Sprite(data['o'],(425,275))
    elif place == 7:
        Sprite(data['o'],(110,450))
    elif place == 8:
        Sprite(data['o'],(275,425))
    elif place == 9:
        Sprite(data['o'],(425,425))
    


if __name__ == '__main__':
    black = Color(0x00000,1)
    white = Color(0xffffff,1)
    blackOutline = LineStyle(10,black)
    boardV1 = LineAsset(0,450,blackOutline)
    boardH1 = LineAsset(450,0,blackOutline)
    data = {}
    
    data['x1'] = LineAsset(100,-100,LineStyle(8,black))
    data['x2'] = LineAsset(100,100,LineStyle(8,black))
    data['o'] = CircleAsset(50,LineStyle(8,black),white)
    data['s1'] = 0
    data['s2'] = 0
    data['s3'] = 0
    data['s4'] = 0
    data['s5'] = 0
    data['s6'] = 0
    data['s7'] = 0
    data['s8'] = 0
    data['s9'] = 0
    #Desplays the board
    Sprite(boardV1,(200,50))
    Sprite(boardV1,(350,50))
    Sprite(boardH1,(50,200))
    Sprite(boardH1,(50,350))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()