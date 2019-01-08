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
    PHASE_GET_POWERPOINTS = 3
    PHASE_END = 4

    EFFECT_ADD_2PP = 1
    EFFECT_MUL_2PP = 2
    EFFECT_OUT_2DAYS = 4
    EFFECT_EXTRA_TRY = 14

    tiers = ["Low tier vijand", "Mid tier vijand", "High tier vijand", "Eindbaas"]

    RESPAWN_WAIT_TIME = 3 #in dagen
    RESPAWN_LESS_WAIT_TIME = 2

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

        playerPPDictOrig = dict() #powerpoints without effects
        playerPPDict = dict() #amount of powerpoints of each player [int per key]
        playerEyesDict = dict() #eyes of thrown dices per player [int array per key]
        playerTotalDict = dict() #Powerpoints + thrown eyes per player
        playerTotal = 0 #Sum of playerTotalDict

        playerPPStrings = ["", "", "", ""]

        for i in self.selectedPlayers:
            playerPPDictOrig[i] = self.getPlayerPowerpoints(i)
            playerEffects = self.effecten[i]
            if self.EFFECT_MUL_2PP in playerEffects and self.EFFECT_ADD_2PP in playerEffects:
                playerPPDict[i] = playerPPDictOrig[i] * 2 + 2
                playerPPStrings[i] = str(playerPPDictOrig[i]) + "k x 2 + 2 = " + str(playerPPDict[i]) + "k"
            elif self.EFFECT_MUL_2PP in playerEffects:
                playerPPDict[i] = playerPPDictOrig[i] * 2
                playerPPStrings[i] = str(playerPPDictOrig[i]) + "k x 2 = " + str(playerPPDict[i]) + "k"
            elif self.EFFECT_ADD_2PP in playerEffects:
                playerPPDict[i] = playerPPDictOrig[i] + 2
                playerPPStrings[i] = str(playerPPDictOrig[i]) + "k + 2 = " + str(playerPPDict[i]) + "k"
            else:
                playerPPDict[i] = playerPPDictOrig[i]
                playerPPStrings[i] = str(playerPPDict[i]) + "k"
            
            playerEyesDict[i] = [random.randint(1, 6) for _ in range(MAX_DICES_PLAYER)]
            playerTotalDict[i] = playerPPDict[i] + max(playerEyesDict[i]) #Get the highest thrown die + player powerpoints
            playerTotal += playerTotalDict[i]
        enemyPP = self.getEnemyPowerpoints(self.enemy)
        
        enemyDices = [random.randint(1,6) for _ in range(MAX_DICES_ENEMY)]
        enemyEyes = max(enemyDices)
        
        enemyTotal = enemyPP + enemyEyes
        
        resultText = ""
        self.backButton.enabled = True
        self.getPPButton.enabled = False
        if(playerTotal > enemyTotal): #GEWONNEN
            resultText = ["Je hebt gewonnen!", "Jullie hebben gewonnen!"][len(self.selectedPlayers) > 1]
            self.tellers.win_points += 1
            self.resetButton.enabled = False
            self.getPPButton.enabled = True
        elif(playerTotal < enemyTotal): #VERLOREN
            resultText = ["Je hebt verloren!", "Jullie hebben verloren!"][len(self.selectedPlayers) > 1]
            self.resetButton.enabled = True
            playersToRemove = set()
            for i in self.selectedPlayers:
                if self.getPlayerPowerpoints(i) >= 0:
                    self.setPlayerPowerpoints(i, self.getPlayerPowerpoints(i) - 1)
                if self.getPlayerPowerpoints(i) < 0:
                    if(self.EFFECT_EXTRA_TRY in self.effecten[i]):
                        self.effecten[i].remove(self.EFFECT_EXTRA_TRY) #Je mag het maar 1 keer gebruiken
                        self.setPlayerPowerpoints(i, 0)
                    else:
                        playerEffects = self.effecten[i]
                        if(self.EFFECT_OUT_2DAYS in playerEffects):
                            self.setPlayerPowerpoints(i, -self.RESPAWN_LESS_WAIT_TIME) #Met effectkaart 14 hoeft de speler maar 2 dagen te wachten
                        else:
                            self.setPlayerPowerpoints(i, -self.RESPAWN_WAIT_TIME) #De speler mag voor een paar dagen niet meedoen
                        playersToRemove.add(i)
            
            for i in playersToRemove:
                self.selectedPlayers.remove(i)

            if(len(self.selectedPlayers) == 0):
                self.backButton.enabled = True
                self.resetButton.enabled = False
        else: #GELIJKSPEL
            resultText = "Gelijkspel!"
            self.resetButton.enabled = True
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
            x = 960-500
            playerText = Text(self.playerNames[playerIndex] + " (" + playerPPStrings[playerIndex] + ")", x+100, y, 400, 64, txtSize=24, txtColor = (255,255,255))
            self.resultValuesPage.add(playerText)
            for dice in playerEyesDict[playerIndex]:
                img = self.files.getImage("dice"+str(dice))
                self.resultValuesPage.add(Image(img, x, y))
                x += 100
            y += 132
        
        for i in range(len(enemyDices)):
            img = self.files.getImage("dice"+str(enemyDices[i]))
            self.resultValuesPage.add(Image(img, 960 + 400 + 100 * i, 250))
        self.resultValuesPage.add(Text(self.tiers[self.enemy] + " (" + str(enemyPP) + ")", 960 + 400 + 100, 250, 400, 64, txtSize=24, txtColor = (255,255,255)))
            

    #throws dices for the players to get powerpoints      
    def throwForPowerpoints(self):
        playerLabelTemplate = Text("PLAYER NAME", 200, 200, 400, 100, txtSize=50)
        ppLabelTemplate = Text("+1k", 200, 500, 600, 100, txtSize=50)

        i = 0
        for playerIndex in self.selectedPlayers:
            dice = self.randomizer()
            x = 200 + 400 * i
            self.pages[self.PHASE_GET_POWERPOINTS].add(playerLabelTemplate.copy(x = x, txt=self.playerNames[playerIndex]))
            img = self.files.getImage("dice"+str(dice))
            self.pages[self.PHASE_GET_POWERPOINTS].add(Image(img, x, 400, True))
            if(dice >= 5): 
                pp = self.getPlayerPowerpoints(playerIndex) + 1 #Give an extra powerpoint to the player
                self.setPlayerPowerpoints(playerIndex, pp)
                self.pages[self.PHASE_GET_POWERPOINTS].add(ppLabelTemplate.copy(x = x))
            i += 1
        
        #pages[self.PHASE_GET_POWERPOINTS]

    #BattleSystem constructor
    def __init__(self, playerNames, tellers, files):
        self.pages = [Page() for i in range(self.PHASE_END+1)]
        self.resultValuesPage = Page()
        self.pages[self.PHASE_RESULT].add(self.resultValuesPage)
        self.playerNames = playerNames
        self.tellers = tellers
        self.files = files

        self.selectedPlayers = set() #Player index 0-3 (player 1 - 4)
        self.enemy = 0 #Enemy tier index 0-3 (low tier, mid tier, high tier, final boss)

        self.effecten = [set(), set(), set(), set()] #Effecten van verkregen effectkaarten van elk speler
        self.availableEffects = [[self.EFFECT_ADD_2PP, "+2k"], [self.EFFECT_MUL_2PP, "x2k"], [self.EFFECT_OUT_2DAYS, ""], [self.EFFECT_EXTRA_TRY, ""]]

        #----BUTTON EVENTS-----
        def onPlayerClick(button):
            self.player = button.playerIndex

            if(button.playerIndex in self.selectedPlayers):
                self.selectedPlayers.remove(button.playerIndex)
                button.bgColor = Button.bgColor
                button.bgColorCurrent = Button.bgColor
            else:
                self.selectedPlayers.add(button.playerIndex)
                button.bgColor = Button.bgColorHover
                button.bgColorCurrent = Button.bgColorHover
                
            self.playerNextButton.enabled = len(self.selectedPlayers) > 0
        
        def onEffectClick(button):
            player = button.playerIndex
            effect = button.effect

            if(effect in self.effecten[player]):
                self.effecten[player].remove(effect)
                button.bgColor = Button.bgColor
                button.bgColorCurrent = Button.bgColor
            else:
                self.effecten[player].add(effect)
                button.bgColor = Button.bgColorPressed
                button.bgColorCurrent = Button.bgColorPressed
                
        def onNextClick(button):
            if(len(self.selectedPlayers) > 0):
                if(len(self.selectedPlayers) > 1):
                    self.headers[self.PHASE_CHOOSE_ENEMY].txt = "Jullie vechten tegen..."
                else:
                    self.headers[self.PHASE_CHOOSE_ENEMY].txt = "Je vecht tegen..."
                self.phase = self.PHASE_CHOOSE_ENEMY
                print("effecten:",self.effecten)

        def onEnemyClick(button):
            self.phase = self.PHASE_RESULT
            self.enemy = button.enemyIndex
            self.fight()
        
        def onBackClick(button):
            self.phase = self.PHASE_END
        
        def onBackToPlayersClick(button):
            self.phase = self.PHASE_CHOOSE_PLAYER

        def onResetClick(button):
            self.fight()

        #If the user clicks on the button of this event, a page will be displayed where he/she can can throw a dice to get a powerpoint.
        def onGetPowerpointsClick(button): 
            self.phase = self.PHASE_GET_POWERPOINTS
            self.throwForPowerpoints() #Throw dices to get powerpoints and display the result
        #---------------------

        self.phase = self.PHASE_CHOOSE_PLAYER
        headerTemplate = Text("TEXT", 960, 160, 1200, 140, txtSize=70, txtColor = (255,255,255))
        self.headers = [ #Create labels to display a header on each page
            headerTemplate.copy(txt="Je bent/Jullie zijn..."),
            headerTemplate.copy(txt="Je vecht tegen..."),
            headerTemplate.copy(txt="RESULTAAT"),
            headerTemplate.copy(txt="Krijg krachtpunten")
        ]

        #Add the headers to the pages to update and display them
        for i in range(len(self.headers)):
            self.pages[i].add(self.headers[i])

        self.buttonTemplate = Button(0,0, w=360, h=50, txtSize = 40, radius = 3)
        unitButtonTemplate = self.buttonTemplate.copy(y=700)
        effectButtonTemplate = Button(0,unitButtonTemplate.y + 70, w=54, h=54, txtOffsetY=14, radius=50)

        heroImageFileNames = ["held1", "held2", "held3", "held4"]
        enemyImageFileNames = ["tier1", "tier2", "tier3", "tier4"]

        #Create buttons for choosing a player
        for i in range(self.getPlayerCount()): #for each player
            button = unitButtonTemplate.copy(x = i * 400 + 340, txt = self.playerNames[i], onClick=onPlayerClick)
            button.playerIndex = i
            button.enabled = self.getPlayerPowerpoints(i) >= 0
            self.pages[self.PHASE_CHOOSE_PLAYER].add(button)

            #Draw hero image
            heroImage = Image(self.files.getImage(heroImageFileNames[i]), button.x, button.y - 270, True)
            self.pages[self.PHASE_CHOOSE_PLAYER].add(heroImage)

            for j in range(len(self.availableEffects)): #for each effect
                effectButton = effectButtonTemplate.copy(x = button.x + 60 * j - 85, onClick=onEffectClick, playerIndex=i, effect=self.availableEffects[j][0], txt=self.availableEffects[j][1])
                effectButton.enabled = self.getPlayerPowerpoints(i) >= 0
                self.pages[self.PHASE_CHOOSE_PLAYER].add(effectButton)

                if(self.availableEffects[j][0] == self.EFFECT_OUT_2DAYS):
                    icon = Image(self.files.getImage("buitenspel_icon"), effectButton.x, effectButton.y, True)
                    self.pages[self.PHASE_CHOOSE_PLAYER].add(icon)
                if(self.availableEffects[j][0] == self.EFFECT_EXTRA_TRY):
                    icon = Image(self.files.getImage("extraLife"), effectButton.x, effectButton.y, True)
                    self.pages[self.PHASE_CHOOSE_PLAYER].add(icon)
                    
        

        #Create buttons for choosing an enemy
        for i in range(self.getEnemyTierCount()):
            button = unitButtonTemplate.copy(x = i * 400 + 340, txt = self.tiers[i], onClick=onEnemyClick)
            button.enemyIndex = i
            self.pages[self.PHASE_CHOOSE_ENEMY].add(button)

            #Draw enemy image
            enemyImage = Image(files.getImage(enemyImageFileNames[i]), button.x, button.y - 270, True)
            self.pages[self.PHASE_CHOOSE_ENEMY].add(enemyImage)
        
        self.playerNextButton = self.buttonTemplate.copy(x=960-300, y=850, txt="Volgende", onClick=onNextClick, enabled=False)
        self.pages[self.PHASE_CHOOSE_PLAYER].add(self.playerNextButton)

        #Reset button: fight again, Backbutton: resets the battlesystem (for now)
        self.resetButton = self.buttonTemplate.copy(x=960-300, y=850, txt = "Vecht opnieuw!", onClick=onResetClick)
        self.backButton = self.buttonTemplate.copy(x=960+300, y=850, txt = "Hoofdmenu", onClick=onBackClick)
        self.getPPButton = self.buttonTemplate.copy(x=960, y=910, w=600, txt = "Verkrijg krachtpunten", onClick=onGetPowerpointsClick)

        #Add those buttons to the result page
        self.pages[self.PHASE_RESULT].add(self.resetButton)
        self.pages[self.PHASE_RESULT].add(self.backButton)
        
        self.pages[self.PHASE_CHOOSE_PLAYER].add(self.backButton.copy(onClick = onBackClick))
        self.pages[self.PHASE_CHOOSE_ENEMY].add(self.backButton.copy(onClick = onBackToPlayersClick))

        self.pages[self.PHASE_RESULT].add(self.getPPButton)
        self.pages[self.PHASE_GET_POWERPOINTS].add(self.backButton.copy(onClick = onBackClick, x=960, y=910, w=600))
    #Code van hakan
    def randomizer(self):
        x=random.randint(1,6)
        return x
    #-----------------
    
    #Call this every frame
    def update(self):
        self.pages[self.phase].update()
    #Call this every frame
    def draw(self):
        self.pages[self.phase].draw()
