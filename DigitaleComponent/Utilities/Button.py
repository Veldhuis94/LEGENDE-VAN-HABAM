#Version 1.1.0
#-Added text color variables for different events (txtColorHover and txtColorPressed)
#-Event based colors will use the default color (ex: bgColorHover -> bgColor) if they are 'None' during initialisation
#-Added opacity support to all color variables
#-Button can be enabled or disabled. It's enabled on default.

#This class is a clickable object (has an event) and can be drawn on screen.
class Button:
    #Properties you can set with **args
    #[Size]
    w = 200 #width
    h = 40 #height
    
    #[Text]
    txt = "text" #text that gets displayed on the button
    txtSize = 32 #font size
    txtColor = (255, 255, 50) #Color of the text
    txtColorHover = None
    txtColorPressed = None
    
    #[Background]
    bgColor = (20, 20, 255) #default background color
    bgColorHover = (20, 255, 20) #background color when the user hovers on the button
    bgColorPressed = (255, 20, 20) #background color when the user clicks on the button
    radius = 5 #rounded cornors
    
    #[Button events]
    onClick = None #Is a event that runs every time a user clicks on this button. Type: function(Button = self)
    
    enabled = True #Onclick event will be fired and color will change based on input (hover, click)
    
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
        self.clicked = False 
        self.clickCount = 0 #Amount of times the user has clicked on the button
        
        #Extra arguments
        if(not(args==None)):
            self.__dict__.update(args)
                
        self.bgColorCurrent = self.bgColor #Current background color
        self.txtColorCurrent = self.txtColor
        
        self.bgColorHover = setToDefaultValueIfNone(self.bgColorHover, self.bgColor)
        self.bgColorPressed = setToDefaultValueIfNone(self.bgColorPressed, self.bgColor)
        
        self.txtColorHover = setToDefaultValueIfNone(self.txtColorHover, self.txtColor)
        self.txtColorPressed = setToDefaultValueIfNone(self.txtColorPressed, self.txtColor)
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
              
           textSize(self.txtSize)
           textAlign(CENTER, TOP)
           
           text(self.txt, self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)
    
    #Is a position/point (example: mouse cursor) in the area of the button?    
    def positionIsOnButton(self, x, y):
        left = self.x - self.w / 2
        right = self.x + self.w / 2
        top = self.y - self.h / 2
        bottom = self.y + self.h / 2
        
        return (x > left and x < right and y > top and y < bottom)
    
    #Run this on every frame.
    def update(self):
        mouseIsOnButton = self.positionIsOnButton(mouseX, mouseY)
        
        if(self.enabled and mouseIsOnButton):
            self.bgColorCurrent = self.bgColorHover
            self.txtColorCurrent = self.txtColorHover
            if(mousePressed and not self.clicked): #The user must release the mouse button before he/she can press on it again
                self.clicked = True
                self.bgColorCurrent = self.bgColorPressed
                self.txtColorCurrent = self.txtColorPressed
                if not(self.onClick == None):
                    self.clickCount += 1
                    self.onClick(self)
        else:
            self.bgColorCurrent = self.bgColor
            self.txtColorCurrent = self.txtColor
        if not(mousePressed):
            self.clicked = False
