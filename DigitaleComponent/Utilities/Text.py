#Made by Audi van Gog
#Version 1.0
#This class is used to display text on the screen
#Contains different style related values
class Text:
    txt = "text"
    txtSize = 32
    txtColor = (50, 50, 50, 255)
    
    def __init__(self, textValue, x, y, w, h, **args):
        self.txt = textValue
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        #Extra arguments
        if(not(args==None)):
            self.__dict__.update(args)
    def draw(self):
        def getAlpha(color):
            if(len(color) >= 4):
                return color[3]
            return 255
        
        opacity = getAlpha(self.txtColor)
        if opacity > 0:
           fill(self.txtColor[0], self.txtColor[1], self.txtColor[2], opacity)
              
           textSize(self.txtSize)
           textAlign(CENTER, TOP)
           
           text(self.txt, self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)
           
