#from BattleSystem.Dobbelstenen import setFaces
from BattleSystem.BattleSystem import BattleSystem
from MainMenu import MainMenu
from AppPhase import AppPhase

currentPhase = AppPhase.MAINMENU

mainMenu = MainMenu()
battleSystem = None
diceFaces = [] #images of each dice side (1-6)

def setup(faces):
    global diceFaces
    diceFaces = faces
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
        
