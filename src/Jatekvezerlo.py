class Jatekvezerlo():
    def __init__(self):
        # Játékállás
        self.JATEKALLASOK = ("menu", "jatek", "vegeredmeny") # Sorrendben lévő játékállások
        self.jatekallas = self.JATEKALLASOK[0]               # Első lehetséges játékállás megadása
        self.jatek_adatok={
            "szint": 0,              # jelenlegi szint
            "ossz_jatekido": 0       # ms
        }

    def frissit(self):
        pass

    # setter függvények
    def s_jatekallas(self, in_jatekallas):
        """
        Játékállás frissítése
        """
        if in_jatekallas in self.JATEKALLASOK:
            self.jatekallas = in_jatekallas
        else:
            raise Exception("[Jatekvezerlo] Megadott játékállás helytelen.")

    # getter függvények
    def g_jatekallas(self):
        return self.jatekallas