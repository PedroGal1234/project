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
            data['s1'] += 1
        elif event.y < 350 and event.y > 200:
            Sprite(data['x1'],(80,320))
            Sprite(data['x2'],(80,220))
            data['s2'] += 1
        elif event.y < 650 and event.y > 350:
            Sprite(data['x1'],(80,465))
            Sprite(data['x2'],(80,365))
            data['s3'] += 1
#Prints out things when clicks in second column  
    elif event.x < 350 and event.x > 50:
        if event.y < 200 and event.y > 50:
            Sprite(data['x1'],(225,175))
            Sprite(data['x2'],(225,75))
            data['s4'] += 1
        elif event.y < 350 and event.y > 200:
            Sprite(data['x1'],(225,320))
            Sprite(data['x2'],(225,220))
            data['s5'] += 1
        elif event.y < 650 and event.y > 350:
            Sprite(data['x1'],(225,465))
            Sprite(data['x2'],(225,365))
            data['s6'] += 1    
#Prints out things when clicks in third column
    elif event.x < 500 and event.x > 350:
        if event.y < 200 and event.y > 50:
            Sprite(data['x1'],(370,175))
            Sprite(data['x2'],(370,75))
            data['s7'] += 1
        elif event.y < 350 and event.y > 200:
            Sprite(data['x1'],(370,320))
            Sprite(data['x2'],(370,220))
            data['s8'] += 1
        elif event.y < 650 and event.y > 350:
            Sprite(data['x1'],(370,465))
            Sprite(data['x2'],(370,365))
            data['s9'] += 1
    ComputerTurn()
    end()

def ComputerTurn():
    place = randint(1,9)
    if place == 1 and data['s1'] == 0:
        Sprite(data['o'],(110,110))
        data['s1'] += 1
    elif place == 2 and data['s2'] == 0:
        Sprite(data['o'],(275,110))
        data['s2'] += 1
    elif place == 3 and data['s3'] == 0:
        Sprite(data['o'],(425,110))
        data['s3'] += 1
    elif place == 4 and data['s4'] == 0:
        Sprite(data['o'],(110,275))
        data['s4'] += 1
    elif place == 5 and data['s5'] == 0:
        Sprite(data['o'],(275,275))
        data['s5'] += 1
    elif place == 6 and data['s6'] == 0:
        Sprite(data['o'],(425,275))
        data['s6'] += 1
    elif place == 7 and data['s7'] == 0:
        Sprite(data['o'],(110,450))
        data['s7'] += 1
    elif place == 8 and data['s8'] == 0:
        Sprite(data['o'],(275,425))
        data['s8'] += 1
    elif place == 9 and data['s9'] == 0:
        Sprite(data['o'],(425,425))
        data['s9'] += 1
    else:
        ComputerTurn()

def end():
    if data['s1']>0 and data['s2']>0 and data['s3']>0 and data['s4']>0 and data['s5']>0 and data['s6']>0 and data['s7']>0 and data['s8']>0 and data['s9']>0:
        print('Tie game')

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