#Made by Audi van Gog
from Utilities.Button import Button
import time

#Variables you are allowed to write
#button [Button], txt [string], placeHolder [string], textCursorTime [int], textCursorSign [string], allowedCharacters [set of strings], maxCharacters
class TextField:
    #Example usage: myTextField = TextField(100, 100) or TextField(100, 200, w=300, h=50)
    def __init__(self, x, y, **buttonArgs): #Constructor, this will be executed when you create an instance of this class
        self.selected = False
        self.button = Button(x, y, **buttonArgs)
        self.txt = ""
        self.placeHolder = "Fill in"
        self.textCursorTime = 500 #in milliseconds
        self.textCursorSign = "|"
        
        #See this link for the character encoding: https://www.rapidtables.com/code/text/unicode-characters.html
        self.allowedCharacters = {chr(i) for i in range(32, 127)} #spatie t/m [~]
        self.maxCharacters = 12
        
        self.previousKey = ""
    
    def setTextFieldArgs(**args):
        self.__dict__.update(args)
            
    def validKey(self, keyString):
        return keyString in self.allowedCharacters
    
    def update(self):
        if(mousePressed):
            if(self.button.positionIsOnButton(mouseX, mouseY)):
                self.selected = True
            else:
                self.selected = False
        
        if(self.selected and keyPressed and CODED): #CODED: heeft het gedrukte toets een keycode?
            currentKey = str(key)
            
            if(currentKey != self.previousKey): #You need to release it if you want to use the same key again
                if(currentKey == str(ESC)):
                    self.selected = False
                if(currentKey == str(BACKSPACE)): 
                    if(len(self.txt) > 0):
                        self.txt = self.txt[:-1] #Remove the last character
                elif(self.validKey(currentKey)):
                    self.txt += currentKey #Add an extra character
                    
                    if(len(self.txt) > self.maxCharacters): #The amount of characters should not exceed the maxCharacters amount
                        self.txt = self.txt[0:self.maxCharacters]
            self.previousKey = currentKey
        elif(keyPressed == False):
            self.previousKey = ""
                
    def draw(self):
        #Text value
        space = ""
        sign = ""
        
        currentTime = int(time.time() * 1000)
        if(self.selected and currentTime % self.textCursorTime * 2 < self.textCursorTime):
            sign = self.textCursorSign
            space = " "
        if(self.txt == ""): #Weergeef de placeholder tekst als het gevulde tekst leeg is
            self.button.txt = self.placeHolder
        else:
            self.button.txt = space + self.txt + sign

        #Text & Background color
        if(self.selected): #When selected
            self.button.bgColorCurrent = self.button.bgColorPressed
            self.button.txtColorCurrent = self.button.txtColorPressed
        elif(self.button.positionIsOnButton(mouseX, mouseY)): #if hovering
            self.button.bgColorCurrent = self.button.bgColorHover
            self.button.txtColorCurrent = self.button.txtColorHover
        else: #Default values
            self.button.bgColorCurrent = self.button.bgColor
            self.button.txtColorCurrent = self.button.txtColor

        self.button.draw() #Draw the button of the textfield
