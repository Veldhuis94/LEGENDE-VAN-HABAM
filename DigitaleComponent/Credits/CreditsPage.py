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
            print('here1')
        #page items
        self.backButton = Button(500, 600, onClick = onBackClick, txt = 'Terug')
        self.titleText = Text('Credits', 500,100,500,100, txtColor = (255,255,255),txtSize = 50)
        self.bodyText = Text('Ontwikkeld door:\nMahmoud Arab\nHakan Dalama\nAudi van Gog\nBastiaan te Veldhuis\n\nMet dank aan:\nAron van den Eng\nGert-Jan den Heijer\nAstrid van Duuren', 500,520,500,800, txtColor = (255,255,255),txtSize = 32)
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
