#made by Bastiaan
from CreditsPage import CreditsPage

creditsPage = CreditsPage()
def setup():
    size(1000,726)
    
def draw():
    global creditsPage
    clear()
    creditsPage.update()
    creditsPage.draw()
