from Button import Button
import random
class tellers:

    def __init__(self):
        self.wood=0
        self.brick=0
        self.metal=0
        self.grain=0
        self.stamina1=7
        self.stamina2=7
        self.stamina3=7
        self.stamina4=7
        self.win_points=0
        self.capacity=10
        player1='Mahmoud'
        self.p1_display='Stamina '+player1
        player2='Hakan'
        self.p2_display='Stamina '+player2
        player3='Audi'
        self.p3_display='Stamina '+player3
        player4='Bastiaan'
        self.p4_display='Stamina '+player4
        self.img=loadImage("TITELSCREEN2.png")
        self.w=1920
        self.h=1080
        self.buttons2=[Button(330, 100, txt="+", bgColor=(255, 255, 255), onClick =self.addition_wood, w = 100, h = 50), 
            Button(100, 100, txt="-", bgColor=(255, 255, 255), onClick =self.sub_wood, w = 100, h = 50), 
            Button(330, 250, txt="+", bgColor=(255, 255, 255), onClick =self.addition_brick, w = 100, h = 50),
            Button(100, 250, txt="-", bgColor=(255, 255, 255), onClick =self.sub_brick, w = 100, h = 50),
            Button(330, 400, txt="+", bgColor=(255, 255, 255), onClick =self.addition_metal, w = 100, h = 50),
            Button(100, 400, txt="-", bgColor=(255, 255, 255), onClick =self.sub_metal, w = 100, h = 50),
            Button(330, 550, txt="+", bgColor=(255, 255, 255), onClick =self.addition_grain, w = 100, h = 50),
                Button(100, 550, txt="-", bgColor=(255, 255, 255), onClick =self.sub_grain, w = 100, h = 50),
                Button(730, 100, txt="+", bgColor=(255, 255, 255), onClick =self.addition_stamina1, w = 100, h = 50),
                Button(500, 100, txt="-", bgColor=(255, 255, 255), onClick =self.sub_stamina1, w = 100, h = 50),
                Button(730, 250, txt="+", bgColor=(255, 255, 255), onClick =self.addition_stamina2, w = 100, h = 50), 
                Button(500, 250, txt="-", bgColor=(255, 255, 255), onClick =self.sub_stamina2, w = 100, h = 50),
                Button(730, 400, txt="+", bgColor=(255, 255, 255), onClick =self.addition_stamina3, w = 100, h = 50), 
                Button(500, 400, txt="-", bgColor=(255, 255, 255), onClick =self.sub_stamina3, w = 100, h = 50),
                Button(730, 550, txt="+", bgColor=(255, 255, 255), onClick =self.addition_stamina4, w = 100, h = 50), 
                Button(500, 550, txt="-", bgColor=(255, 255, 255), onClick =self.sub_stamina4, w = 100, h = 50),
                #Button(730, 670, txt="+", bgColor=(255, 255, 255), onClick =self.addition_winning, w = 100, h = 50),
                Button(330, 670, txt="+", bgColor=(255, 255, 255), onClick =self.addition_capacity, w = 100, h = 50),
                Button(100, 670, txt="-", bgColor=(255, 255, 255), onClick =self.sub_capacity, w = 100, h = 50),
                #Button(500, 670, txt="-", bgColor=(255, 255, 255), onClick =self.sub_winning, w = 100, h = 50),
                Button(1000, 100, txt="Dag voorbij", bgColor=(255, 255, 255), onClick =self.playersdone, w = 300, h = 50),
                Button(1000, 200, txt="reset", bgColor=(255, 255, 255), onClick =self.another_card, w = 300, h = 50)]
    def addition_winning(self,self1):

        if self.win_points<20:
            self.win_points+=1
    def sub_winning(self,self1):

        if self.win_points>0:
            self.win_points-=1
    def addition_capacity(self,self1):

        self.capacity+=1
    def sub_capacity(self,self1):

        if self.capacity>10 and self.capacity!=self.brick+self.metal+self.wood+self.grain:
            self.capacity-=1    
    def addition_stamina1(self,self1):

        self.stamina1+=1
    def sub_stamina1(self,self1):

        if self.stamina1>0:
            self.stamina1-=1
    def addition_stamina2(self,self1):

        self.stamina2+=1
    def sub_stamina2(self,self1):
        if self.stamina2>0:
            self.stamina2-=1
    def addition_stamina3(self,self1):
        self.stamina3+=1
    def sub_stamina3(self,self1):

        if self.stamina3>0:
            self.stamina3-=1
    def addition_stamina4(self,self1):
        self.stamina4+=1   
    def sub_stamina4(self,self1):
        if self.stamina4>0:
            self.stamina4-=1
    def addition_wood (self,self1):
        if (self.wood+self.metal+self.brick+self.grain)<(self.capacity):
            self.wood+=1
    def sub_wood(self,self1):
        if self.wood>1:
            self.wood-=1
        else:
            self.wood=0
    def addition_brick(self,self1):
        if (self.wood+self.metal+self.brick+self.grain)<(self.capacity):
            self.brick+=1
    def sub_brick(self,self1):
        if self.brick >1:
            self.brick-=1
        else:
            self.brick=0
    def addition_metal(self,self1):
        if (self.wood+self.metal+self.brick+self.grain)<(self.capacity):
            self.metal+=1
    def sub_metal(self,self1):
        if self.metal>1:
            self.metal-=1
        else:
            self.metal=0
    def addition_grain(self,self1):
        if (self.wood+self.metal+self.brick+self.grain)<(self.capacity):
            self.grain+=1
    def sub_grain(self,self1):
        if self.grain>1:
            self.grain-=1
        else:
            self.grain=0
    def playersdone(self,self1):
        self.players_done=True
        return self.players_done

    def action_card(self):
        self.clicked=0
        if self.players_done:
            image(self.card,1203,83)
            self.buttons2[18].enabled=False
    
    def another_card(self,self1):
        global card
        global players_done
        global clicked
        global buttons2
        self.players_done=False
        self.clicked+=1
        self.card=random.choice(self.action_cards)
        self.action_cards.remove(self.card)
        self.buttons2[18].enabled=True
        if self.clicked==1:
            redraw()
    def winning(self,self1):
        global win_count
        global player_win
        if self.player_win:
            win_count+=1
    

        

    def setup(self):
        global players_done
        global action_cards
        global card
        global players_done
        global clicked

        self.img=loadImage("TITLESCREEN2.png")
        self.players_done=False
        self.clicked=0
        self.action_cards=[]
        for self.i in range(1,21):
            self.filename = "actiekaart"+str(self.i)+".png"
            if self.i!=10:
                self.action_cards.append(loadImage(self.filename))   
        self.card=random.choice(self.action_cards)
        self.action_cards.remove(self.card)
        


        
    def draw(self):
       image(self.img,0,0)
       noFill()
       rect(1200,80,305,342,5)
       fill(0)
       text('Actie kaart',1350,20)
       text('HOUT',220,20)
       text(str(self.wood),220,80)
       text('STEEN',220,170)
       text(str(self.brick),220,230)
       text('IJZER',220,320)
       text(str(self.metal),220,380)
       text('GRAAN',220,480)
       text(str(self.grain),220,530)
       text(self.p1_display,620,20)
       text(str(self.stamina1),620,80)
       text(self.p2_display,620,170)
       text(str(self.stamina2),620,230)
       text(self.p3_display,620,320)
       text(str(self.stamina3),620,380)
       text(self.p4_display,620,480)
       text(str(self.stamina4),620,530)
       text('Overwinningspunten',620,600)
       text(str(self.win_points),620,650)
       text('Opslag Capaciteit',220,600)
       text(str(self.capacity),220,650)

       self.action_card()
       for button in self.buttons2:
            button.update()
            button.draw()
            button.update()
