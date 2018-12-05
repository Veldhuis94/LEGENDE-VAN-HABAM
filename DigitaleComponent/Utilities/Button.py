class Button:
    #Properties you can set with **args
    #[Size]
    w = 200 #width
    h = 40 #height
    
    #[Text]
    txt = "text" #text that gets displayed on the button
    txtSize = 32 #font size
    txtColor = (255, 255, 50) #Color of the text
    
    #[Background]
    bgColor = (20, 20, 255) #default background color
    bgColorHover = (20, 255, 20) #background color when the user hovers on the button
    bgColorPressed = (255, 20, 20) #background color when the user clicks on the button
    radius = 5 #rounded cornors
    
    #[Button events]
    onClick = None #Is a event that runs every time a user clicks on this button. Type: function(Button = self)
    
    #Constructor of the Button, use this to initialise the button. Example usage: myButton = Button(100, 100, w = 100, h = 50, txt='click here')
    def __init__(self, x, y, **args):
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
    
    #Default onclick event
    def onClickDefault(button):
        print("click", button.clickCount)
    
    #draw the button
    def draw(self):
        #Button background
        fill(self.bgColorCurrent[0], self.bgColorCurrent[1], self.bgColorCurrent[2])
        #the rectangle must be on the center of the button
        rect(self.x - self.w / 2, self.y - self.h / 2, self.w, self.h, self.radius)
        
        #Text
        fill(self.txtColor[0], self.txtColor[1], self.txtColor[2])
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
        
        if(mouseIsOnButton):
            self.bgColorCurrent = self.bgColorHover
            if(mousePressed and not self.clicked): #The user must release the mouse button before he/she can press on it again
                self.clicked = True
                self.bgColorCurrent = self.bgColorPressed
                if not(self.onClick == None):
                    self.clickCount += 1
                    self.onClick(self)
        else:
            self.bgColorCurrent = self.bgColor

        if not(mousePressed):
            self.clicked = False
