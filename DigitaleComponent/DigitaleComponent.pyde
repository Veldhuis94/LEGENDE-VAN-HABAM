#Made by Audi van Gog en Hakan
#import DigitaleComponent

#from BattleSystem.Dobbelstenen import setFaces
from BattleSystem.BattleSystem import BattleSystem
from MainMenu import MainMenu
from AppPhase import AppPhase

currentPhase = AppPhase.MAINMENU

mainMenu = MainMenu()
battleSystem = None
diceFaces = [] #images of each dice side (1-6)

def setup():
    global diceFaces
    #diceFaces = faces
    size(1000, 726)
    
    #laad de afbeeldingen voor de dobbelstenen (code is van Hakan)
    #Reminder: loadImage can only be executed on this setup function! (You cannot run this on a external script)
    face1=loadImage('dice_1.png')
    face2=loadImage('dice_2.png')
    face3=loadImage('dice_3.png')
    face4=loadImage('dice_4.png')
    face5=loadImage('dice_5.png')
    face6=loadImage('dice_6.png')
    diceFaces=[face1,face2,face3,face4,face5,face6]
def draw():    
    clear()
    
    if currentPhase == AppPhase.BATTLESYSTEM:
        runBattleSystem()
    else:
        runMainMenu()
   
        
def runBattleSystem():
    global battleSystem
    global currentPhase
    
    if(battleSystem == None):
        battleSystem = BattleSystem()
        battleSystem.diceFaces = diceFaces
    if(battleSystem.phase == battleSystem.PHASE_END):
        battleSystem = None
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
    else:
        battleSystem.update()
        battleSystem.draw()

def runMainMenu():
    global mainMenu
    global currentPhase
    mainMenu.draw()
    
    if(not(mainMenu.phase == AppPhase.MAINMENU)):
        currentPhase = mainMenu.phase
        #print("differentPhase")
