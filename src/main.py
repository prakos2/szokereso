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
         # ablaknév
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
            pg.display.set_caption(str(10-(pg.time.get_ticks()//1000)))
            # Játékvezérlés
            if self.JATEKVEZERLO.jatekallas == "menu":
                self.JATEKVEZERLO.f_jatekallas("jatek")
            elif self.JATEKVEZERLO.jatekallas == "jatek":
                self.JATEKVEZERLO.f_jatekallas("vegeredmeny")
            elif self.JATEKVEZERLO.jatekallas == "vegeredmeny":
                self.JATEKVEZERLO.f_jatekallas("menu")


if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany._folyamat()
    exit()