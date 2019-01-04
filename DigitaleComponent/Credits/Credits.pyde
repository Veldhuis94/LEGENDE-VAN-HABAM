#Made by Audi van Gog en Hakan
from CreditsPage import CreditsPage
#import Dobbelstenen

creditsPage = CreditsPage()
def setup():
    size(1000, 726)

    
def draw():
    global creditsPage
    clear()
    
    if(creditsPage.phase == creditsPage.PHASE_END):
        c = CreditsPage() #Start het gevechtssysteem opnieuw op
    else:
        creditsPage.update()
        creditsPage.draw()
