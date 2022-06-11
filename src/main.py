import pygame as pg
import sys
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
                    25,
                    (0,0,0),
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
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//2.5+10+self.ABLAKVEZERLO.g_ablakmeret()[0]//4, 10),
                    True,
                    "Arial",
                    "0",
                    25,
                    (0,0,0),
                    False
                ),
                "racs": AV.Grid(
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//2.5-self.ABLAKVEZERLO.g_ablakmeret()[0]//4,
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//2-self.ABLAKVEZERLO.g_ablakmeret()[0]//4
                    ),
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//2,self.ABLAKVEZERLO.g_ablakmeret()[0]//2),
                    True,
                    3,
                    (0,0,0)
                ),
                "szavak_lista": AV.Negyszog(
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//2.5+10+self.ABLAKVEZERLO.g_ablakmeret()[0]//4,
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//2-self.ABLAKVEZERLO.g_ablakmeret()[0]//4
                    ),
                    (self.ABLAKVEZERLO.g_ablakmeret()[0]//4-15,self.ABLAKVEZERLO.g_ablakmeret()[0]//2),
                    True,
                    (0,0,0),
                    1
                ),
                "szavak": AV.SzovegLista(
                    (
                        self.ABLAKVEZERLO.g_ablakmeret()[0]//2.5+10+self.ABLAKVEZERLO.g_ablakmeret()[0]//4,
                        self.ABLAKVEZERLO.g_ablakmeret()[1]//2-self.ABLAKVEZERLO.g_ablakmeret()[0]//4
                    ),
                    True,
                    "Verdana",
                    ["init"],
                    20,
                    (0,0,0)
                )
            }, (233,179,94)),
            "vegeredmeny": AV.Ablak({
                "vege": AV.Szoveg((self.ABLAKVEZERLO.g_ablakmeret()[0]//2, 20), True, "Verdana", "A játék véget ért", 25, (0,0,0), True),
                "pontszam": AV.Szoveg((self.ABLAKVEZERLO.g_ablakmeret()[0]//2, 20*3), True, "Verdana", f"Elért pontszám: {self.JATEKVEZERLO.jatek_adatok['pont']}", 25, (0,0,0), True),
                "ujra": AV.Gomb((self.ABLAKVEZERLO.g_ablakmeret()[0]//2, 0), (50,50), True, (0,0,0), 1, "Újra")
            }, (233,179,94))
        })
    
    """
    Játékfolyamat
    """
    def folyamat(self):
        F_JV = self.JATEKVEZERLO
        F_AV = self.ABLAKVEZERLO
        while True:
            try:

                # A vezérlők frissítése
                F_AV.frissit(F_JV.g_jatekallas())
                # Játékirányítás
                if F_JV.g_jatekallas() == "menu":
                    if F_AV.ABLAKOK["menu"].ELEMEK["start"].g_lenyomva() == True:
                        F_JV.s_uj_jatek(F_AV.ABLAKOK["jatek"])
                        F_JV.s_jatekallas("jatek")
                    elif F_AV.ABLAKOK["menu"].ELEMEK["kilepes"].g_lenyomva() == True:
                        pg.quit()
                        exit()

                elif F_JV.g_jatekallas() == "jatek":
                    ido = F_JV.jatek_adatok["jatekido"]-pg.time.get_ticks()//1000
                    if ido < 0: F_JV.s_jatekallas("vegeredmeny") # Ha lejárt az idő
                    # Visszaszámláló óra frissítése
                    F_AV.ABLAKOK["jatek"].ELEMEK["time"].frissit(
                        Eszkozok.idoformat(ido) + f" - {F_JV.jatek_adatok['szint']}. szint"
                    )
                    # Kijelölés frissítése
                    racs_valasztas = F_AV.ABLAKOK["jatek"].ELEMEK["racs"].g_valasztas()
                    if type(racs_valasztas) == list:
                        F_JV.szo_ellenor([(int(i[0]), int(i[1])) for i in racs_valasztas])

                elif F_JV.g_jatekallas() == "vegeredmeny":
                    F_AV.ABLAKOK["vegeredmeny"].ELEMEK["pontszam"].frissit(
                        F_JV.jatek_adatok["pont"]
                    )
                    if F_AV.ABLAKOK["vegeredmeny"].ELEMEK["ujra"].g_lenyomva() == True:
                        F_JV.s_uj_jatek(F_AV.ABLAKOK["jatek"])
                        F_JV.s_jatekallas("jatek")

            except Exception as kivetel:
                # "crash" előidézése hogy a program ne lépjen "nem válaszol" állapotba fatális kivétel esetén
                print("crash: " + str(kivetel))
                pg.quit()
                exit()

if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany.folyamat()