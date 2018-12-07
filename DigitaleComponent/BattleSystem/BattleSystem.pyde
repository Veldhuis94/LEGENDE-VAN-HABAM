#Made by Audi van Gog
from BattleSystem import BattleSystem

battleSystem = BattleSystem()
def setup():
    size(1000, 726)
def draw():
    global battleSystem
    clear()
    
    if(battleSystem.phase == battleSystem.PHASE_END):
        battleSystem = BattleSystem() #Start het gevechtssysteem opnieuw op
    else:
        battleSystem.update()
        battleSystem.draw()
