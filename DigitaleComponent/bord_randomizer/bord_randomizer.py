import random
from Button import Button
class Board:
    def __init__(self):
        self.button=Button(960, 1000, txt="Nieuw Bord", bgColor=(255, 255, 255), onClick =self.draw_board, w = 350, h = 60)
    def draw_board(self,b):
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
        self.amount_pieces=0
        self.amount_rows=0
        self.piece_x=300
        self.piece_y=100
        def row(self,amount_pieces,piece_x,piece_y):
            while self.amount_pieces<13:
                self.piece=random.choice(self.board)
                image(self.piece,self.piece_x,self.piece_y)
                self.piece_x+=100
                self.amount_pieces+=1
        while self.amount_rows<7:
            self.amount_pieces=0
            self.piece_y+=100
            self.piece_x=300
            row(self,self.amount_pieces,self.piece_x,self.piece_y)
            self.amount_rows+=1
        
    def setup(self):
        fullScreen()
        self.font=loadFont('BlackChancery-48.vlw')
        self.img=loadImage('TITLESCREEN2.png')
        # background(255,165,0)
        background(self.img)
        textFont(self.font)
        fill(0)
        text('De Legende Van HABAM',700,150)
    def draw(self):
        self.button.update()
        self.button.draw()
        