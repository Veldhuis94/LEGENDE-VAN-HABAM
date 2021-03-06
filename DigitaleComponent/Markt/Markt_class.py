import sys
sys.path.append('..') #Go one folder up to access the Utilities folder

from tellers.tellers_class import tellers
from Utilities.Button import Button
import random
class Markt:
    def __init__(self,tellers):

        self.movetoMainMenu = False
        self.backButton= Button(1300 , 950,txt = 'Terug', onClick = self.onBackClick, w = 250, h=50)
        self.tellers=tellers
        self.showcard=False
        self.boughtbags=0
        self.enoughbrick=True
        self.enoughgrain=True
        self.price= 3
        self.effect14=False
        self.clicked=False
        self.resourcename='nothing'
        self.enoughmats=True
        self.chosenmat=5
        self.pressed=False
        self.enoughmatspp=True
        self.buttons=[Button(200, 150, txt="EffectKaart", onClick =self.chosencard, w = 250, h = 50),
                Button(200, 250, txt="Reset", onClick =self.reset, w = 250, h = 50),
                Button(1300, 250, txt="Rugzak", onClick =self.backpack, w = 250, h = 50),
                Button(850, 470, txt="Gebruik", onClick =self.Effect14Used, w = 250, h = 50),
                Button(1300, 550, txt="Krachtpunt P1", onClick =self.powerup1, w = 250, h = 50),
                Button(1300, 650, txt="Krachtpunt P2", onClick =self.powerup2, w = 250, h = 50),
                Button(1300, 750, txt="Krachtpunt P3", onClick =self.powerup3, w = 250, h = 50),
                Button(1300, 850, txt="Krachtpunt P4", onClick =self.powerup4, w = 250, h = 50),
                ]
    
    
        self.resourcesbuttons=[Button(200,600, txt="Hout", onClick =self.Exchangewood, w = 250, h = 50),
                        Button(200,700, txt="Steen", onClick =self.Exchangebrick, w = 250, h = 50),
                        Button(200,800, txt="Ijzer", onClick =self.Exchangemetal, w = 250, h = 50),
                        Button(200,900, txt="Graan", onClick =self.Exchangegrain, w = 250, h = 50),]
    
    
        self.matsbuttons=[Button(550,600, txt="Hout", onClick =self.pluswood, w = 250, h = 50),
                    Button(550,700, txt="Steen", onClick =self.plusstone, w = 250, h = 50),
                    Button(550,800, txt="Ijzer", onClick =self.plusmetal, w = 250, h = 50),
                    Button(550,900, txt="Graan", onClick =self.plusgrain, w = 250, h = 50),]
    
    
    
        self.errorbuttons=[Button(1650,350, txt="OK", onClick =self.NoBrickError, w = 100, h = 50),
                    Button(500,300, txt="OK", onClick =self.NoGrainError, w = 100, h = 50),
                    Button(850,750, txt="OK", onClick =self.NoMatserror, w = 100, h = 50),
                    Button(1600,730, txt="OK", onClick =self.NoMatsppError, w = 100, h = 50),]
    def onBackClick(self,self1):
        self.movetoMainMenu = True
    def powerup1(self,self1):

        if self.tellers.wood >=self.price and self.tellers.brick >=self.price and self.tellers.metal>=self.price and self.tellers.grain>=self.price:
            self.tellers.power1+=1
            self.tellers.wood -=self.price
            self.tellers.brick -=self.price
            self.tellers.metal-=self.price
            self.tellers.grain-=self.price
        else:
            self.enoughmatspp=False
    def powerup2(self,self1):

        if self.tellers.wood >=self.price and self.tellers.brick >=self.price and self.tellers.metal>=self.price and self.tellers.grain>=self.price:
            self.tellers.power2+=1
            self.tellers.wood -=self.price
            self.tellers.brick -=self.price
            self.tellers.metal-=self.price
            self.tellers.grain-=self.price
        else:
            self.enoughmatspp=False


    def powerup3(self,self1):

        if self.tellers.wood >=self.price and self.tellers.brick >=self.price and self.tellers.metal>=self.price and self.tellers.grain>=self.price:
            self.tellers.power3+=1
            self.tellers.wood -=self.price
            self.tellers.brick -=self.price
            self.tellers.metal-=self.price
            self.tellers.grain-=self.price
        else:
            self.enoughmatspp=False


    def powerup4(self,self1):

        if self.tellers.wood >=self.price and self.tellers.brick >=self.price and self.tellers.metal>=self.price and self.tellers.grain>=self.price:
            self.tellers.power4+=1
            self.tellers.wood -=self.price
            self.tellers.brick -=self.price
            self.tellers.metal-=self.price
            self.tellers.grain-=self.price
        else:
            self.enoughmatspp=False
    def chosencard(self,self1):

        self.card=random.choice(self.effectcards)

        if self.card==self.effectcards[9]:
            self.tellers.effect10=True
        if self.card==self.effectcards[13] and self.effect14==True:
            self.card=random.choice(self.effectcards2)
        if self.tellers.grain>=self.price:
            self.showcard=True
            self.buttons[0].enabled=False
            self.tellers.grain-=self.price
        else:
            self.enoughgrain=False
            self.price=3


    def effectcard(self):

        if self.showcard==True:
            image(self.card,352,77)


    def reset(self,self1):

        self.showcard=False
        self.buttons[0].enabled=True
        if self.card==self.effectcards[13]:
            self.effect14=True
        if self.card==self.effectcards[4]:
            self.price=self.price//2
        else:
            self.price=3


    def backpack(self,self1):

        if self.tellers.brick >=self.price:
            self.tellers.bagcount=True
            self.buttons[2].enabled=False
            self.tellers.brick -=self.price
            self.tellers.capacity+=3
        else:
            self.enoughbrick=False


    def NoBrickError(self,self1):

        self.enoughbrick=True


    def NoGrainError(self,self1):

        self.enoughgrain=True


    def Effect14Used(self,self1):

        self.effect14=False


    def Exchangewood(self,self1):

        if self.tellers.wood >=self.price:
            self.tellers.wood -=self.price
            self.clicked=True
            self.chosenmat=0
        else:
            self.resourcename='Hout'
            self.enoughmats=False
            self.clicked=True
            self.chosenmat=5


    def Exchangebrick(self,self1):

        if self.tellers.brick >=self.price:
            self.tellers.brick -=self.price
            self.clicked=True
            self.chosenmat=1
        else:
            self.resourcename='steen'
            self.enoughmats=False
            self.clicked=True
            self.chosenmat=5


    def Exchangemetal(self,self1):

        if self.tellers.metal>=self.price:
            self.tellers.metal-=self.price
            self.clicked=True
            self.chosenmat=2
        else:
            self.resourcename='Ijzer'
            self.enoughmats=False
            self.clicked=True
            self.chosenmat=5


    def Exchangegrain(self,self1):

        if self.tellers.grain>=self.price:
            self.tellers.grain-=self.price
            self.clicked=True
            self.chosenmat=3
            
        else:
            self.resourcename='Graan'
            self.enoughmats=False
            self.clicked=True
            self.chosenmat=5
    def pluswood(self,self1):

        if (self.tellers.wood +self.tellers.metal+self.tellers.brick +self.tellers.grain)<(self.tellers.capacity):
            self.tellers.wood +=1
            self.clicked=False

    def plusstone(self,self1):

        if (self.tellers.wood +self.tellers.metal+self.tellers.brick +self.tellers.grain)<(self.tellers.capacity):
            self.tellers.brick +=1
            self.clicked=False
    
    def plusmetal(self,self1):

        if (self.tellers.wood +self.tellers.metal+self.tellers.brick +self.tellers.grain)<(self.tellers.capacity):
            self.tellers.metal+=1
            self.clicked=False

    def plusgrain(self,self1):

        if (self.tellers.wood +self.tellers.metal+self.tellers.brick +self.tellers.grain)<(self.tellers.capacity):
            self.tellers.grain+=1
            self.clicked=False

    def NoMatserror(self,self1):

        self.clicked=False
        self.enoughmats=True
    def NoMatsppError(self,self1):
        self.enoughmatspp=True    
            


    def setup(self):
        self.effectcards=[]
        self.effectcards2=[]
        self.backgr=loadImage('BG.png')
        for self.i in range(1,21):
            self.filename='effectkaart'+str(self.i)+'.png'
            self.effectcards.append(loadImage(self.filename))
        for self.i in range(1,21):
            self.filename='effectkaart'+str(self.i)+'.png'
            if self.i!=14:
                self.effectcards2.append(loadImage(self.filename))


        

    def draw(self):
        image(self.backgr,0,0)
        self.backButton.update()
        self.backButton.draw()
        for self.x in range(3):
            self.buttons[self.x].draw()
            self.buttons[self.x].update()
        fill(0)
        text("Effectkaart",500,20)
        noFill()
        rect(350,75,304,341,5)
        self.effectcard()
        if not self.enoughbrick:
            rect(1500,100,300,300)
            fill(0)
            text('\n'+'Onvoldoende'+'\n'+'steen voor'+'\n'+'een rugzak!',1650,100)
            self.errorbuttons[0].draw()
            self.errorbuttons[0].update()

        if not self.enoughgrain:
            fill(0)
            text('Onvoldoende'+'\n'+'graan voor'+'\n'+'een effectkaart!',500,100)
            self.errorbuttons[1].draw()
            self.errorbuttons[1].update()
        if self.effect14:
            rect(700,77,304,341,5)
            image(self.effectcards[13],702,79)
            self.buttons[3].draw()
            self.buttons[3].update()
        if self.buttons[0].enabled==True:
            self.buttons[1].enabled=False
        else:
            self.buttons[1].enabled=True
        fill(0)
        text('Wissel : ',200,500)
        text('Voor : ',550,500)
        for i in range(4):
            self.resourcesbuttons[i].draw()
            self.resourcesbuttons[i].update()
            self.matsbuttons[i].draw()
            self.matsbuttons[i].update()
            if self.clicked:
                self.resourcesbuttons[i].enabled=False
                if self.enoughmats and i!=self.chosenmat:
                    self.matsbuttons[i].enabled=True
            else:
                self.resourcesbuttons[i].enabled=True
                self.matsbuttons[i].enabled=False         
            
        if not self.enoughmats:
            fill(0)
            text('Onvoldoende'+'\n'+self.resourcename+'!',850,630)
            noFill()
            rect(700,600,300,200,5)
            self.errorbuttons[2].draw()
            self.errorbuttons[2].update()
        for self.i in range(4,8):
            self.buttons[self.i].draw()
            self.buttons[self.i].update()
        if not self.enoughmatspp:
            noFill()
            rect(1450,550,300,250,5)
            fill(0)
            text('Onvoldoende'+'\n'+'Resources!',1600,600)
            self.errorbuttons[3].draw()
            self.errorbuttons[3].update()
            for self.i in range(4,8):
                self.buttons[self.i].enabled=False
        else:
            for self.i in range(4,8):
                self.buttons[self.i].enabled=True
