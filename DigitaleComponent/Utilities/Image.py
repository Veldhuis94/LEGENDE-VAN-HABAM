#Gemaakt door Audi
#Version 1.1
import copy
class Image:
    def __init__(self, processingImage, x, y, centered=False):
        self.x = x
        self.y = y
        self.invisible = False
        self.imageRef = processingImage
        self.centered = centered
    def copy(self):
        imageCopy = copy.deepcopy(self)
        return imageCopy
    def getWidth(self):
        if self.imageRef != None:
            return self.imageRef.width
        return 0
    def getHeight(self):
        if self.imageRef != None:
            return self.imageRef.height
        return 0
    def draw(self):
        if self.invisible == False and self.imageRef != None:
            if self.centered == True:
                w = self.getWidth()
                h = self.getHeight()
                image(self.imageRef, self.x - w//2, self.y - h//2)
            else:
                image(self.imageRef, self.x, self.y)
