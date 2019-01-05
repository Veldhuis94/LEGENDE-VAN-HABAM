#Made by Audi van Gog
#Version 1.1
#-Added copy function
#-Added font type variable

#Version 1.0
#This class is used to display text on the screen
#Contains different style related values
import copy

class Text:
    txt = "text"
    txtSize = 32
    txtColor = (255,255,255,255)
    txtFont = None
    static_defaultFont = None

    def __init__(self, textValue, x, y, w, h, **args):
        self.txt = textValue
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        #Extra arguments
        if(not(args==None)):
            self.__dict__.update(args)
    
    def copy(self, **args):
        textCopy = copy.deepcopy(self)

        if(not(args==None)):
            textCopy.__dict__.update(args)
        return textCopy

    def draw(self):
        def getAlpha(color):
            if(len(color) >= 4):
                return color[3]
            return 255
        
        opacity = getAlpha(self.txtColor)
        if opacity > 0:
            fill(self.txtColor[0], self.txtColor[1], self.txtColor[2], opacity)
            
            if(self.txtFont != None):
                textFont(self.txtFont)
            elif(Text.static_defaultFont != None):
                textFont(Text.static_defaultFont)

            textSize(self.txtSize)
            textAlign(CENTER, TOP)
            
            text(self.txt, self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)
           
