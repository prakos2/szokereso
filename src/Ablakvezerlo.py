import pygame as pg

# Globális változók
_gomb_lenyomva = False # Bármely egérgomb lenyomva

# Ablakkomponensek

class Ablakkomponens():
    def __init__(self, pozicio = (0,0), dimenziok = (0,0), latszik = True) -> None:
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
    def __init__(self, pozicio, latszik, font, szoveg, kozep_origo = False) -> None:
        super().__init__(pozicio, (0,0), latszik)
        
        if type(szoveg) == str:
            self.szoveg=szoveg
        else:
            self.szoveg="*HIBÁS*"

        if type(font) == str:
            self.font = font
        else:
            print("[F] Ablakvezerlo] A betűtípust stringként kell megadni, de nem az")
            self.font = "Consolas"
        self.iro=pg.font.SysFont(self.font, 30)

        if type(pozicio)==tuple:
            if kozep_origo == True:
                self.pozicio=(
                    pozicio[0]-(self.iro.size(self.szoveg)[0]//2),
                    pozicio[1]-(self.iro.size(self.szoveg)[1]//2)
                )
            else:
                self.pozicio = pozicio
        else:
            print("[F] Ablakvezerlo] Nem adtad meg a pozíciót")
            self.pozicio=(0,0)
        
    def rajzol(self, pg_felulet):
        pg_felulet.blit(self.iro.render(f"{self.szoveg}", True, (0,0,0)), self.pozicio)
    def frissit(self, szoveg):
        self.szoveg = szoveg

class Gomb(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, szin, vastagsag, in_szoveg="", font="Consolas") -> None:
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
    def __init__(self) -> None:
        super().__init__()
    def rajzol(self, pg_felulet):
        pass

class Negyszog(Ablakkomponens):
    def __init__(self, pozicio, dimenziok, latszik, szin, vastagsag) -> None:
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
        pg.draw.rect(pg_felulet, self.szin, pg.Rect(0,0, self.pozicio[0], self.pozicio[1]), self.vastagsag)

# Ablak

class Ablak():
    def __init__(self, in_elemek, hatterszin) -> None:
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
        self.TULAJDONSAGOK = {
            "FELBONTAS": (pg.display.Info().current_w, pg.display.Info().current_h),
            "ABLAK_MERET": (pg.display.Info().current_w//1.5, pg.display.Info().current_h//1.5),
            "CIM": "Szókereső"
        }
        self.FOLYAMAT_ABLAK = pg.display.set_mode(self.TULAJDONSAGOK["ABLAK_MERET"])
        pg.display.set_caption(self.TULAJDONSAGOK["CIM"])
        self.PG_CLOCK = pg.time.Clock()
        self.FPS = 60
        # Ablakok inicializálása
        self.ABLAKOK = {} # Értéket az init_ablaklista függvény ad majd.

    def init_ablaklista(self, in_ablakok):
        '''
        Ablakok inicializálása, dictionaryt vár. Formátum: "jatekallas": Ablak()
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
        if jatekallas in self.ABLAKOK.keys():
            self.FOLYAMAT_ABLAK.fill(self.ABLAKOK[jatekallas].hatterszin)
            for i in self.ABLAKOK[jatekallas].ELEMEK.keys():
                self.ABLAKOK[jatekallas].ELEMEK[i].rajzol(self.FOLYAMAT_ABLAK)
        else:
            self.FOLYAMAT_ABLAK.fill((255,0,0))
    
    # getter függvények
    def g_felbontas(self):
        return self.TULAJDONSAGOK["FELBONTAS"]
    def g_ablakmeret(self):
        return self.TULAJDONSAGOK["ABLAK_MERET"]