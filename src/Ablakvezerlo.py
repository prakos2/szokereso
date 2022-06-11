import pygame as pg
import Eszkozok

# Globális változók
_gomb_lenyomva = False # Bármely egérgomb lenyomva
_FELBONTAS = () # A teljes képernyő felbontása, inicializáláskor kap értéket
_FHD_ARANY = () # A képernyő aránya a full hd felbontáshoz képest

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
        if ertek != self.latszik:
            self.latszik = ertek
    
    def g_latszik(self):
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
        print(self.szoveg)
        self.font = Eszkozok.bemenetellenor(font, str)
        self.szin = Eszkozok.bemenetellenor(szin, tuple)
        # Betűtípus mérete relatív a képernyőhöz
        meret = meret*_FHD_ARANY
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
            self.szovegek.update({in_szoveglista[i]: Szoveg((self.pozicio[0], self.pozicio[1]+(i*self.pozicio[1])), self.latszik, self.font, in_szoveglista[i], 15, (0,0,0))})

    def rajzol(self, pg_felulet):
        for i in self.szovegek.keys():
            self.szovegek[i].rajzol(pg_felulet)

    def s_uj_szoveglista(self, in_szoveglista):
        self.szovegek = {}
        for i in range(len(in_szoveglista)):
            self.szovegek.update({in_szoveglista[i]: Szoveg((self.pozicio[0], self.pozicio[1]+(i*self.pozicio[1])), self.latszik, self.font, in_szoveglista[i], 15, (0,0,0))})

class Gomb(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, szin, vastagsag, in_szoveg="", font="Consolas"):
        super().__init__(pozicio, dimenziok, latszik)
        # Szín
        if type(szin) == tuple and len(szin) == 3:
            self.szin = szin
        else:
            print("[F] [Ablakvezerlo] Az ablakkomponens színe csak RGB tuple lehet. Alapértelmezett színre cserélés.")
            self.szin = (0,0,0)
        # Vastagság
        if type(vastagsag) == int:
            self.vastagsag = vastagsag
        else:
            print("[F] [Ablakvezerlo] Az ablakkomponens vastagsága csak egész szám lehet. Alapértelmezett értékre cserélés.")
            self.vastagsag = 1
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

        if type(feloszt_meret) == int:
            self.feloszt_meret = feloszt_meret
        else:
            print("[F] [Ablakvezerlo] A méret egész szám lehet")
            self.feloszt_meret = 2

        if type(szin) == tuple and len(szin) == 3:
            self.szin = szin
        else:
            print("[F] [Ablakvezerlo] A szín tuple RGB lehet")
            self.szin = (0,0,0)
        self.koordinatak = []
        self.betu = pg.font.SysFont("Verdana", 20*int(_FELBONTAS[1]//1080))
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
                    self.pozicio[0]+i*(self.dimenziok[0]/self.feloszt_meret),
                    self.pozicio[1]+j*(self.dimenziok[1]/self.feloszt_meret)
                ))
    
    def g_valasztas(self):
        koordinatak = (
            (pg.mouse.get_pos()[0]-self.pozicio[0])//(self.dimenziok[0]/(self.feloszt_meret)), 
            (pg.mouse.get_pos()[1]-self.pozicio[1])//(self.dimenziok[1]/(self.feloszt_meret))
        )
        if _gomb_lenyomva == True:
            self.kijeloles = True
            if koordinatak not in self.koordinatak:
                if (koordinatak[0] >= 0 and koordinatak[0] <= self.feloszt_meret) and (koordinatak[1] >= 0 and koordinatak[1] <= self.feloszt_meret):
                    self.koordinatak.append(koordinatak)
            return self.kijeloles
        elif _gomb_lenyomva == False and self.kijeloles == True:
            self.kijeloles = False
            return self.koordinatak
        elif _gomb_lenyomva == False and self.kijeloles == False:
            self.koordinatak = []
            return False

    def s_frissit(self, feloszt_meret):
        self.feloszt_meret = feloszt_meret

class Negyszog(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, szin, vastagsag):
        super().__init__(pozicio, dimenziok, latszik)
        # Szín
        if type(szin) == tuple and len(szin) == 3:
            self.szin = szin
        else:
            print("[F] [Ablakvezerlo] Az ablakkomponens színe csak RGB tuple lehet. Alapértelmezett színre cserélés.")
            self.szin = (0,0,0)
        # Vastagság
        if type(vastagsag) == int:
            self.vastagsag = vastagsag
        else:
            print("[F] [Ablakvezerlo] Az ablakkomponens vastagsága csak egész szám lehet. Alapértelmezett értékre cserélés.")
            self.vastagsag = 1

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
        if type(hatterszin) == tuple:
            if len(hatterszin) == 3:
                self.hatterszin = hatterszin
            else:
                self.hatterszin = (125,0,0)
                print("[F] [Ablakvezerlo] A háttérszín csak RGB tuple lehet. Alapértelmezett színre cserélés.")

# Ablakvezérlő

class Ablakvezerlo():
    def __init__(self):
        # PyGame ablakelemek inicializálása
        global _FELBONTAS, _FHD_ARANY
        _FELBONTAS = (pg.display.Info().current_w, pg.display.Info().current_h)
        _FHD_ARANY = (1920/_FELBONTAS[0])/(1080/_FELBONTAS[1])

        self.TULAJDONSAGOK = {
            "FELBONTAS": _FELBONTAS,
            "ABLAK_MERET": (pg.display.Info().current_w//1.5, pg.display.Info().current_h//1.5),
            "CIM": "Szókereső"
        }
        self.FOLYAMAT_ABLAK = pg.display.set_mode(self.TULAJDONSAGOK["ABLAK_MERET"])
        pg.display.set_caption(self.TULAJDONSAGOK["CIM"])
        self.PG_CLOCK = pg.time.Clock()
        self.FPS = 60
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
        # FPS
        pg.display.set_caption(f"FPS: {self.PG_CLOCK.get_fps()}")
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
        if jatekallas in self.ABLAKOK.keys():
            self.FOLYAMAT_ABLAK.fill(self.ABLAKOK[jatekallas].hatterszin)
            for i in self.ABLAKOK[jatekallas].ELEMEK.keys():
                if self.ABLAKOK[jatekallas].ELEMEK[i].latszik == True:
                    self.ABLAKOK[jatekallas].ELEMEK[i].rajzol(self.FOLYAMAT_ABLAK)
        else:
            self.FOLYAMAT_ABLAK.fill((255,0,0))
    
    # getter függvények
    def g_felbontas(self):
        return self.TULAJDONSAGOK["FELBONTAS"]
    def g_ablakmeret(self):
        return self.TULAJDONSAGOK["ABLAK_MERET"]