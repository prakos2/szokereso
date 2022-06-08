import pygame as pg
from Jatekvezerlo import Jatekvezerlo
import Ablakvezerlo as AV

class Szokereso():
    """
    Inicializálás
    """
    def __init__(self):
        # PyGame
        pg.init()
        # Játékvezérlő
        self.JATEKVEZERLO = Jatekvezerlo()
        # Ablakvezérlő, ablakok inicializálása
        self.ABLAKVEZERLO = AV.Ablakvezerlo()
        self.ABLAKVEZERLO.init_ablaklista({
            "menu": AV.Ablak({
                "start_gomb": AV.Gomb((self.ABLAKVEZERLO.g_ablakmeret()[0]//2, self.ABLAKVEZERLO.g_ablakmeret()[1]//2), True, (255,0,0), 10),
                "szoveg":AV.Szoveg(pozicio=(1,1),latszik=True,font="Consola",szoveg="teszt")
            }, (255,255,255)),
            "jatek": AV.Ablak({
                "grid": AV.Grid()
            }, (255,255,255)),
            "vegeredmeny": AV.Ablak({
                "kilepes_gomb": AV.Negyszog()
            }, (255,255,255))
        })
    
    """
    Játékfolyamat
    """
    def folyamat(self):
        while True:
            # A vezérlők frissítése
            self.JATEKVEZERLO.frissit()
            self.ABLAKVEZERLO.frissit(self.JATEKVEZERLO.g_jatekallas())
            # Játékirányítás
            if self.JATEKVEZERLO.g_jatekallas() == "menu":
                pass
            elif self.JATEKVEZERLO.g_jatekallas() == "jatek":
                pass
            elif self.JATEKVEZERLO.g_jatekallas() == "vegeredmeny":
                pass

if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany.folyamat()