#Made by Audi van Gog
import sys
sys.path.append('..') #Go one folder up to access the Utilities folder

from Utilities.Page import Page
from Utilities.Button import Button
from Utilities.Text import Text
from Turn import Turn

class SpelverloopUI:
    TURN_COLOR_DEFAULT = (255, 255, 255)
    TURN_COLOR_CURRENT = (10, 10, 255)

    def __init__(self, spelverloop):
        self.spelverloop = spelverloop
        self.page = Page()
        self.page.add(Text("Spelverloop", 500, 100, 500, 80, txtSize=40, txtColor = (255,255,255))) #header
        self.currentDayText = Text("Dag 1", 500, 140, 500, 80, txtSize=32, txtColor = (240, 240, 240))
        self.page.add(self.currentDayText)

        self.goBackToMainMenu = False

        def onNextTurnClick(button):
            self.spelverloop.nextTurn()
        def onBackClick(button):
            self.goBackToMainMenu = True

        self.page.add(Button(500, 500, txt="Volgende beurt", onClick = onNextTurnClick))
        self.page.add(Button(500, 600, txt="Terug", onClick = onBackClick))

        
        self.turnLabelValues = {
            Turn.PLAYER_1: "Speler 1",
            Turn.PLAYER_2: "Speler 2",
            Turn.PLAYER_3: "Speler 3",
            Turn.PLAYER_4: "Speler 4",
            Turn.ACTIONCARD: "Pak een\nactiekaart",
            Turn.ENEMIES: "Tegenstanders\n gaan vooruit",
            Turn.GET_GRAIN: "Krijg\n graan",
            Turn.GET_RESOURCES: "Krijg\n resources"
        }

        self.turnLabels = [Text(self.turnLabelValues[i], 100 + 120 * i, 300, 200, 50, txtSize=20, txtColor=(self.TURN_COLOR_DEFAULT)) for i in range(Turn.END)]

        for label in self.turnLabels:
            self.page.add(label)
    def draw(self):
        for i in range(len(self.turnLabels)):
            if(i == self.spelverloop.currentTurn):
                self.turnLabels[i].txtColor = self.TURN_COLOR_CURRENT
            else:
                self.turnLabels[i].txtColor = self.TURN_COLOR_DEFAULT
        self.currentDayText.txt = "Dag " + str(self.spelverloop.currentDay)
        self.page.update()
        self.page.draw()
