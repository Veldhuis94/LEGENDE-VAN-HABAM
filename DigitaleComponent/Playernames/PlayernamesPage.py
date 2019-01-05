#gemaakt door Bastiaan
from Utilities.Button import Button
from Utilities.Page import Page
from Utilities.Text import Text
from Utilities.TextField import TextField

class Playernames():
    PHASE_PAGE = 0
    PHASE_END = 1
    def __init__(self):
        self.toMainMenu = False
        self.pages = [Page()]
        self.mainPage = Page()
        self.pages[0].add(self.mainPage)
        def onBackClick(button):
            self.toMainMenu = True
        #page items
        self.backButton = Button(960, 700, onClick = onBackClick, txt = 'Terug')
        self.titleText = Text("Spelernamen", 960, 150, 960, 150, txtColor=(255,255,255), txtSize = 100)
        self.p1name = TextField(960,300, placeHolder = 'Speler 1')
        self.p2name = TextField(960,380, placeHolder = 'Speler 2')
        self.p3name = TextField(960,460, placeHolder = 'Speler 3')
        self.p4name = TextField(960,540, placeHolder = 'Speler 4')
        #to add items
        self.pages[0].add(self.backButton)
        self.pages[0].add(self.titleText)
        self.pages[0].add(self.p1name)
        self.pages[0].add(self.p2name)
        self.pages[0].add(self.p3name)
        self.pages[0].add(self.p4name)
    #Call this every frame
    def update(self):
        self.pages[0].update()
        self.p1 = self.p1name.txt
        self.p2 = self.p2name.txt
        self.p3 = self.p3name.txt
        self.p4 = self.p4name.txt
    #Call this every frame
    def draw(self):
        self.pages[0].draw()
    def pages():
        return None
    def phase():
        return None
    def sendBack(self):
        return [self.p1, self.p2, self.p3, self.p4]
