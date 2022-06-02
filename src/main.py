import pygame as pg
from Jatekvezerlo import Jatekvezerlo
from Ablakvezerlo import Ablakvezerlo, Ablakkomponens

class Szokereso():
    """
    Inicializálás
    """
    def __init__(self):
        # PyGame
        pg.init()
        self.ORA = pg.time.Clock() # óra
        # PyGame ablak
        self.FELBONTAS=self.ABLAK_SZELESSEG, self.ABLAK_MAGASSAG=(pg.display.Info().current_w, pg.display.Info().current_h) # A képernyő teljes mérete
        self.ABLAK_MERET=(self.ABLAK_SZELESSEG/1.5, self.ABLAK_MAGASSAG/1.5) # Relatív ablakméret
        self.FPS=60 # képkocka / s
        self.KEPERNYO=pg.display.set_mode(self.ABLAK_MERET) # képernyőméret
        pg.display.set_caption("Szókereső") # ablaknév
        # Játékvezérlő
        self.JATEKVEZERLO = Jatekvezerlo()
        self.JATEKVEZERLO.reset()
        # Ablakvezérlő
        self.ABLAKVEZERLO = Ablakvezerlo()
        # Ablakok inicializálása
        Ablakvezerlo.s_ablakok
    
    """
    Tickre változó függvény
    """
    def folyamat(self):
        while True:
            # Kilépés kezelése
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    return
            # Képfrissítés
            pg.display.flip()
            self.ORA.tick(self.FPS)
            # Játékvezérlés
            if self.JATEKVEZERLO.jatekallas == "menu":
                Ablakvezerlo.rajzol("menu")
            elif self.JATEKVEZERLO.jatekallas == "jatek":
                Ablakvezerlo.rajzol("jatek")
            elif self.JATEKVEZERLO.jatekallas == "vegeredmeny":
                Ablakvezerlo.rajzol("vegeredmeny")

if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany.folyamat()
    exit()