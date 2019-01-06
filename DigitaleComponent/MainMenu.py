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
            self.phase = AppPhase.RULEBOOK
        def onCreditsClick(button):
            self.phase = AppPhase.CREDITS
        def onPlayernameClick(button):
            self.phase = AppPhase.PLAYERNAMES
        def onMarketClick(button):
            self.phase = AppPhase.MARKET
        def onSpelverloopClick(button):
            self.phase = AppPhase.SPELVERLOOP
            
        buttonX = 960
        buttonY = 250
        buttonMarginY = 70
        buttonTemplate = Button(buttonX, buttonY, w=260, radius=3)
            
        self.page.add(Text("Hoofdmenu", 960, 150, 500, 100, txtColor=(255,255,255), txtSize = 100))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 0, onClick = onInventoryClick, txt="Inventaris"))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 1, onClick = onBattleSystemClick, txt="Gevecht"))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 2, onClick = onBoardRandomizerClick, txt="Bord randomizer"))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 3, onClick = onGameManualClick, txt="Spelregels"))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 4, onClick = onCreditsClick, txt="Credits"))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 5, onClick = onPlayernameClick, txt = 'Spelernamen'))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 6, onClick = onMarketClick, txt = 'Markt'))
        self.page.add(buttonTemplate.copy(y=buttonY + buttonMarginY * 7, onClick = onSpelverloopClick, txt = 'Spelverloop'))
    def draw(self):
       self.page.update()
       self.page.draw()
