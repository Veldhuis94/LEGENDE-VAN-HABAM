#Gemaakt door Audi
from Utilities.Button import Button
from Utilities.Page import Page
from Utilities.Text import Text

from BattleSystem.BattleSystem import BattleSystem
from AppPhase import AppPhase

class MainMenu:
    page = Page()
    phase = AppPhase.MAINMENU
    def __init__(self):
        def onInventoryClick(button):
            self.phase = AppPhase.INVENTORY
        def onBattleSystemClick(button):
            self.phase = AppPhase.BATTLESYSTEM
        def onBoardRandomizerClick(button):
            self.phase = AppPhase.BOARD_RANDOMIZER
        def onGameManualClick(button):
            self.phase = AppPhase.GAME_MANUAL
        def onCreditsClick(button):
            self.phase = AppPhase.CREDITS
            
        self.page.add(Text("Hoofdmenu", 500, 100, 500, 100, txtColor=(255,255,255), txtSize = 50))
        self.page.add(Button(500, 300, onClick = onInventoryClick, txt="Inventaris"))
        self.page.add(Button(500, 380, onClick = onBattleSystemClick, txt="Gevecht"))
        self.page.add(Button(500, 460, onClick = onBoardRandomizerClick, txt="Bord randomizer"))
        self.page.add(Button(500, 540, onClick = onGameManualClick, txt="Spelregels"))
        self.page.add(Button(500, 620, onClick = onCreditsClick, txt="Credits"))
       
    def draw(self):
       self.page.update()
       self.page.draw()
