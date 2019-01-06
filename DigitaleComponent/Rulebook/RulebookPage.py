#gemaakt door Bastiaan
from Utilities.Button import Button
from Utilities.Page import Page
from Utilities.Text import Text
from Utilities.TextField import TextField

class Rulebook():

    PHASE_PAGE1 = 0
    PHASE_PAGE2 = 1
    def __init__(self):
        self.currentPage = 0
        self.toMainMenu = False
        self.pages = [Page(), Page(), Page(), Page(), Page(), Page(), Page(), Page(), Page()]
        self.page1 = Page()
        self.page2 = Page()
        self.page3 = Page()
        self.page4 = Page()
        self.page5 = Page()
        self.page6 = Page()
        self.page7 = Page()
        self.page8 = Page()
        self.page9 = Page()
        self.pages[0].add(self.page1)
        self.pages[1].add(self.page2)
        self.pages[2].add(self.page3)
        self.pages[3].add(self.page4)
        self.pages[4].add(self.page5)
        self.pages[5].add(self.page6)
        self.pages[6].add(self.page7)
        self.pages[7].add(self.page8)
        self.pages[8].add(self.page9)
        def onBackClick(button):
            self.toMainMenu = True
        def onNextClick(button):
            self.currentPage += 1
        def onPrevClick(button):
            self.currentPage -= 1
        #page items
        self.backButton = Button(960,900,onClick = onBackClick, txt = 'Terug')
        self.nextButton = Button(1200,900,onClick = onNextClick, txt = 'Volgende ->')
        self.prevButton = Button(720,900, onClick = onPrevClick, txt = '<- Vorige')
        self.titleText = Text("Spelregels", 960, 150, 500, 100, txtColor=(255,255,255), txtSize = 100)
        self.text1 = Text("Voorbereiding\n\nVoordat het spel kan beginnen moet het bord worden neergelegd. Het bord bestaat uit een frame en een aantal vierkante plaatjes. De plaatjes worden willekeurig in het frame gelegd. Dit is het uiteindelijke speelveld.\n\nVervolgens worden de spelerpionnen aan een kant van het speelveld gezet. Spelers mogen zelf kiezen op welk van de 7 beginvakjes ze gaan staan. Er mag maar 1 held op 1 vakje staan. Aan de andere kant van het speelveld komen de vijandige pionnen, 1 op elk vakje. Dit is de eerste vijandengolf.\n\nAls laatst mogen er drie fabrieken naar keuze worden neergezet op het speelveld. Let op: fabrieken leveren alleen iets op als ze op een met grondstof gemarkeerd veld staan.\n\nDe grondstof- stamina- en krachtpunten kunnen via de software bijgehouden worden. Het spel begint zonder grondstoffen en elke speler krijgt 2 krachtpunten en 7 staminapunten.", 960, 600, 800, 800, txtSize = 25)
        self.text2 = Text("Spelverloop\n\nDe spelers kunnen tijdens een beurt lopen, bouwen, verbeteren en vechten. Naast deze acties kan een speler ook ervoor kiezen om niets te doen. Alle acties kunnen in 1 dag uitgevoerd worden door elke speler. De spelers kunnen deze acties alleen overdag uitvoeren.\n\nLopen\nAls een speler gaat lopen met zijn pion, kost hem of haar dit 1 staminapunt per vakje. Als een speler geen stamina meer heeft kan deze niet meer lopen. Stamina kan worden bijgevuld door 1 eenheid graan te gebruiken uit de grondstoffen. (1 eenheid graan = 1 staminapunt)\n\nBouwen\nEen speler kan ervoor kiezen om 1 van de volgende dingen te bouwen: Fabriek, Muur, Brug, Straat, Warenhuis of Markt. Een gebouw kan alleen gebouwd worden op het vakje waar de bouwende speler op staat, met als uitzondering de Brug, die alleen op een watervak naast de bouwende speler gebouwd kan worden. Sommige gebouwen hebben meerdere soorten (tiers): Hout (goud), steen (zwart) of staal (blauw).", 960, 600, 800, 800, txtSize = 25)
        self.text3 = Text("Gebouwen\n\nFabriek\nEen fabriek zorgt voor grondstoffen. Er zijn twee verschillende soorten fabriek: een high tier fabriek en een low tier fabriek. Deze fabrieken leveren het volgende op:\nGraan\nLow tier - 1 keer het aantal spelers per dag\nHigh tier - 2 keer het aantal spelers per dag\nHout\nLow tier - 3 per 2 dagen\nHigh tier - 3 per dag\nSteen\nLow tier - 2 per 2 dagen\nHigh tier - 2 per dag\nStaal\nLow tier - 1 per 2 dagen\nHigh tier - 1 per dag\n\nEen low tier fabriek kost 2 hout en 1 steen. De vijand kan deze in 2 beurten vernietigen.\nEen high tier fabriek kost 3 hout, 2 steen en 1 staal. De vijand kan deze in 4 beurten vernietigen.\nDe fabrieken produceren de grondstof van het vakje waar ze op staan.\nJe kunt een fabriek verbeteren (ombouwen van low tier tot high tier) met 1 hout, 1 steen en 2 staal.", 960, 600, 8000, 800, txtSize = 25)
        self.text4 = Text("Gebouwen\n\nMuur\nEen muur kan gebouwd worden om vijanden tijdelijk tegen te houden. Er zijn houten, stenen en stalen muren. De kosten van de muur is 1 eenheid van de grondstof waar deze van wordt gebouwd. Een houten muur zorgt ervoor dat de vijand 1 beurt langer op het huidige vakje blijft, een stenen muur doet dit voor 2 beurten en een stalen muur 3 beurten. Wanneer deze beurten voorbij zijn, wordt de muur vernietigd. Een muur kan afgebroken worden, dit kost hetzelfde als een muur bouwen.\n\nBrug\nEen brug kan gebouwd worden om watervlakken over te kunnen steken. Een brug kost 2 van de desbetreffende grondstoffen. Er zijn houten, stenen en stalen bruggen. Een houten brug kan 2 keer gebruikt worden, een stenen brug 4 keer en een stalen brug 8 keer. Vijanden kunnen ook gebruik maken van de bruggen. Deze kan dan in 1 keer over een vakje water. Als een vijand over de brug gaat telt dit als 1 keer gebruikt. Nadat een brug is opgebruikt stort deze in. Een brug kan afgebroken worden, dit kost 1 eenheid van de desbetreffende grondstof.", 960, 600, 800, 800, txtSize = 25)
        self.text5 = Text("Gebouwen\n\nStraat\nEen straat kan gebouwd worden door 2 steen te gebruiken. Tegenstanders kunnen deze niet afbreken maar wel gebruiken. Als een speler over een vakje met een straat loopt kost dit geen stamina. Het afbreken van een straat kost 1 steen.\n\nWarenhuis\nEen warenhuis kan gebouwd worden om het aantal grondstoffen dat de spelers tegelijk in het bezit kan hebben te vergroten. Een warenhuis kan gebouwd worden door 3 hout te gebruiken. Een warenhuis kan verbeterd worden om meer voorwerpen vast te kunnen houden, dit kost 3 steen voor de eerste upgrade, en 3 staal voor de tweede upgrade. Aan het begin van het spel kunnen de spelers 10 grondstoffen bezitten. Een houten warenhuis heeft plaats voor 6 extra grondstoffen, een stenen warenhuis heeft plaats voor 10 extra grondstoffen, en een stalen warenhuis voor 14. Warenhuizen kunnen worden afgebroken met 2 eenheden van de grondstof waar ze van zijn gebouwd.\n\nMarkt\nEen markt kan gebouwd worden om effectkaarten en rugzakken te kopen. Een effectkaart kost 3 graan en een rugzak kost 3 steen. Een rugzak vergroot het aantal grondstoffen dat gehouden kan worden met 3. Er kan maar 1 rugzak worden gekocht. Met de markt kunnen 3 dezelfde grondstoffen geruild worden voor 1 andere grondstof. Een krachtpunt kan hier gekocht worden van 3 van elke grondstof. Een vijand heeft 3 beurten nodig om een markt te vernietigen.", 960, 600, 1100, 800, txtSize = 25)
        self.text6 = Text("Vechten\n\nAls een speler op hetzelfde vakje staat als een vijand kan de speler kiezen om aan te vallen. Spelers kunnen niet worden aangevallen door vijanden.\nBij het aanvallen worden dobbelstenen gebruikt om te bepalen wie er wint. De speler gooit 2 dobbelstenen. Een andere speler gooit voor de vijand. Het aantal dobbelstenen en krachtpunten wordt bepaald door de tier van de vijand. Als er gegooid is, wordt het hoogste aantal gegooide ogen opgeteld bij de krachtpunten. Wie dan het meeste punten heeft wint het gevecht. Je kunt ook met meerdere spelers 1 vijand aanvallen. In dat geval worden alle totale punten van de spelers bij elkaar opgeteld.\nIn de software kun je gebruikmaken van een automatisch gevechtssysteem.\n\nEr zijn vier verschillende tiers vijanden: Low-tier heeft 1 krachtpunt en 2 dobbelstenen, Mid-tier heeft 2 krachtpunten en 2 dobbelstenen, High tier heeft 4 krachtpunten en 3 dobbelstenen, en de eindbaas. De eindbaas heeft bij 2 spelers 6 krachtpunten, bij 3 spelers 12 en bij 4 spelers 18, gooit altijd met 3 dobbelstenen, en zet twee stappen per nacht.\n\nAls je een gevecht wint, krijg je een overwinningspunt. Deze punten bepalen welke vijanden op welk moment in het spel komen. Op de volgende pagina staat welke tier op welke plaats in het spel komt. Wanneer er vijf, tien, vijftien of twintig overwinningspunten behaald zijn begint er meteen een nieuwe golf. Alle nog levende vijanden blijven in het veld, met als uitzondering de eindbaasgolf, waarbij de nog levende vijanden uit het spel verwijderd worden.", 960, 600, 1000, 800, txtSize = 25)
        self.text7 = Text("Vechten\n\nVijandengolven:\n[L = Low-tier, M = Mid-tier, H = High-tier, E = Eindbaas]\nVanaf 0 overwinningspunten (begin van het spel):\nL, L, L, L, L, L, L\n\nVanaf 5 overwinningspunten:\nL, L, M, M, M, L, L\n\nVanaf 10 overwinningspunten:\nM, M, H, H, H, M, M\n\nVanaf 15 overwinningspunten:\nH, H, H, H, H, H, H\n\nVanaf 20 overwinningspunten:\n-, -, -, E, -, -, -", 960, 600, 800, 800, txtSize = 25)
        self.text8 = Text("Vechten\n\nGewonnen?\nDe vijand is verslagen en wordt uit het spel gehaald. De speler gooit 1 dobbelsteen. Als 5 of 6 wordt gegooid krijgt de speler een extra krachtpunt, anders gebeurt er niets. Elke vijand is 1 overwinningspunt waard.\n\nVerloren?\nDe speler is verslagen en verliest een krachtpunt. Als de speler geen krachtpunten meer heeft mag deze niet meer meedoen voor 3 dagen. Daarna begint deze aan het begin van het bord (bij het kasteel). De vijand blijft op het bord maar beweegt niet voor 1 nacht.\n\nGelijkspel?\nEr gebeurt niets en de speler kan opnieuw gooien of stoppen met de aanval.", 960, 600, 800, 800, txtSize = 25)
        self.text9 = Text("Spelverloop\n\nNacht\nAls iedere speler aan de beurt geweest is, is de dag voorbij en begint de nacht. In de nacht kunnen spelers geen acties meer uitvoeren en worden de volgende stappen ondernomen:\n1. Vijanden bewegen allemaal 1 stap naar voren.\n2. Er wordt een actiekaart gepakt en deze wordt uitgevoerd.\n3. De spelers krijgen grondstoffen.\n\nAfloop\nAls de spelers 20 overwinningspunten hebben bemachtigd worden alle vijanden van het bord gehaald en wordt de eindbaas op het bord gezet. Als de eindbaas verslagen is is het spel voorbij en hebben de spelers gewonnen.\nHet spel is verloren wanneer er 3 of meer reguliere (low- mid- of high-tier) vijanden het kasteel binnen zijn gedrongen. Het spel eindigt ook in verlies voor de spelers wanneer de eindbaas het kasteel bereikt.", 960, 600, 800, 800, txtSize = 25)
        #to add items
        for self.x in range(0,9):
            self.pages[self.x].add(self.titleText)
            self.pages[self.x].add(self.backButton)
            if self.x != 8:
                self.pages[self.x].add(self.nextButton)
            if self.x != 0:
                self.pages[self.x].add(self.prevButton)
        self.pages[0].add(self.text1)
        self.pages[1].add(self.text2)
        self.pages[2].add(self.text3)
        self.pages[3].add(self.text4)
        self.pages[4].add(self.text5)
        self.pages[5].add(self.text6)
        self.pages[6].add(self.text7)
        self.pages[7].add(self.text8)
        self.pages[8].add(self.text9)
    def update(self):
        self.pages[self.currentPage].update()
    def draw(self):
        self.pages[self.currentPage].draw()
    def pages():
        pass
    def phase():
        pass
