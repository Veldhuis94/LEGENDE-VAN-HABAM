#Gemaakt door Audi
from Utilities.Button import Button
from Utilities.Page import Page
from Utilities.Text import Text
from Utilities.TextField import TextField

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
        def onPlayernameClick(button):
            self.phase = AppPhase.PLAYERNAMES
            
        self.page.add(Text("Hoofdmenu", 500, 100, 500, 100, txtColor=(255,255,255), txtSize = 50))
        self.page.add(Button(500, 200, onClick = onInventoryClick, txt="Inventaris"))
        self.page.add(Button(500, 280, onClick = onBattleSystemClick, txt="Gevecht"))
        self.page.add(Button(500, 360, onClick = onBoardRandomizerClick, txt="Bord randomizer"))
        self.page.add(Button(500, 440, onClick = onGameManualClick, txt="Spelregels"))
        self.page.add(Button(500, 520, onClick = onCreditsClick, txt="Credits"))
        self.page.add(Button(500, 600, onClick = onPlayernameClick, txt = 'Spelernamen'))

    def draw(self):
       self.page.update()
       self.page.draw()
