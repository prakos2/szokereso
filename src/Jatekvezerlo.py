class Jatekvezerlo():
    def __init__(self):
        # Játékállás
        self.JATEKALLASOK = ("menu", "jatek", "vegeredmeny") # Sorrendben lévő játékállások
        self.jatekallas = self.JATEKALLASOK[0]               # Első lehetséges játékállás megadása
        self.jatek_adatok={
            "szint": 0,              # jelenlegi szint
            "szavak": 0,             # össz szó
            "megtalalt_szavak": 0,   # megtalált szavak / szint
            "ossz_szavak": 0,        # összes megtalált szó
            "eltelt_jatekido": 0,    # ms
            "ossz_jatekido": 0       # ms
        }

    # setter függvények
    def s_jatekallas(self, in_jatekallas):
        """
        Játékállás frissítése
        """
        if in_jatekallas in self.JATEKALLASOK:
            self.jatekallas = in_jatekallas
        else:
            raise Exception("[Jatekvezerlo] Megadott játékállás helytelen.")

    def reset(self):
        """
        A játék újraindítása
        """
        try:
            self.s_jatekallas("menu")
            for i in self.jatek_adatok:
                self.jatek_adatok[i] = 0
        except:
            raise Exception("[Jatekvezerlo] Reset nem lehetséges.")

    # getter függvények

class Ellenor():
    pass