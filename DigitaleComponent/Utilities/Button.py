#Made by Audi van Gog
#Version 1.3.0
import copy

#This class is a clickable object (has an event) and can be drawn on screen.
class Button:
    #Properties you can set with **args
    #[Size]
    w = 200 #width
    h = 40 #height
    
    #[Text]
    txt = "text" #text that gets displayed on the button
    txtSize = 32 #font size
    txtOffsetX = 0
    txtOffsetY = 5
    txtColor = (255, 254, 50) #Color of the text
    txtColorHover = None
    txtColorPressed = None
    txtColorDisabled = (100, 100, 100)
    txtFont = None
    static_defaultFont = None

    #[Background]
    bgColor = (255, 148, 0) #default background color
    bgColorHover = (255, 188, 96) #background color when the user hovers on the button
    bgColorPressed = (96, 183, 255) #background color when the user clicks on the button
    bgColorDisabled = (155, 77, 4)
    radius = 5 #rounded cornors
    
    #[Button events]
    onClick = None #Is a event that runs every time a user clicks on this button. Type: function(Button = self)
    
    enabled = True #Onclick event will be fired and color will change based on input (hover, click)

    static_clicked = False

    @staticmethod
    def setDefaultFont(font):
        Button.static_defaultFont = font

    #Constructor of the Button, use this to initialise the button. Example usage: myButton = Button(100, 100, w = 100, h = 50, txt='click here')
    def __init__(self, x, y, **args):

        #----------------------
        def setToDefaultValueIfNone(value, defaultValue):
            if(value == None):
                value = defaultValue
            return value
        #----------------------
        
        #set the button position
        self.x = x
        self.y = y
        
        self.onClick = Button.onClickDefault 
        self.clicked = True 
        self.clickCount = 0 #Amount of times the user has clicked on the button

        #Extra arguments
        if(not(args==None)):
            self.__dict__.update(args)
                
        self.bgColorCurrent = self.bgColor #Current background color
        self.txtColorCurrent = self.txtColor
        
        self.bgColorHover = setToDefaultValueIfNone(self.bgColorHover, self.bgColor)
        self.bgColorPressed = setToDefaultValueIfNone(self.bgColorPressed, self.bgColor)
        self.bgColorDisabled = setToDefaultValueIfNone(self.bgColorDisabled, self.bgColor)

        self.txtColorHover = setToDefaultValueIfNone(self.txtColorHover, self.txtColor)
        self.txtColorPressed = setToDefaultValueIfNone(self.txtColorPressed, self.txtColor)
        self.txtColorDisabled = setToDefaultValueIfNone(self.txtColorDisabled, self.txtColor)

    #Make a copy of this button and return the copy.
    #Example: myButton.copy(), myButton.copy(x = 5, y = 3)
    def copy(self, **args):
        buttonCopy = copy.deepcopy(self)

        buttonCopy.onClick = Button.onClickDefault 
        buttonCopy.clicked = True 
        buttonCopy.clickCount = 0 #Amount of times the user has clicked on the button

        if(not(args==None)):
            buttonCopy.__dict__.update(args)
        return buttonCopy

    #Default onclick event
    def onClickDefault(button):
        print("click", button.clickCount)
    
    #draw the button
    def draw(self):
        def getAlpha(color):
            if(len(color) >= 4):
                return color[3]
            return 255
        
        #Button background
        opacity = getAlpha(self.bgColorCurrent)
        
        if opacity > 0: #If it's 0 or under, don't try to render it, it's going to be invisible anyways
           fill(self.bgColorCurrent[0], self.bgColorCurrent[1], self.bgColorCurrent[2], opacity)
           
           #the rectangle must be on the center of the button
           rect(self.x - self.w / 2, self.y - self.h / 2, self.w, self.h, self.radius)
        
        #Text
        opacity = getAlpha(self.txtColorCurrent)
        if opacity > 0:
            fill(self.txtColorCurrent[0], self.txtColorCurrent[1], self.txtColorCurrent[2], opacity)
            
            if(self.txtFont != None):
                textFont(self.txtFont)
            elif(Button.static_defaultFont != None):
                textFont(Button.static_defaultFont)
            textSize(self.txtSize)
            textAlign(CENTER, TOP)
            
            text(self.txt, self.x - self.w / 2 + self.txtOffsetX, self.y - self.h / 2 + self.txtOffsetY, self.w, self.h)
    
    #Is a position/point (example: mouse cursor) in the area of the button?    
    def positionIsOnButton(self, x, y):
        left = self.x - self.w / 2
        right = self.x + self.w / 2
        top = self.y - self.h / 2
        bottom = self.y + self.h / 2
        
        return (x > left and x < right and y > top and y < bottom)
    
    def isClicked(self):
        return self.clicked and self.clickCount > 0

    #Run this on every frame.
    def update(self):
        #Prevent the user can click on multiple buttons simultaniously
        if(Button.static_clicked==True):
            if(mousePressed == False):
                Button.static_clicked=False
            else:
                return #Don't run the rest of the function
            

        mouseIsOnButton = self.positionIsOnButton(mouseX, mouseY)
        
        if(self.enabled and mouseIsOnButton):
            self.bgColorCurrent = self.bgColorHover
            self.txtColorCurrent = self.txtColorHover
            
            if(mousePressed and self.clicked == False): #The user must release the mouse button before he/she can press on it again
                Button.static_clicked=True
                self.clicked = True
                self.bgColorCurrent = self.bgColorPressed
                self.txtColorCurrent = self.txtColorPressed
                if not(self.onClick == None):
                    self.clickCount += 1
                    self.onClick(self)
        else:
            if(not(self.enabled)): #If the button has been disabled...
                self.bgColorCurrent = self.bgColorDisabled
                self.txtColorCurrent = self.txtColorDisabled
            else:
                self.bgColorCurrent = self.bgColor
                self.txtColorCurrent = self.txtColor
        if not(mousePressed):
            self.clicked = False
