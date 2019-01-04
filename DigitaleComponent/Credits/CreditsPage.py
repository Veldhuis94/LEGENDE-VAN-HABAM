#Made by Audi van Gog
import random

import sys
sys.path.append('..') #Go one folder up to access the Utilities folder
from Utilities.Button import Button
from Utilities.Text import Text
from Utilities.Page import Page
from Utilities.Image import Image
from Utilities.FileResources import FileResources
from tellers.tellers_class import tellers
#import Dobbelstenen

class BattleSystem:
    #Constant values
    PHASE_CHOOSE_PLAYER = 0
    PHASE_CHOOSE_ENEMY = 1
    PHASE_RESULT = 2
    PHASE_END = 3

    tiers = ["Low tier vijand", "Mid tier vijand", "High tier vijand", "Eindbaas"]

    def getPlayerCount(self):
        return 4
    
    def getEnemyTierCount(self):
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

    #index: 0-3 (tier 1-3 + final boss)
    def getEnemyPowerpoints(self, i):
        eindbaas = (self.getPlayerCount() - 1) * 6 #2 spelers: 6, 3: 12, 4: 18
        ppList = [1, 2, 4, eindbaas]
        return ppList[i]
        
    #Start the fight between the chosen player and the enemy
    def fight(self):
        MAX_DICES_PLAYER = 2
        MAX_DICES_ENEMY = 2

        playerPPDict = dict() #amount of powerpoints of each player [int per key]
        playerEyesDict = dict() #eyes of thrown dices per player [int array per key]
        playerTotalDict = dict() #Powerpoints + thrown eyes per player
        playerTotal = 0 #Sum of playerTotalDict

        for i in self.selectedPlayers:
            playerPPDict[i] = self.getPlayerPowerpoints(i)
            playerEyesDict[i] = [random.randint(1, 6) for _ in range(MAX_DICES_PLAYER)]
            playerTotalDict[i] = playerPPDict[i] + max(playerEyesDict[i]) #Get the highest thrown die + player powerpoints
            playerTotal += playerTotalDict[i]
        enemyPP = self.getEnemyPowerpoints(self.enemy)
        
        enemyDices = [random.randint(1,6) for _ in range(MAX_DICES_ENEMY)]
        enemyEyes = max(enemyDices)
        
        enemyTotal = enemyPP + enemyEyes
        
        resultText = ""
        
        if(playerTotal > enemyTotal):
            resultText = "Je hebt gewonnen!"
            self.tellers.win_points += 1
            self.backButton.enabled = True
        elif(playerTotal < enemyTotal):
            resultText = "Je hebt verloren!"
            self.backButton.enabled = True
            
            for i in self.selectedPlayers:
                self.setPlayerPowerpoints(i, self.getPlayerPowerpoints(i) - 1)
        else:
            resultText = "Gelijkspel!"
            self.backButton.enabled = False
        self.headers[self.PHASE_RESULT].txt = resultText
        
        print("---FIGHT---")
        print("playerPPDict",playerPPDict)
        print("playerEyesDict",playerEyesDict)
        print("playerTotalDict",playerTotalDict)
        print("playerTotal",playerTotal)
        print("enemyTotal",enemyTotal)

        self.resultValuesPage.clear()
        
        y = 250
        for playerIndex in playerEyesDict:
            x = 240
            playerText = Text("Speler "+str(playerIndex+1) + " (" + str(playerPPDict[playerIndex]) + ")", 300, y-8, 200, 32, txtSize=16, txtColor = (255,255,255))
            self.resultValuesPage.add(playerText)
            for dice in playerEyesDict[playerIndex]:
                img = self.files.getImage("dice"+str(dice)).copy()
                img.resize(50, 50)
                self.resultValuesPage.add(Image(img, x, y))
                x += 60
            y += 80
        
        for i in range(len(enemyDices)):
            img = self.files.getImage("dice"+str(enemyDices[i])).copy()
            img.resize(50, 50)
            self.resultValuesPage.add(Image(img, 580 + 60 * i, 250))
        self.resultValuesPage.add(Text(self.tiers[self.enemy] + " (" + str(enemyPP) + ")", 640, 250-8, 200, 32, txtSize=16, txtColor = (255,255,255)))
            

    #BattleSystem constructor
    def __init__(self):
        self.pages = [Page(), Page(), Page(), Page()]
        self.resultValuesPage = Page()
        self.pages[self.PHASE_RESULT].add(self.resultValuesPage)

        self.selectedPlayers = set() #Player index 0-3 (player 1 - 4)
        self.enemy = 0 #Enemy tier index 0-3 (low tier, mid tier, high tier, final boss)

        #----BUTTON EVENTS-----
        def onPlayerClick(button):
            self.player = button.playerIndex

            if(button.playerIndex in self.selectedPlayers):
                self.selectedPlayers.remove(button.playerIndex)
                button.txt = button.txt[:-1]
            else:
                self.selectedPlayers.add(button.playerIndex)
                button.txt += "<"
        def onNextClick(button):
            if(len(self.selectedPlayers) > 0):
                self.phase = self.PHASE_CHOOSE_ENEMY

        def onEnemyClick(button):
            self.phase = self.PHASE_RESULT
            self.enemy = button.enemyIndex
            self.fight()
        
        def onBackClick(button):
            self.phase = self.PHASE_END
        
        def onResetClick(button):
            self.fight()
        #---------------------
        
        
        self.phase = self.PHASE_CHOOSE_PLAYER
        self.headers = [ #Create labels to display a header on each page
            Text("Je bent..."       , 500, 200, 1000, 96, txtSize=48, txtColor = (255, 255, 255)),
            Text("Je vecht tegen...", 500, 200, 1000, 96, txtSize=48, txtColor = (255, 255, 255)),
            Text("RESULTAAT"        , 500, 200, 1000, 96, txtSize=48, txtColor = (255, 255, 255))
        ]
        
        #Add the headers to the pages to update and display them
        self.pages[self.PHASE_CHOOSE_PLAYER].add(self.headers[0])
        self.pages[self.PHASE_CHOOSE_ENEMY].add(self.headers[1])
        self.pages[self.PHASE_RESULT].add(self.headers[2])
        
        unitButtonTemplate = Button(200, 500, w=150, h=40)
        #Create buttons for choosing a player
        for i in range(self.getPlayerCount()):
            button = unitButtonTemplate.copy(x = i * 200 + 200, txt = "Speler: " + str(i+1), txtSize = 24, onClick=onPlayerClick)
            button.playerIndex = i
            self.pages[self.PHASE_CHOOSE_PLAYER].add(button)
        self.pages[self.PHASE_CHOOSE_PLAYER].add(Button(500, 600, txt="Volgende", w=150, h=40, txtSize=24, onClick=onNextClick))

        #Create buttons for choosing an enemy
        for i in range(self.getEnemyTierCount()):
            button = unitButtonTemplate.copy(x = i * 200 + 200, txt = self.tiers[i], txtSize = 20, onClick=onEnemyClick)
            button.enemyIndex = i
            self.pages[self.PHASE_CHOOSE_ENEMY].add(button)
        
        #Reset button: fight again, Backbutton: resets the battlesystem (for now)
        self.resetButton = Button(300, 600, w=150, h=40, txt = "Vecht opnieuw!", txtSize = 20, onClick=onResetClick)
        self.backButton = Button(700, 600, w=150, h=40, txt = "Terug", txtSize = 20, onClick=onBackClick)
        
        #Add those buttons to the result page
        self.pages[self.PHASE_RESULT].add(self.resetButton)
        self.pages[self.PHASE_RESULT].add(self.backButton)
        

    #Call this every frame
    def update(self):
        self.pages[self.phase].update()
    #Call this every frame
    def draw(self):
        self.pages[self.phase].draw()
