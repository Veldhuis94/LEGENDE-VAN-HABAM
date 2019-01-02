#made by Bastiaan
import sys
sys.path.append('..')
from Utilities.Button import Button
from Utilities.Text import Text
from Utilities.Page import Page
from Utilities.Image import Image
from CreditsPage import CreditsPage

creditsPage = CreditsPage()
def setup(self):
    #fullScreen()
    #self.font=loadFont('BlackChancery-48.vlw')
    self.font=loadFont('BlackChancery.vlw')

    self.img=loadImage('TITLESCREEN2.png')
    # background(255,165,0)
    self.img.resize(1000, 726) #resize to the size of the screen
