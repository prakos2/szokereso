import pygame as pg
from Jatekvezerlo import Jatekvezerlo

class Szokereso():
    """
    Inicializálás
    """
    def __init__(self):
        # PyGame
        pg.init()
        self.ORA = pg.time.Clock() # óra
        # PyGame ablak
        self.FELBONTAS=self.SZELESSEG, self.MAGASSAG=(pg.display.Info().current_w, pg.display.Info().current_h) # A képernyő teljes mérete
        self.ABLAK_MERET=(self.SZELESSEG/1.5, self.MAGASSAG/1.5) # Relatív ablakméret
        self.FPS=60 # Képkocka/s
        self.KEPERNYO=pg.display.set_mode(self.ABLAK_MERET) # képernyőméret
        pg.display.set_caption("Szókereső") # ablaknév
        # Játékvezérlő
        self.JATEKVEZERLO = Jatekvezerlo()
        self.JATEKVEZERLO.reset()
    
    """
    Tickre változó függvény
    """
    def _folyamat(self):
        while True:
            # Kilépés kezelése
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    return
            # Képfrissítés
            pg.display.flip()
            self.ORA.tick(self.FPS)
            # Játékvezérlés
            self.JATEKVEZERLO.frissit()
            if self.JATEKVEZERLO.jatekallas == "menu":
                self.KEPERNYO.fill((255,255,255))
                self.JATEKVEZERLO.f_jatekallas("jatek")
            elif self.JATEKVEZERLO.jatekallas == "jatek":
                self.KEPERNYO.fill((125,52,52))
                self.JATEKVEZERLO.f_jatekallas("vegeredmeny")
            elif self.JATEKVEZERLO.jatekallas == "vegeredmeny":
                self.KEPERNYO.fill((52,32,12))
                self.JATEKVEZERLO.f_jatekallas("menu")


if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany._folyamat()
    exit()