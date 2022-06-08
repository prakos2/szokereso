import pygame as pg

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
            raise Exception("[H] [Jatekvezerlo] Megadott játékállás helytelen.")

    # getter függvények
    def g_jatekallas(self):
        return self.jatekallas