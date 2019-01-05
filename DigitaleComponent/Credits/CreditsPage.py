#gemaakt door Bastiaan
from Utilities.Button import Button
from Utilities.Page import Page
from Utilities.Text import Text

class Credits():
    PHASE_PAGE = 0
    def __init__(self):
        self.toMainMenu = False
        self.pages = [Page()]
        self.mainPage = Page()
        self.pages[0].add(self.mainPage)
        def onBackClick(button):
            self.toMainMenu = True
        #page items
        self.backButton = Button(960, 840, onClick = onBackClick, txt = 'Terug')
        self.titleText = Text('Credits', 960,150,960,150, txtColor = (255,255,255),txtSize = 100)
        self.bodyText = Text('de Legende van Habam -Digital Companion-\n(c) 2019 INF1C Groep 1\n\nOntwikkeld door:\nMahmoud Arab\nHakan Dalama\nAudi van Gog\nBastiaan te Veldhuis\n\nMet dank aan:\nAron van den Eng\nGert-Jan den Heijer\nAstrid van Duuren\n\nGemaakt met Python in Processing 3', 960,500,960,600, txtColor = (255,255,255),txtSize = 32)
        #to add items
        self.pages[0].add(self.backButton)
        self.pages[0].add(self.titleText)
        self.pages[0].add(self.bodyText)
    def update(self):
        self.pages[0].update()
    def draw(self):
        self.pages[0].draw()
    def pages():
        pass
    def phase():
        pass
