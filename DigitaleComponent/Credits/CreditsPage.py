import sys
import Credits
class CreditsPage:
    pages = [page1]
    PHASE_SHOW = 0
    PHASE_END = 1
    def __init__(self):
        def onBackClick(button):
            self.phase = self.PHASE_END

        self.page.add(Text('Credits', 500, 100, 500, 100, txtColor=(255, 255, 255), txtSize = 50))
        self.backButton = Button(500,700, onClick = onBackClick, txt = "Terug")
        
        
            #Call this every frame

    #Call this every frame
    def draw(self):
       self.page.update()
       self.page.draw()
