#Het digitale component voor Legende van Habam is gemaakt door GROEP INF1C

from BattleSystem.BattleSystem import BattleSystem
from MainMenu import MainMenu
from AppPhase import AppPhase
from Utilities.FileResources import FileResources
from Utilities.Button import Button
from Utilities.Text import Text
from Utilities.TextField import TextField
from tellers.tellers_class import tellers
from bord_randomizer.bord_randomizer import Board
from Playernames.PlayernamesPage import Playernames


currentPhase = AppPhase.MAINMENU

mainMenu = MainMenu()
battleSystem = None #Wordt later geïnitialiseerd
tellerSystem = tellers()
boardRandomizer = Board()
playernames = Playernames()

files = FileResources()
#playernames
p1 = 'Speler 1'
p2 = 'Speler 2'
p3 = 'Speler 3'
p4 = 'Speler 4'
board_randomizer_firstFrame = True

def setup():
    global files
    size(1000, 726)
    
    for i in range(1, 7):
        files.loadImageFile('dice_'+str(i)+".png", "dice"+str(i))
    
    files.loadFontFile("BlackChancery.vlw", "defaultfont")
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
    elif(currentPhase == AppPhase.CREDITS):
        runCredits()
    elif(currentPhase == AppPhase.PLAYERNAMES):
        runPlayernames()
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
        boardRandomizer.goToMainMenu = False
def runTellers():
    global tellerSystem
    global currentPhase
    tellerSystem.draw()
    
    if(tellerSystem.goToMainMenu):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        tellerSystem.goToMainMenu = False
def runBattleSystem():
    global battleSystem
    global currentPhase
    
    if(battleSystem == None):
        battleSystem = BattleSystem()
        battleSystem.files = files
        battleSystem.tellers = tellerSystem
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
        
def runCredits():
    global creditsPage
    global curretPhase
    creditsPage.update()
    creditsPage.draw()
    
def runPlayernames():
    global playernames
    global currentPhase
    playernames.update()
    playernames.draw()
    if(playernames.toMainMenu == True):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        playernames.toMainMenu = False
        namelist = playernames.sendBack()
        p1 = namelist[0]
        p2 = namelist[1]
        p3 = namelist[2]
        p4 = namelist[3]
        if p1 == '':
            p1 = 'Speler 1'
        if p2 == '':
            p2 = 'Speler 2'
        if p3 == '':
            p3 = 'Speler 3'
        if p4 == '':
            p4 = 'Speler 4'
        print('Namen veranderd in ', p1, p2, p3, p4)
