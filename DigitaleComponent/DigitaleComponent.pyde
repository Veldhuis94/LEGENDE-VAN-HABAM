#Made by Audi van Gog en Hakan
from BattleSystem.BattleSystem import BattleSystem
from MainMenu import MainMenu
from AppPhase import AppPhase
from Utilities.FileResources import FileResources
from Utilities.Button import Button
from Utilities.Text import Text
from tellers.tellers_class import tellers
from bord_randomizer.bord_randomizer import Board

currentPhase = AppPhase.MAINMENU

mainMenu = MainMenu()
battleSystem = None #Wordt later geïnitialiseerd
tellerSystem = tellers()
boardRandomizer = Board()

files = FileResources()

board_randomizer_firstFrame = True

def setup():
    global files
    size(1000, 726)
    
    for i in range(1, 7):
        files.loadImageFile('dice_'+str(i)+".png", "dice"+str(i))
    
    files.loadFontFile("BlackChancery.vlw", "defaultfont")
    btn = Button(100, 100)
    Button.static_defaultFont = files.getFont("defaultfont")
    Text.static_defaultFont = files.getFont("defaultfont")
    
    tellerSystem.setup()
    boardRandomizer.setup()
def draw():
    global board_randomizer_firstFrame
    
    if(currentPhase != AppPhase.BOARD_RANDOMIZER):
        clear()
        board_randomizer_firstFrame = True
    
    if currentPhase == AppPhase.BATTLESYSTEM:
        runBattleSystem()
    elif(currentPhase == AppPhase.INVENTORY):
        runTellers()
    elif(currentPhase == AppPhase.BOARD_RANDOMIZER):
        runBoardRandomizer()
    else:
        runMainMenu()
    
def runBoardRandomizer():
    global currentPhase
    global board_randomizer_firstFrame
    if(board_randomizer_firstFrame):
        clear()
        boardRandomizer.draw_board()
        boardRandomizer.drawOnce()
        board_randomizer_firstFrame = False
    boardRandomizer.draw()
    
    if(boardRandomizer.goToMainMenu):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
def runTellers():
    global tellerSystem
    global currentPhase
    tellerSystem.draw()
    
    if(tellerSystem.goToMainMenu):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
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
