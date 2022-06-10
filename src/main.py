import pygame as pg
from Jatekvezerlo import Jatekvezerlo
import Ablakvezerlo as AV
import Eszkozok

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
                "cim": AV.Szoveg(
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//2, self.ABLAKVEZERLO.g_ablakmeret()[1]//2),
                    True,
                    "Consolas",
                    "Szókereső",
                    True
                ),
                "start": AV.Gomb(
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//2-(self.ABLAKVEZERLO.g_ablakmeret()[0]//5)//2,
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//2
                    ),
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//5, 
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//15
                    ),
                    True,
                    (255,255,255),
                    2,
                    "Start"
                ),
                "kilepes": AV.Gomb(
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//2-(self.ABLAKVEZERLO.g_ablakmeret()[0]//5)//2, 
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//1.5-(self.ABLAKVEZERLO.g_ablakmeret()[1]//15)//2
                    ),
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//5,
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//15
                    ),
                    True,
                    (255,255,255),
                    2,
                    "Kilépés"
                ),
            }, (233,179,94)),
            "jatek": AV.Ablak({
                "time": AV.Szoveg(
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//2, 20),
                    True,
                    "Arial",
                    "0",
                    True
                ),
                "racs": AV.Grid(
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//2-(self.ABLAKVEZERLO.g_ablakmeret()[0]//2/2),self.ABLAKVEZERLO.g_ablakmeret()[1]//2-(self.ABLAKVEZERLO.g_ablakmeret()[1]//2/2)),
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//2,self.ABLAKVEZERLO.g_ablakmeret()[1]//2),
                    True,
                    8,
                    (0,0,0)
                )
            }, (255,255,255))
        })
        #self.JATEKVEZERLO.grid_general(8, 8)
    
    """
    Játékfolyamat
    """
    def folyamat(self):
        while True:
            try:
                # A vezérlők frissítése
                self.JATEKVEZERLO.frissit()
                self.ABLAKVEZERLO.frissit(self.JATEKVEZERLO.g_jatekallas())
                # Játékirányítás
                if self.JATEKVEZERLO.g_jatekallas() == "menu":
                    if self.ABLAKVEZERLO.ABLAKOK["menu"].ELEMEK["start"].g_lenyomva() == True:
                        self.JATEKVEZERLO.s_uj_jatek(600) # Új 10 perces játék
                        self.JATEKVEZERLO.s_jatekallas("jatek")
                    elif self.ABLAKVEZERLO.ABLAKOK["menu"].ELEMEK["kilepes"].g_lenyomva() == True:
                        pg.quit()
                        exit()
                elif self.JATEKVEZERLO.g_jatekallas() == "jatek":
                    # Visszaszámláló óra frissítése
                    self.ABLAKVEZERLO.ABLAKOK["jatek"].ELEMEK["time"].frissit(
                        Eszkozok.idoformat(self.JATEKVEZERLO.jatek_adatok["jatekido"]-pg.time.get_ticks()//1000)
                    )
                    print(self.ABLAKVEZERLO.ABLAKOK["jatek"].ELEMEK["racs"].g_valasztas())
                elif self.JATEKVEZERLO.g_jatekallas() == "vegeredmeny":
                    pass
            except Exception as kivetel:
                # "crash" előidézése hogy a program ne lépjen "nem válaszol" állapotba fatális kivétel esetén
                print("crash: " + str(kivetel))
                pg.quit()
                exit()

if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany.folyamat()