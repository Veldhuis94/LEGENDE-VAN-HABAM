#Gemaakt door Hakan

import random

def randomizer():
    x=random.randint(1,6)
    return x

def setFaces(faces):
    global face
    face = faces
def draw(x, y, aantalOgen):
    global face
    photo=face[aantalOgen-1]
    
    image(photo,x,y)
