#Pedro Gallino
#11/1/17
#tic-tac-toe against computer

from ggame import *
from random import randint

#Checks to see if a space is empty
def isEmpty(s):
    if data['s'+str(s)] > 0:
        return False
    else:
        return True

#Checks to see if someone won
def winner():
    red = Color(0xff0000,.25)
    redOutline = LineStyle(1,red)
    redRectangle = RectangleAsset(150,150,redOutline,red)
    
    #Checks to see if X won
    if data['s1'] == 1 and data['s2'] == 1 and data['s3'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,50))
        Sprite(redRectangle,(200,50))
        Sprite(redRectangle,(350,50))
    elif data['s4'] == 1 and data['s5'] == 1 and data['s6'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,200))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(350,200))
    elif data['s7'] == 1 and data['s8'] == 1 and data['s9'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,350))
        Sprite(redRectangle,(200,350))
        Sprite(redRectangle,(350,350))
    elif data['s1'] == 1 and data['s4'] == 1 and data['s7'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,50))
        Sprite(redRectangle,(50,200))
        Sprite(redRectangle,(50,350))
    elif data['s2'] == 1 and data['s5'] == 1 and data['s8'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(200,50))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(200,350))
    elif data['s3'] == 1 and data['s6'] == 1 and data['s9'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(350,50))
        Sprite(redRectangle,(350,200))
        Sprite(redRectangle,(350,350))
    elif data['s1'] == 1 and data['s5'] == 1 and data['s9'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,50))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(350,350))
    elif data['s7'] == 1 and data['s5'] == 1 and data['s3'] == 1:
        data['say'] = 'X wins'
        data['gameOver'] = True
        Sprite(redRectangle,(350,50))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(350,350))
    #Checks to see if O won
    if data['s1'] == 2 and data['s2'] == 2 and data['s3'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,50))
        Sprite(redRectangle,(200,50))
        Sprite(redRectangle,(350,50))
    elif data['s4'] == 2 and data['s5'] == 2 and data['s6'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,200))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(350,200))
    elif data['s7'] == 2 and data['s8'] == 2 and data['s9'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,350))
        Sprite(redRectangle,(200,350))
        Sprite(redRectangle,(350,350))
    elif data['s1'] == 2 and data['s4'] == 2 and data['s7'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,50))
        Sprite(redRectangle,(50,200))
        Sprite(redRectangle,(50,350))
    elif data['s2'] == 2 and data['s5'] == 2 and data['s8'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(200,50))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(200,350))
    elif data['s3'] == 2 and data['s6'] == 2 and data['s9'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(350,50))
        Sprite(redRectangle,(350,200))
        Sprite(redRectangle,(350,350))
    elif data['s1'] == 2 and data['s5'] == 2 and data['s9'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(50,50))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(350,350))
    elif data['s7'] == 2 and data['s5'] == 2 and data['s3'] == 2:
        data['say'] = 'O wins'
        data['gameOver'] = True
        Sprite(redRectangle,(350,50))
        Sprite(redRectangle,(200,200))
        Sprite(redRectangle,(50,350))

#Checks to see if a tie
    elif fullboard() == True:
        data['say'] = 'Tie Game'
        data['gameOver'] = True

#Checks to see if board is full for a tie
def fullboard():
    if data['s1']>0 and data['s2']>0 and data['s3']>0 and data['s4']>0 and data['s5']>0 and data['s6']>0 and data['s7']>0 and data['s8']>0 and data['s9']>0:  
        return True
    else:
        return False

#Does Something when someone clicks On an open Sace
def mouseClick(event):
    #Only runs if the game isn't over
    if data['gameOver'] == False:
        #Prints out things when clicks in first column
        if event.x < 200 and event.x > 50:
            if event.y < 200 and event.y > 50 and isEmpty(1) == True:
                Sprite(data['x1'],(80,175))
                Sprite(data['x2'],(80,75))
                data['s1'] = 1
                ComputerTurn()
            elif event.y < 350 and event.y > 200 and isEmpty(4) == True:
                Sprite(data['x1'],(80,320))
                Sprite(data['x2'],(80,220))
                data['s4'] = 1
                ComputerTurn()
            elif event.y < 650 and event.y > 350 and isEmpty(7) == True:
                Sprite(data['x1'],(80,465))
                Sprite(data['x2'],(80,365))
                data['s7'] = 1
                ComputerTurn()
    #Prints out things when clicks in second column  
        elif event.x < 350 and event.x > 50:
            if event.y < 200 and event.y > 50 and isEmpty(2) == True:
                Sprite(data['x1'],(225,175))
                Sprite(data['x2'],(225,75))
                data['s2'] = 1
                ComputerTurn()
            elif event.y < 350 and event.y > 200 and isEmpty(5) == True:
                Sprite(data['x1'],(225,320))
                Sprite(data['x2'],(225,220))
                data['s5'] = 1
                ComputerTurn()
            elif event.y < 650 and event.y > 350 and isEmpty(8) == True:
                Sprite(data['x1'],(225,465))
                Sprite(data['x2'],(225,365))
                data['s8'] = 1
                ComputerTurn()
    #Prints out things when clicks in third column
        elif event.x < 500 and event.x > 350:
            if event.y < 200 and event.y > 50 and isEmpty(3) == True:
                Sprite(data['x1'],(370,175))
                Sprite(data['x2'],(370,75))
                data['s3'] = 1
                ComputerTurn()
            elif event.y < 350 and event.y > 200 and isEmpty(6) == True:
                Sprite(data['x1'],(370,320))
                Sprite(data['x2'],(370,220))
                data['s6'] = 1
                ComputerTurn()
            elif event.y < 650 and event.y > 350 and isEmpty(9) == True:
                Sprite(data['x1'],(370,465))
                Sprite(data['x2'],(370,365))
                data['s9'] = 1
                ComputerTurn()
        winner()
    #It will print a white screen with the winner if the game is over
    else:
        text = TextAsset(data['say'], fill=black, style='bold 100pt Times')
        whiteRectangle = RectangleAsset(1000,1000,whiteOutline,white)
        Sprite(whiteRectangle)
        Sprite(text,(300,100))
        
#Does the computer turn
def ComputerTurn():
    place = randint(1,9)
    if data['s1'] == 1 and data['s2'] == 1 and isEmpty(3) == True:
        Sprite(data['o'],(425,110))
        data['s3'] = 2
    elif data['s2'] == 1 and data['s3'] == 1 and isEmpty(1) == True:
        Sprite(data['o'],(115,110))
        data['s1'] = 2
    elif data['s1'] == 1 and data['s3'] == 1 and isEmpty(2) == True:
        Sprite(data['o'],(275,110))
        data['s2'] = 2
    elif data['s4'] == 1 and data['s5'] == 1 and isEmpty(6) == True:
        Sprite(data['o'],(425,275))
        data['s6'] = 2
    elif data['s4'] == 1 and data['s6'] == 1 and isEmpty(5) == True:
        Sprite(data['o'],(275,275))
        data['s5'] = 2
    elif data['s5'] == 1 and data['s6'] == 1 and isEmpty(4) == True:
        Sprite(data['o'],(115,275))
        data['s4'] = 2


    elif place == 1 and isEmpty(1) == True:
        Sprite(data['o'],(115,110))
        data['s1'] = 2
    elif place == 2 and isEmpty(2) == True:
        Sprite(data['o'],(275,110))
        data['s2'] = 2
    elif place == 3 and isEmpty(3) == True:
        Sprite(data['o'],(425,110))
        data['s3'] = 2
    elif place == 4 and isEmpty(4) == True:
        Sprite(data['o'],(115,275))
        data['s4'] = 2
    elif place == 5 and isEmpty(5) == True:
        Sprite(data['o'],(275,275))
        data['s5'] = 2
    elif place == 6 and isEmpty(6) == True:
        Sprite(data['o'],(425,275))
        data['s6'] = 2
    elif place == 7 and isEmpty(7) == True:
        Sprite(data['o'],(115,425))
        data['s7'] = 2
    elif place == 8 and isEmpty(8) == True:
        Sprite(data['o'],(275,425))
        data['s8'] = 2
    elif place == 9 and isEmpty(9) == True:
        Sprite(data['o'],(425,425))
        data['s9'] = 2
    elif fullboard() == True:
        print('')
    else:
        ComputerTurn()

if __name__ == '__main__':
    black = Color(0x00000,1)
    white = Color(0xffffff,1)
    blackOutline = LineStyle(10,black)
    whiteOutline = LineStyle(10,white)
    boardV1 = LineAsset(0,450,blackOutline)
    boardH1 = LineAsset(450,0,blackOutline)
    
    #sets up the dictionary with all of the variables
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
    data['gameOver'] = False
    data['say'] = ''
    
    #Desplays the board
    Sprite(boardV1,(200,50))
    Sprite(boardV1,(350,50))
    Sprite(boardH1,(50,200))
    Sprite(boardH1,(50,350))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()