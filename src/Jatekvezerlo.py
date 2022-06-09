import pygame as pg
import random
import Eszkozok

class Jatekvezerlo():
    def __init__(self):
        # Játékállás
        self.JATEKALLASOK = ("menu", "jatek", "vegeredmeny") # Sorrendben lévő játékállások
        self.jatekallas = self.JATEKALLASOK[0]               # Első lehetséges játékállás megadása
        # A játék adatai, ez a dictionary gyakori módosításokon esik át a játék menete alatt
        self.jatek_adatok={
            "szint": 0,              # jelenlegi szint
            "jatekido": 0            # s
        }
        # Szavak listája
        self.szavak = []
        try:
            with open("./assets/szavak.txt", encoding="utf-8-sig") as SZAVAK_FAJL:
                for i in SZAVAK_FAJL.readlines():
                    try:
                        for j in i.split(';'):
                            self.szavak.append(j)
                    except Exception as kivetel:
                        print(f"[F] [Jatekvezerlo] Hiba a sor beolvasása közben: {str(kivetel)}")
        except Exception as kivetel:
            print(f"[H] [Jatekvezerlo] Fatális hiba a fájl beolvasása közben: {str(kivetel)}")
        print(self.szavak)
        # Szórács
        self.szo_grid = []

    def frissit(self):
        pass

    # setter függvények
    def s_uj_jatek(self, t):
        if type(t) != int:
            t = 180
        self.jatek_adatok["szint"] = 0 # Szint nullázása
        self.jatek_adatok["jatekido"] = (pg.time.get_ticks()//1000 + t) # Játékidő meghatározása: jelenlegi + össz

    def s_jatekallas(self, in_jatekallas):
        """
        Játékállás frissítése
        """
        if in_jatekallas in self.JATEKALLASOK:
            self.jatekallas = in_jatekallas
        else:
            print("[F] [Jatekvezerlo] Megadott játékállás helytelen.")

    # getter függvények
    def g_jatekallas(self):
        return self.jatekallas
    
    # eszközök
    def grid_general(self, N, max_szavak):
        self.szo_grid = [[0 for x in range(N)] for j in range(N)]
        for i in max_szavak:
            r_koord = (random.randint(0, N-1), random.randint(0, N-1))
            tengely = random.randint(1)
            if tengely == 0:
                # vízszint
                Eszkozok.szokeres(self.szavak, N)
            else:
                # függőleges
                Eszkozok.szokeres(self.szavak, N)