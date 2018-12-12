#Made by Audi van Gog
#comment
import random

import sys
sys.path.append('..') #Go one folder up to access the Utilities folder
from Utilities.Button import Button
from Utilities.Text import Text
from Utilities.Page import Page
import Dobbelstenen

class BattleSystem:
    #Constant values
    PHASE_CHOOSE_PLAYER = 0
    PHASE_CHOOSE_ENEMY = 1
    PHASE_RESULT = 2
    PHASE_END = 3
    
    player = 0 #Player index 0-3 (player 1 - 4)
    enemy = 0 #Enemy tier index 0-3 (low tier, mid tier, high tier, final boss)
    
    pages = [Page(), Page(), Page(), Page()]
    
    def getPlayerCount(self):
        return 4
    
    def getEnemyTierCount(self):
        return 4
    
    #index: 0-3 (speler 1-4)
    def getPlayerPowerpoints(self, i):
        ppList = [2, 2, 2, 2]
        return ppList[i]
    
    #index: 0-3 (tier 1-3 + final boss)
    def getEnemyPowerpoints(self, i):
        eindbaas = (self.getPlayerCount() - 1) * 6 #2 spelers: 6, 3: 12, 4: 18
        ppList = [1, 2, 4, eindbaas]
        return ppList[i]
    
    #Start the fight between the chosen player and the enemy
    def fight(self):
        playerPP = self.getPlayerPowerpoints(self.player)
        enemyPP = self.getEnemyPowerpoints(self.enemy)
        
        playerEyes = Dobbelstenen.randomizer()
        enemyEyes = Dobbelstenen.randomizer()
        
        playerTotal = playerPP + playerEyes
        enemyTotal = enemyPP + enemyEyes
        
        resultText = ""
        
        if(playerTotal > enemyTotal):
            print("You win!")
            resultText = "Je hebt gewonnen!"
        elif(playerTotal < enemyTotal):
            print("You lose!")
            resultText = "Je hebt verloren!"
        else:
            print("Tie!")
            resultText = "Gelijkspel!"
        self.headers[self.PHASE_RESULT].txt = resultText
        print("player pp:", playerPP, "enemy pp:", enemyPP, "playerEyes:", playerEyes, "enemyEyes:", enemyEyes, "playerTotal:", playerTotal, "enemyTotal:", enemyTotal)
        
        self.playerEyes = playerEyes
        self.enemyEyes = enemyEyes
        tiers = ["Low tier vijand", "Mid tier vijand", "High tier vijand", "Eindbaas"]
        self.playerText.txt = "Player " + str(self.player+1) + " (" + str(playerPP) + ")"
        self.enemyText.txt = tiers[self.enemy] + " (" + str(enemyPP) + ")"
                                                    
    #BattleSystem constructor
    def __init__(self):
        
        #----BUTTON EVENTS-----
        def onPlayerClick(button):
            self.phase = self.PHASE_CHOOSE_ENEMY
            self.player = button.playerIndex
        
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
        
        #Create buttons for choosing a player
        for i in range(self.getPlayerCount()):
            button = Button(i * 200 + 200, 500, w=150, h=40, txt = "Speler: " + str(i+1), txtSize = 24, onClick=onPlayerClick)
            button.playerIndex = i
            self.pages[self.PHASE_CHOOSE_PLAYER].add(button)
        
        #Create buttons for choosing an enemy
        for i in range(self.getEnemyTierCount()):
            tiers = ["Low tier vijand", "Mid tier vijand", "High tier vijand", "Eindbaas"]
            button = Button(i * 200 + 200, 500, w=150, h=40, txt = tiers[i], txtSize = 20, onClick=onEnemyClick)
            button.enemyIndex = i
            self.pages[self.PHASE_CHOOSE_ENEMY].add(button)
        
        #Reset button: fight again, Backbutton: resets the battlesystem (for now)
        resetButton = Button(300, 500, w=150, h=40, txt = "Vecht opnieuw!", txtSize = 20, onClick=onResetClick)
        backButton = Button(700, 500, w=150, h=40, txt = "Terug", txtSize = 20, onClick=onBackClick)
        
        #Add those buttons to the result page
        self.pages[self.PHASE_RESULT].add(resetButton)
        self.pages[self.PHASE_RESULT].add(backButton)
        
        self.playerText = Text("Speler", 300, 270, 200, 32, txtSize=16, txtColor = (255,255,255))
        self.enemyText = Text("Vijand", 700, 270, 200, 32, txtSize=16, txtColor = (255,255,255))
        self.pages[self.PHASE_RESULT].add(self.playerText)
        self.pages[self.PHASE_RESULT].add(self.enemyText)
    
    #Call this every frame
    def update(self):
        self.pages[self.phase].update()
    #Call this every frame
    def draw(self):
        self.pages[self.phase].draw()
        
        if(self.phase == self.PHASE_RESULT):
            Dobbelstenen.draw(250, 300, self.playerEyes)
            Dobbelstenen.draw(650, 300, self.enemyEyes)
