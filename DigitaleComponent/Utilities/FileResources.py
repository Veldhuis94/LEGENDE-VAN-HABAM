#Gemaakt door Audi van Gog

class FileResources:
    fonts = None
    images = None

    def __init__(self):
        self.fonts = dict()
        self.images = dict()

    def loadFontFile(self, path, key):
        font = loadFont(path)

        if(font == None):
            print("ERROR: Font with path '"+path+"' doesn't exists")
        else:
            self.fonts[key] = font
    
    def loadImageFile(self, path, key):
        image = loadImage(path)

        if(image == None):
            print("ERROR: Image with path '"+path+"' doesn't exists")
        else:
            self.images[key] = image

    def getFont(self, key):
        return self.fonts[key]
    
    def getImage(self, key):
        return self.images[key]