#gemaakt door Bastiaan

import random

leftAction = []
leftEffect = []

def cards(type): 
    '''type must be 'action' or 'effect'!'''
    found = False
    global leftAction
    global leftEffect
    
    while not found:
        res = random.randint(0,20)
        if type == 'action':
            if len(leftAction) == 20:
                leftAction = []
            if not res in leftAction:
                leftAction.append(res)
                found = True
                return res
        elif type == 'effect':
            if len(leftEffect) == 20:
                leftEffect = []
            if not res in leftEffect:
                leftEffect.append(res)
                found = True
                return res
        else:
            raise valueError("type should be 'action' or 'effect'!!")
            break
