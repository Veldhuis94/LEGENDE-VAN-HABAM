#Made by Audi van Gog
#Version 1.0
#Updates and draws all items it contains
#The item needs to be from class that has a draw function. update is optional
class Page:
    def __init__(self):
        self.drawables = []

    #Update all items
    def update(self):
        for item in self.drawables:
            if hasattr(item, "update"): #Only update if the object has that function
                item.update()
    
    #Draw all items
    def draw(self):
        for item in self.drawables:
            item.draw()
            
    def add(self, item):
        self.drawables.append(item)
    
    #Empty the drawables list
    def clear(self):
        self.drawables = []
