import pygame as pg

# Ablakkomponensek

class Ablakkomponens():
    def __init__(self, pozicio = (0,0), latszik = True) -> None:
        self.pozicio = pozicio
        self.latszik = latszik

    def s_latszik(self, ertek):
        if ertek != self.latszik:
            self.latszik = ertek
    
    def g_latszik(self):
        return self.latszik

    def g_kurzorpoz(self):
        return pg.mouse.get_cursor()

    def rajzol(self, pg_felulet):
        '''
        Alakzat rajzolása
        '''
        pass

class Gomb(Ablakkomponens):
    def __init__(self, pozicio, latszik, szin, vastagsag) -> None:
        super().__init__(pozicio, latszik)
        # Szín
        if type(szin) == tuple and len(szin) == 3:
            self.szin = szin
        else:
            print("[Ablakvezerlo]: Az ablakkomponens színe csak RGB tuple lehet. Alapértelmezett színre cserélés.")
            self.szin = (0,0,0)
        # Vastagság
        if type(vastagsag) == int:
            self.vastagsag = vastagsag
        else:
            print("[Ablakvezerlo]: Az ablakkomponens vastagsága csak egész szám lehet. Alapértelmezett értékre cserélés.")
            self.vastagsag = 1

    def rajzol(self, pg_felulet):
        pg.draw.rect(pg_felulet, self.szin, pg.Rect(0,0,self.pozicio[0], self.pozicio[1]), self.vastagsag)
    def g_lenyomva(self):
        '''
        Le van-e nyomva a gomb
        '''
        return False

class Szoveg(Ablakkomponens):
    def __init__(self) -> None:
        super().__init__()
    def rajzol(self):
        pass

class Grid(Ablakkomponens):
    def __init__(self) -> None:
        super().__init__()
    def rajzol(self, surface):
        pass

class Negyszog(Ablakkomponens):
    def __init__(self) -> None:
        super().__init__()
    def rajzol(self, surface):
        pass

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
                if type(in_elemek[i]) == Gomb:
                    self.ELEMEK.update({i: in_elemek[i]})
                else:
                    print(f"[Ablakvezerlo]: Nem ablakkomponenst akar felvenni az ablakba ({str(type(in_elemek[i]))})")
        # Háttérszín
        if type(hatterszin) == tuple:
            if len(hatterszin) == 3:
                self.hatterszin = hatterszin
            else:
                self.hatterszin = (125,0,0)
                print("[Ablakvezerlo]: A háttérszín csak RGB tuple lehet. Alapértelmezett színre cserélés.")

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
        self.ABLAKOK = {}
        for i in in_ablakok.keys():
            if type(in_ablakok[i]) == Ablak:
                if len(in_ablakok[i].ELEMEK) > 0:
                    self.ABLAKOK.update({i: in_ablakok[i]})
                else:
                    print("[Ablakvezerlo] Egy ablak felvétele nem sikerült, mert egyetlen komponens sem megfelelő benne")

    def frissit(self, jatekallas):
        # Események kezelése
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                exit()
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