import sys
sys.path.append('..')
from Utilities.Button import Button
from Utilities.Text import Text
from Utilities.Page import Page
from Utilities.Image import Image

class CreditsPage:
    page = Page()
    PHASE_SHOW = 0
    PHASE_END = 1
    def __init__(self):
        def onBackClick(button):
            self.phase = self.PHASE_END

        self.page.add(Text('Credits', 500, 100, 500, 100, txtColor=(255, 255, 255), txtSize = 50))
        self.backButton = Button(500,700, onClick = onBackClick, txt = "Terug")
        
        self.page[self.PHASE_SHOW].add(self.backButton)
            #Call this every frame
    def update(self):
        self.page[self.phase].update()
    #Call this every frame
    def draw(self):
        self.page[self.phase].draw()
