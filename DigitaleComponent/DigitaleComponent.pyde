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
from Credits.CreditsPage import Credits
from Markt.Markt_class import Markt
from Spelverloop.Spelverloop import Spelverloop
from Spelverloop.SpelverloopUI import SpelverloopUI
from Rulebook.RulebookPage import Rulebook


currentPhase = AppPhase.MAINMENU
#playernames
p1 = 'Speler 1'
p2 = 'Speler 2'
p3 = 'Speler 3'
p4 = 'Speler 4'
Namen = [p1, p2, p3, p4]
tellerSystem = tellers(Namen)
mainMenu = MainMenu()
battleSystem = None #Wordt later geïnitialiseerd
boardRandomizer = Board()
playernames = Playernames()
creditsPage = Credits()
markt = Markt(tellerSystem)
files = FileResources()
spelverloop = Spelverloop(tellerSystem)
spelverloopUI = SpelverloopUI(spelverloop)
rulebook = Rulebook()


board_randomizer_firstFrame = True

def setup():
    global files
    size(1920, 1000)
    for i in range(1, 7):
        files.loadImageFile('dice_'+str(i)+".png", "dice"+str(i))
    files.loadImageFile('BG.png', "background")
    files.loadFontFile("BlackChancery.vlw", "defaultfont")
    files.loadImageFile('buitenspel_icon.png', 'buitenspel_icon')
    files.loadImageFile('extraLife.png', 'extraLife')
    
    files.loadImageFile('held1.png', 'held1')
    files.loadImageFile('held2.png', 'held2')
    files.loadImageFile('held3.png', 'held3')
    files.loadImageFile('held4.png', 'held4')
    
    files.loadImageFile('tier1.png', 'tier1')
    files.loadImageFile('tier2.png', 'tier2')
    files.loadImageFile('tier3.png', 'tier3')
    files.loadImageFile('tier4.png', 'tier4')
    Button.static_defaultFont = files.getFont("defaultfont")
    Text.static_defaultFont = files.getFont("defaultfont")
    
    tellerSystem.setup()
    boardRandomizer.setup()
    markt.setup()
def draw():
    global board_randomizer_firstFrame
    
    if(currentPhase != AppPhase.BOARD_RANDOMIZER):
        clear()
        board_randomizer_firstFrame = True
        background(files.getImage("background"))
    
    Namen = [p1, p2, p3, p4]
    tellerSystem.Names = Namen
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
    elif(currentPhase == AppPhase.MARKET):
        runMarket()
    elif(currentPhase == AppPhase.SPELVERLOOP):
        runSpelverloop()
    elif(currentPhase == AppPhase.RULEBOOK):
        runRulebook()
    else:
        runMainMenu()
    
def runBoardRandomizer():
    global currentPhase
    global board_randomizer_firstFrame
    if(board_randomizer_firstFrame):
        clear()
        background(files.getImage("background"))
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
    global Names
    tellerSystem.draw()
    if(tellerSystem.goToMainMenu):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        tellerSystem.goToMainMenu = False
def runBattleSystem():
    global battleSystem
    global currentPhase
    
    if(battleSystem == None):
        playerNames = [p1, p2, p3, p4] #Stuur de spelernamen naar het gevechtssysteem
        battleSystem = BattleSystem(playerNames, tellerSystem, files)
        
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
    global currentPhase
    creditsPage.update()
    creditsPage.draw()
    if(creditsPage.toMainMenu == True):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        creditsPage.toMainMenu = False

def runMarket():
    global markt
    global currentPhase
    markt.draw()
    if(markt.movetoMainMenu):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        markt.movetoMainMenu = False
def runPlayernames():
    global playernames
    global currentPhase
    global p1  
    global p2
    global p3
    global p4
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
def runSpelverloop():
    global currentPhase
    spelverloopUI.draw()
    
    if(spelverloopUI.goBackToMainMenu == True):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        spelverloopUI.goBackToMainMenu = False
def runRulebook():
    global currentPhase
    global rulebook
    rulebook.update()
    rulebook.draw()
    if(rulebook.toMainMenu == True):
        currentPhase = AppPhase.MAINMENU
        mainMenu.phase = currentPhase
        rulebook.toMainMenu = False
        rulebook.currentPage = 0
