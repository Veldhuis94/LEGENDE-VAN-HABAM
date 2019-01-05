import sys
sys.path.append('..') #Go one folder up to access the Utilities folder
from Utilities.Button import Button
import random

class Board:
    def __init__(self):
        def onDrawBoardClick(button):
            self.draw_board()
        self.button=Button(300, 600, txt="Nieuw Bord", bgColor=(255, 255, 255), onClick = onDrawBoardClick, w = 350, h = 60)

        def onBackButtonClick(button):
            self.goToMainMenu = True
        self.goToMainMenu = False
        self.backButton = Button(700, 600, txt="Back", onClick=onBackButtonClick)
    def boardSetup(self):
        self.board=[]
        self.wood=loadImage('Hout.jpg')
        self.stone=loadImage('Stone.jpg')
        self.metal=loadImage('Metaal.jpg')
        self.water=loadImage('Water.jpg')
        self.grain=loadImage('Graan.png')
        self.empty=loadImage('empty_wood.jpg')
        for n in range(5):
            self.board.append(self.wood)
            self.board.append(self.stone)
            self.board.append(self.metal)
            self.board.append(self.grain)
        for n in range(48):
            self.board.append(self.empty)
        for n in range(23):
            self.board.append(self.water)

    def draw_board(self):
        self.amount_pieces=0
        self.amount_rows=0
        self.piece_x=180
        self.piece_y=-50
        def row(self,amount_pieces,piece_x,piece_y):
            while self.amount_pieces<13:
                self.piece=random.choice(self.board)
                self.piece.resize(75,75) #Make them smaller so all the pieces can be displayed on the window 
                image(self.piece,self.piece_x,self.piece_y)
                self.piece_x+=75
                self.amount_pieces+=1
        while self.amount_rows<7:
            self.amount_pieces=0
            self.piece_y+=75
            self.piece_x=12
            row(self,self.amount_pieces,self.piece_x,self.piece_y)
            self.amount_rows+=1
        
    def setup(self):
        #fullScreen()
        #self.font=loadFont('BlackChancery-48.vlw')
        self.font=loadFont('BlackChancery.vlw')

        self.img=loadImage('TITLESCREEN2.png')
        # background(255,165,0)
        self.img.resize(1000, 726) #resize to the size of the screen

        self.boardSetup()
    def drawOnce(self):
        #background(self.img)
        textFont(self.font)
    def draw(self):
        self.button.update()
        self.backButton.update()
        self.button.draw()
        self.backButton.draw()
        