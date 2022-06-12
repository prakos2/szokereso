import pygame as pg
import Eszkozok

# Globális változók
_gomb_lenyomva = False # Bármely egérgomb lenyomva
FELBONTAS = () # A teljes képernyő felbontása, inicializáláskor kap értéket

# Ablakkomponensek

class Ablakkomponens():
    def __init__(self, pozicio = (0,0), dimenziok = (0,0), latszik = True):
        if (type(pozicio) == tuple and len(pozicio) == 2) and (type(dimenziok) == tuple and len(dimenziok) == 2):
            self.pozicio = pozicio
            self.dimenziok = dimenziok
        else:
            print("[F] [Ablakvezerlo] A megadott koordinátaértékekben hibák találhatóak. Helyes szintaxis: tuple (x, y)")
        self.latszik = latszik

    def s_latszik(self, ertek):
        '''
        Megváltoztatja egy elem láthatóságát
        '''
        if ertek != self.latszik:
            self.latszik = ertek
    
    def g_latszik(self):
        '''
        Látható-e az elem?
        '''
        return self.latszik

    def rajzol(self, pg_felulet):
        '''
        Alakzat rajzolása
        '''
        pass

class Szoveg(Ablakkomponens):
    def __init__(self, pozicio, latszik, font, szoveg, meret, szin, kozep_origo = False):
        super().__init__(pozicio, (0,0), latszik)
    
        self.szoveg = Eszkozok.bemenetellenor(szoveg, str)
        self.font = Eszkozok.bemenetellenor(font, str)
        self.szin = Eszkozok.bemenetellenor(szin, tuple)
        # Betűtípus mérete relatív a képernyőhöz
        meret = meret
        self.iro = pg.font.SysFont(self.font, Eszkozok.bemenetellenor(meret, int))

        if type(pozicio)==tuple:
            if kozep_origo == True:
                self.pozicio=(
                    pozicio[0]-(self.iro.size(self.szoveg)[0]//2),
                    pozicio[1]-(self.iro.size(self.szoveg)[1]//2)
                )
            else:
                self.pozicio = pozicio
        else:
            print("[F] [Ablakvezerlo] Nem adtad meg a pozíciót")
            self.pozicio=(0,0)
        
    def rajzol(self, pg_felulet):
        pg_felulet.blit(self.iro.render(f"{self.szoveg}", True, self.szin), self.pozicio)
    def frissit(self, szoveg):
        self.szoveg = szoveg

class SzovegLista(Ablakkomponens):
    def __init__(self, pozicio, latszik, font, in_szoveglista, elteres_y, szin):
        super().__init__(pozicio, (0,0), latszik)
        self.font = Eszkozok.bemenetellenor(font, str)
        self.elteres_y = Eszkozok.bemenetellenor(elteres_y, int)
        self.szin = Eszkozok.bemenetellenor(szin, tuple)
        self.szovegek = {}

        in_szoveglista = Eszkozok.bemenetellenor(in_szoveglista, list)
        for i in range(len(in_szoveglista)):
            self.szovegek.update({in_szoveglista[i]: Szoveg((self.pozicio[0], self.pozicio[1]+(i*self.elteres_y)), self.latszik, self.font, in_szoveglista[i], 15, (0,0,0))})

    def rajzol(self, pg_felulet):
        for i in self.szovegek.keys():
            self.szovegek[i].rajzol(pg_felulet)

    def s_uj_szoveglista(self, in_szoveglista):
        '''
        Kicseréli a meglévő szöveglistát új szavakkal
        '''
        self.szovegek = {}
        for i in range(len(in_szoveglista)):
            self.szovegek.update({in_szoveglista[i]: Szoveg((self.pozicio[0], self.pozicio[1]+(i*self.elteres_y)), self.latszik, self.font, in_szoveglista[i], 15, (0,0,0))})

class Gomb(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, szin, vastagsag, in_szoveg="", font="Consolas"):
        super().__init__(pozicio, dimenziok, latszik)
        # Szín
        self.szin = Eszkozok.bemenetellenor(szin, tuple)
        # Vastagság
        self.vastagsag = Eszkozok.bemenetellenor(vastagsag, int)
        # Szöveg
        if type(in_szoveg) == str:
            self.szoveg = Szoveg(
                (self.pozicio[0]+(self.dimenziok[0]//2), self.pozicio[1]+(self.dimenziok[1]//2)),
                True,
                font,
                in_szoveg,
                10,
                (0,0,0),
                True
            )
        else:
            print("[F] [Ablakvezerlo] A szöveg csak string lehet")


    def rajzol(self, pg_felulet):
        pg.draw.rect(pg_felulet, self.szin, pg.Rect(self.pozicio[0], self.pozicio[1], 
        self.dimenziok[0], self.dimenziok[1]), self.vastagsag)
        self.szoveg.rajzol(pg_felulet)
        
    def g_lenyomva(self):
        '''
        Le van-e nyomva a gomb
        '''
        kurzor_poz = pg.mouse.get_pos()
        if _gomb_lenyomva == True:
            # ellenőrzés x, y tengelyre
            if (kurzor_poz[0] > self.pozicio[0] and kurzor_poz[0] < self.pozicio[0]+self.dimenziok[0]) and (kurzor_poz[1] > self.pozicio[1] and kurzor_poz[1] < self.pozicio[1]+self.dimenziok[1]):
                return True
            else:
                return False

class Grid(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, feloszt_meret, szin):
        super().__init__(pozicio, dimenziok, latszik)

        self.feloszt_meret = Eszkozok.bemenetellenor(feloszt_meret, int)
        self.szin = Eszkozok.bemenetellenor(szin, tuple)

        self.koordinatak = []
        self.betu = pg.font.SysFont("Verdana", 20)
        self.kijeloles = False # A rács állapota (kijelölés folyik / nem)
        self.szolista = []

    def rajzol(self, pg_felulet):
        for i in range(self.feloszt_meret):
            for j in range(self.feloszt_meret):
                if (i, j) in self.koordinatak:
                    szin = (255,0,0)
                else:
                    szin = self.szin
                pg.draw.rect(
                    # négyzetek rajzolása, a rács felosztása
                    pg_felulet,
                    szin,
                    pg.Rect(
                        self.pozicio[0]+i*(self.dimenziok[0]/self.feloszt_meret),
                        self.pozicio[1]+j*(self.dimenziok[1]/self.feloszt_meret),
                        self.dimenziok[0]/(self.feloszt_meret),
                        self.dimenziok[1]/(self.feloszt_meret)
                    ),
                    1
                )
                
                pg_felulet.blit(self.betu.render(str(self.szolista[j][i]), True, (0,0,0)), (
                    # betűk kiírása
                    self.pozicio[0]+i*(self.dimenziok[0]/self.feloszt_meret)+(self.dimenziok[0]/(self.feloszt_meret)//2)-self.betu.size(str(self.szolista[j][i]))[0],
                    self.pozicio[1]+j*(self.dimenziok[1]/self.feloszt_meret)+(self.dimenziok[1]/(self.feloszt_meret)//2)-self.betu.get_height()//2
                ))
    
    def g_valasztas(self):
        '''
        Visszaadja a rácson választott koordinátákat
        '''
        koordinatak = (
            (pg.mouse.get_pos()[0]-self.pozicio[0])//(self.dimenziok[0]/(self.feloszt_meret)), 
            (pg.mouse.get_pos()[1]-self.pozicio[1])//(self.dimenziok[1]/(self.feloszt_meret))
        )
        if _gomb_lenyomva == True:
            self.kijeloles = True
            # Kijelölt koordináták összegyűjtése
            if koordinatak not in self.koordinatak:
                if (koordinatak[0] >= 0 and koordinatak[0] <= (self.feloszt_meret-1)) and (koordinatak[1] >= 0 and koordinatak[1] <= (self.feloszt_meret-1)):
                    self.koordinatak.append(koordinatak)
            return self.kijeloles
        elif _gomb_lenyomva == False and self.kijeloles == True:
            # Ha a kijelölés elvégződött
            self.kijeloles = False
            return self.koordinatak
        elif _gomb_lenyomva == False and self.kijeloles == False:
            # Ha nincs kijelölés folyamatban
            self.koordinatak = []
            return False

    def s_frissit(self, feloszt_meret):
        '''
        Frissíti a felosztás mértékét
        '''
        self.feloszt_meret = feloszt_meret

class Negyszog(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, szin, vastagsag):
        super().__init__(pozicio, dimenziok, latszik)
        # Szín
        self.szin = Eszkozok.bemenetellenor(szin, tuple)
        # Vastagság
        self.vastagsag = Eszkozok.bemenetellenor(vastagsag, int)

    def rajzol(self, pg_felulet):
        pg.draw.rect(pg_felulet, self.szin, pg.Rect(self.pozicio[0], self.pozicio[1], self.dimenziok[0], self.dimenziok[1]), self.vastagsag)

# Ablak

class Ablak():
    def __init__(self, in_elemek, hatterszin):
        '''
        Ablak inicializálása ablakkomponensekkel
        '''
        # Elemek
        self.ELEMEK = {} # "nev":Ablakkomponens()
        if type(in_elemek) == dict:
            for i in in_elemek.keys():
                if type(in_elemek[i]).__bases__[0] == Ablakkomponens:
                    self.ELEMEK.update({i: in_elemek[i]})
                else:
                    print(f"[F] [Ablakvezerlo] Nem ablakkomponenst akar felvenni az ablakba ({str(type(in_elemek[i]))})")
        # Háttérszín
        self.hatterszin = Eszkozok.bemenetellenor(hatterszin, tuple)

# Ablakvezérlő

class Ablakvezerlo():
    def __init__(self):
        # PyGame ablakelemek inicializálása
        global FELBONTAS
        FELBONTAS = (pg.display.Info().current_w, pg.display.Info().current_h)
        self.TULAJDONSAGOK = {
            "FELBONTAS": FELBONTAS,
            "ABLAK_MERET": (pg.display.Info().current_w//1.5, pg.display.Info().current_h//1.5),
            "CIM": "Szókereső"
        }
        self.FOLYAMAT_ABLAK = pg.display.set_mode(self.TULAJDONSAGOK["ABLAK_MERET"])
        pg.display.set_caption(self.TULAJDONSAGOK["CIM"])
        self.PG_CLOCK = pg.time.Clock()
        self.FPS = 60
        self.elozo_ablak = "" # Ablakváltáskor a kattintás pozíciója megmaradhat, így azt olyankor ki kell kapcsolni, ehhez tudni kell az előző ablakot.
        # Ablakok inicializálása
        self.ABLAKOK = {} # Értéket az init_ablaklista függvény ad majd.

    def init_ablaklista(self, in_ablakok: dict):
        '''
        Ablakok inicializálása. Formátum: "jatekallas": Ablak()
        '''
        for i in in_ablakok.keys():
            if type(in_ablakok[i]) == Ablak:
                if len(in_ablakok[i].ELEMEK) > 0:
                    self.ABLAKOK.update({i: in_ablakok[i]})
                else:
                    print("[F] [Ablakvezerlo] Egy ablak felvétele nem sikerült, mert egyetlen komponens sem megfelelő benne")

    def frissit(self, jatekallas):
        global _gomb_lenyomva
        # Események kezelése
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
            elif i.type == pg.MOUSEBUTTONDOWN:
                _gomb_lenyomva = True
            elif i.type == pg.MOUSEBUTTONUP:
                _gomb_lenyomva = False
        # Képfrissítés
        self.PG_CLOCK.tick(self.FPS)
        pg.display.update()
        # Ablakváltás ellenőrzése
        if self.elozo_ablak != jatekallas:
            _gomb_lenyomva = False
            self.elozo_ablak = jatekallas
        # A játékállásnak megfelelő ablak elemeinek kirajzolása
        if jatekallas in self.ABLAKOK.keys():
            self.FOLYAMAT_ABLAK.fill(self.ABLAKOK[jatekallas].hatterszin)
            for i in self.ABLAKOK[jatekallas].ELEMEK.keys():
                if self.ABLAKOK[jatekallas].ELEMEK[i].latszik == True:
                    self.ABLAKOK[jatekallas].ELEMEK[i].rajzol(self.FOLYAMAT_ABLAK)
        else:
            # Ha az ablak nem létezik vörös képernyő figyelmeztet
            self.FOLYAMAT_ABLAK.fill((255,0,0))
    
    # getter függvények
    def g_FELBONTAS(self):
        return self.TULAJDONSAGOK["FELBONTAS"]
    def g_ablakmeret(self):
        return self.TULAJDONSAGOK["ABLAK_MERET"]