#Made by Audi van Gog
from Turn import Turn

class Spelverloop:
    POWERPOINTS_ON_RESPAWN = 1
    def __init__(self, tellers):
        self.currentTurn = Turn.PLAYER_1
        self.currentDay = 1
        self.tellers = tellers
        self.processPlayerTurns()

    def getPlayerCount(self):
        return 4

    #index: 0-3 (speler 1-4)
    def getPlayerPowerpoints(self, i):
        ppList = [self.tellers.power1, self.tellers.power2, self.tellers.power3, self.tellers.power4]
        return ppList[i]
    
    def setPlayerPowerpoints(self, i, value):
        if(i == 0):
            self.tellers.power1 = value
        elif(i == 1):
            self.tellers.power2 = value
        elif(i == 2):
            self.tellers.power3 = value
        elif(i == 3):
            self.tellers.power4 = value
        else:
            print("Error: invalid index, value: " + str(i))

    def processPlayerTurns(self):
        while(Turn.isPlayerTurn(self.currentTurn)):
            playerIndex = Turn.turnToPlayerIndex(self.currentTurn)
            powerpoints = self.getPlayerPowerpoints(playerIndex)

            if(powerpoints >= 0):
                break
            else: #Als het aantal krachtpunten negatief is... (= aantal dagen dat de speler moet wachten)
                self.currentTurn += 1 #Sla de beurt van een speler over
                print("skip player's turn")
    def nextTurn(self):
        #Volgende beurt
        self.currentTurn += 1

        self.processPlayerTurns()
        
        
        if(self.currentTurn == Turn.GET_RESOURCES): #Je krijgt alleen om de 2 dagen resources
            if(self.currentDay % 2 == 0):
                pass #Voor nu moeten de spelers handmatig resources toevoegen bij de tellers
            else:
                self.currentTurn += 1
            
        
        if(self.currentTurn >= Turn.END):
            for playerIndex in range(self.getPlayerCount()):
                powerpoints = self.getPlayerPowerpoints(playerIndex)
                if(powerpoints < 0): #negatieve aantal krachtpunten = hoeveel dagen de speler moet wachten voordat hij/zij weer mag meedoen.
                    powerpoints += 1
                    
                    if(powerpoints == 0):
                        powerpoints = self.POWERPOINTS_ON_RESPAWN #Speler mag weer meedoen
                    self.setPlayerPowerpoints(playerIndex, powerpoints)

            self.currentDay += 1
            self.currentTurn = Turn.PLAYER_1
            self.processPlayerTurns()
        
