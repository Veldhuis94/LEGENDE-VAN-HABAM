#gemaakt door Bastiaan

import random

leftAction = []
leftEffect = []

def cards(cardType): 
    '''cardType must be 'action' or 'effect'!'''
    found = False
    global leftAction
    global leftEffect
    
    while not found:
        res = random.randint(0,20)
        if cardType == 'action':
            if len(leftAction) == 20:
                leftAction = [11]
            if not res in leftAction:
                leftAction.append(res)
                found = True
                return res
        elif cardType == 'effect':
            if len(leftEffect) == 20:
                leftEffect = []
            if not res in leftEffect:
                leftEffect.append(res)
                found = True
                return res
        else:
            raise ValueError("cardType should be 'action' or 'effect'!!")
            break