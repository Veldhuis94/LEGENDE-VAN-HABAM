#Made by Audi van Gog en Hakan
from BattleSystem.BattleSystem import BattleSystem
from MainMenu import MainMenu
from AppPhase import AppPhase
from Utilities.FileResources import FileResources

currentPhase = AppPhase.MAINMENU

mainMenu = MainMenu()
battleSystem = None
files = FileResources()

def setup():
    global files
    size(1000, 726)
    
    for i in range(1, 7):
        files.loadImageFile('dice_'+str(i)+".png", "dice"+str(i))
    
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
        battleSystem.files = files
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
