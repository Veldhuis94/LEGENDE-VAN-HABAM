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
        
        self.page.add(Text("Hoofdmenu", 500, 100, 500, 100, txtColor=(255,255,255), txtSize = 50)
        self.page.add(Button(500, 400, onClick = onInventoryClick, txt="Inventaris"))
        self.page.add(Button(500, 480, onClick = onBattleSystemClick, txt="Gevecht"))
       
    def draw(self):
       self.page.update()
       self.page.draw()
