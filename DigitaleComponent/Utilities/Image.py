#Gemaakt door Audi
#Version 1.1
import copy
class Image:
    def __init__(self, processingImage, x, y):
        self.x = x
        self.y = y
        self.invisible = False
        self.imageRef = processingImage
    def copy(self):
        imageCopy = copy.deepcopy(self)
        return imageCopy
    def draw(self):
        if self.invisible == False and self.imageRef != None:
            image(self.imageRef, self.x, self.y)
