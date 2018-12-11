#Made by Audi van Gog en Hakan
from BattleSystem import BattleSystem
import Dobbelstenen

battleSystem = BattleSystem()
def setup():
    size(1000, 726)
    
    #laad de afbeeldingen voor de dobbelstenen (code is van Hakan)
    face1=loadImage('dice_1.png')
    face2=loadImage('dice_2.png')
    face3=loadImage('dice_3.png')
    face4=loadImage('dice_4.png')
    face5=loadImage('dice_5.png')
    face6=loadImage('dice_6.png')
    faces=[face1,face2,face3,face4,face5,face6]
    Dobbelstenen.setFaces(faces)
    
def draw():
    global battleSystem
    clear()
    
    if(battleSystem.phase == battleSystem.PHASE_END):
        battleSystem = BattleSystem() #Start het gevechtssysteem opnieuw op
    else:
        battleSystem.update()
        battleSystem.draw()
