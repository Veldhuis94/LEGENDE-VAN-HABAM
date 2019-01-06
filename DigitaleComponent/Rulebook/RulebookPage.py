#gemaakt door Bastiaan
from Utilities.Button import Button
from Utilities.Page import Page
from Utilities.Text import Text

class Rulebook():

    PHASE_PAGE1 = 0
    PHASE_PAGE2 = 1
    def __init__(self):
        self.currentPage = 0
        self.toMainMenu = False
        self.pages = [Page(), Page(), Page(), Page(), Page()]
        self.page1 = Page()
        self.page2 = Page()
        self.page3 = Page()
        self.page4 = Page()
        self.page5 = Page()
        self.pages[0].add(self.page1)
        self.pages[1].add(self.page2)
        self.pages[2].add(self.page3)
        self.pages[3].add(self.page4)
        self.pages[4].add(self.page5)
        def onBackClick(button):
            self.toMainMenu = True
        def onNextClick(button):
            self.currentPage += 1
        def onPrevClick(button):
            self.currentPage -= 1
        #page items
        self.backButton = Button(960,900,onClick = onBackClick, txt = 'Terug')
        self.nextButton = Button(1200,900,onClick = onNextClick, txt = 'Volgende')
        self.prevButton = Button(720,900, onClick = onPrevClick, txt = 'Vorige')
        self.titleText = Text("Spelregels", 960, 150, 500, 100, txtColor=(255,255,255), txtSize = 100)
        self.text1 = Text("Voorbereiding\n\nVoordat het spel kan beginnen moet het bord worden neergelegd. Het bord bestaat uit een frame en een aantal vierkante plaatjes. De plaatjes worden willekeurig in het frame gelegd. Dit is het uiteindelijke speelveld.\n\nVervolgens worden de spelerpionnen aan een kant van het speelveld gezet. Spelers mogen zelf kiezen op welk van de 7 beginvakjes ze gaan staan. Er mag maar 1 held op 1 vakje staan. Aan de andere kant van het speelveld komen de vijandige pionnen, 1 op elk vakje. Dit is de eerste vijandengolf.\n\nAls laatst mogen er drie fabrieken naar keuze worden neergezet op het speelveld. Let op: fabrieken leveren alleen iets op als ze op een met grondstof gemarkeerd veld staan.\n\nDe grondstof- stamina- en krachtpunten kunnen via de software bijgehouden worden. Het spel begint zonder grondstoffen en elke speler krijgt 2 krachtpunten en 7 staminapunten.", 960, 600, 800, 800, txtSize = 25)
        self.text2 = Text("Spelverloop\n\nDe spelers kunnen tijdens een beurt lopen, bouwen, verbeteren en vechten. Naast deze acties kan een speler ook ervoor kiezen om niets te doen. Alle acties kunnen in 1 dag uitgevoerd worden door elke speler. De spelers kunnen deze acties alleen overdag uitvoeren.\n\nLopen\nAls een speler gaat lopen met zijn pion, kost hem of haar dit 1 staminapunt per vakje. Als een speler geen stamina meer heeft kan deze niet meer lopen. Stamina kan worden bijgevuld door 1 eenheid graan te gebruiken uit de grondstoffen. (1 eenheid graan = 1 staminapunt)\n\nBouwen\nEen speler kan ervoor kiezen om 1 van de volgende dingen te bouwen: Fabriek, Muur, Brug, Straat, Warenhuis of Markt. Een gebouw kan alleen gebouwd worden op het vakje waar de bouwende speler op staat, met als uitzondering de Brug, die alleen op een watervak naast de bouwende speler gebouwd kan worden. Sommige gebouwen hebben meerdere soorten (tiers): Hout (goud), steen (zwart) of staal (blauw).", 960, 600, 800, 800, txtSize = 25)
        self.text3 = Text("Gebouwen\n\nFabriek\nEen fabriek zorgt voor grondstoffen. Er zijn twee verschillende soorten fabriek: een high tier fabriek en een low tier fabriek. Deze fabrieken leveren het volgende op:\nGraan\nLow tier - 1 keer het aantal spelers per dag\nHigh tier - 2 keer het aantal spelers per dag\nHout\nLow tier - 3 per 2 dagen\nHigh tier - 3 per dag\nSteen\nLow tier - 2 per 2 dagen\nHigh tier - 2 per dag\nStaal\nLow tier - 1 per 2 dagen\nHigh tier - 1 per dag\n\nEen low tier fabriek kost 2 hout en 1 steen. De vijand kan deze in 2 beurten vernietigen.\nEen high tier fabriek kost 3 hout, 2 steen en 1 staal. De vijand kan deze in 4 beurten vernietigen.\nDe fabrieken produceren de grondstof van het vakje waar ze op staan.", 960, 600, 8000, 800, txtSize = 25)
        self.text4 = Text("Gebouwen\n\nMuur\nEen muur kan gebouwd worden om vijanden tijdelijk tegen te houden. Er zijn houten, stenen en stalen muren. De kosten van de muur is 1 eenheid van de grondstof waar deze van wordt gebouwd. Een houten muur zorgt ervoor dat de vijand 1 beurt langer op het huidige vakje blijft, een stenen muur doet dit voor 2 beurten en een stalen muur 3 beurten. Wanneer deze beurten voorbij zijn, wordt de muur vernietigd. Een muur kan afgebroken worden, dit kost hetzelfde als een muur bouwen.\n\nBrug\nEen brug kan gebouwd worden om watervlakken over te kunnen steken. Een brug kost 2 van de desbetreffende grondstoffen. Er zijn houten, stenen en stalen bruggen. Een houten brug kan 2 keer gebruikt worden, een stenen brug 4 keer en een stalen brug 8 keer. Vijanden kunnen ook gebruik maken van de bruggen. Deze kan dan in 1 keer over een vakje water. Als een vijand over de brug gaat telt dit als 1 keer gebruikt. Nadat een brug is opgebruikt stort deze in. Een brug kan afgebroken worden, dit kost 1 eenheid van de desbetreffende grondstof.", 960, 600, 800, 800, txtSize = 25)
        self.text5 = Text("Gebouwen\n\nStraat\nEen straat kan gebouwd worden door 2 steen te gebruiken. Tegenstanders kunnen deze niet afbreken maar wel gebruiken. Als een speler over een vakje met een straat loopt kost dit geen stamina. Het afbreken van een straat kost 1 steen.\n\nWarenhuis\nEen warenhuis kan gebouwd worden om het aantal grondstoffen dat de spelers tegelijk in het bezit kan hebben te vergroten. Een warenhuis kan gebouwd worden door 3 hout te gebruiken. Een warenhuis kan verbeterd worden om meer voorwerpen vast te kunnen houden, dit kost 3 steen voor de eerste upgrade, en 3 staal voor de tweede upgrade. Aan het begin van het spel kunnen de spelers 10 grondstoffen bezitten. Een houten warenhuis heeft plaats voor 6 extra grondstoffen, een stenen warenhuis heeft plaats voor 10 extra grondstoffen, en een stalen warenhuis voor 14.\n\nMarkt\nEen markt kan gebouwd worden om effectkaarten en rugzakken te kopen. Een effectkaart kost 3 graan en een rugzak kost 3 steen. Een rugzak vergroot het aantal grondstoffen dat gehouden kan worden met 3. Er kan maar 1 rugzak worden gekocht. Met de markt kunnen 3 dezelfde grondstoffen geruild worden voor 1 andere grondstof. Een krachtpunt kan hier gekocht worden van 3 van elke grondstof. Een vijand heeft 3 beurten nodig om een markt te vernietigen.", 960, 600, 1000, 800, txtSize = 25)
        #to add items
        self.pages[0].add(self.titleText)
        self.pages[1].add(self.titleText)
        self.pages[2].add(self.titleText)
        self.pages[3].add(self.titleText)
        self.pages[4].add(self.titleText)
        self.pages[0].add(self.backButton)
        self.pages[1].add(self.backButton)
        self.pages[2].add(self.backButton)
        self.pages[3].add(self.backButton)
        self.pages[4].add(self.backButton)
        self.pages[0].add(self.nextButton)
        self.pages[1].add(self.nextButton)
        self.pages[2].add(self.nextButton)
        self.pages[3].add(self.nextButton)
        self.pages[1].add(self.prevButton)
        self.pages[2].add(self.prevButton)
        self.pages[3].add(self.prevButton)
        self.pages[4].add(self.prevButton)
        self.pages[0].add(self.text1)
        self.pages[1].add(self.text2)
        self.pages[2].add(self.text3)
        self.pages[3].add(self.text4)
        self.pages[4].add(self.text5)
    def update(self):
        self.pages[self.currentPage].update()
    def draw(self):
        self.pages[self.currentPage].draw()
    def pages():
        pass
    def phase():
        pass
