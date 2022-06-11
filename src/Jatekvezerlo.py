import pygame as pg
import Ablakvezerlo
import Eszkozok
import random

class Jatekvezerlo():
    def __init__(self): 
        # Játékállás
        self.JATEKALLASOK = ("menu", "jatek", "vegeredmeny") # Sorrendben lévő játékállások
        self.jatekallas = self.JATEKALLASOK[0]               # Első lehetséges játékállás megadása
        self.MAX_SZINT = 5                                   # A játékon belül elérhető maximális szintek
        # A játék adatai
        self.jatek_adatok={
            "szint": 0,              # jelenlegi szint
            "jatekido": 0,           # s
            "pont": 0                # elért pontszám
        }
        # Aktuális játék szavai a rácson
        self.jatek_szavak = {} # Indexhivatkozás a szavak tömb elemeire -> Dictionary: szavak_adatbazis[x] : [bool, bool] (szó elhelyezve, szó megtalálva)
        self.jatek_grid = []   # Lista rács
        # Ablakvezérlő grafikus elemek
        self.av_grid = Ablakvezerlo.Grid            # Grafikus rács
        self.av_szolista = Ablakvezerlo.SzovegLista # Grafikus szöveglista
        # Szavak listája
        self.szavak_adatbazis = []
        try:
            with open(r"M:\[ISKOLA]\2022-projekt\szokereso\assets\szavak.txt", encoding="utf-8-sig") as SZAVAK_FAJL:
                for i in SZAVAK_FAJL.readlines():
                    try:
                        for j in i.split(';'):
                            self.szavak_adatbazis.append(j)
                    except Exception as kivetel:
                        print(f"[F] [Jatekvezerlo] Hiba a sor beolvasása közben: {str(kivetel)}")
        except Exception as kivetel:
            print(f"[H] [Jatekvezerlo] Fatális hiba a fájl beolvasása közben: {str(kivetel)}")
            pg.quit()
            exit()

    # Rács generálás
    def uj_racs(self, n):
        # Rács hosszának beállítása, ha kisebb mint a legrövidebb szó hossza, módosítás.
        legrovidebb_szo = min([len(x) for x in self.szavak_adatbazis if len(x) != 0])
        if n < legrovidebb_szo:
            n = legrovidebb_szo
            print("[F] [Jatekvezerlo] A rács mérete kisebb, mint a legrövidebb szó hossza. Átállítva a legrövidebb szó hosszára.")
        self.av_grid.feloszt_meret = n
        # Karaktertömb meghatározása
        karaktertomb = [[chr(random.randint(97,122)) for x in range(n)] for x in range(n)] # random ASCII betűkkel feltöltés
        # Szavak keresése, mindegyikhez bool hozzárendelése a későbbi elhelyezés végett.
        self.jatek_szavak = {x: [False, False] for x in random.sample([x for x in range(len(self.szavak_adatbazis)) if len(self.szavak_adatbazis[x]) <= n], n)}
        for i in range(len(karaktertomb)):
            # Végigiterálás az üres pozíciókon (y tengely lefele, x tengelyen szó elhelyezés)
            szo_index = random.choice(list(self.jatek_szavak))
            # Véletlenszerű szó kiválasztása
            if self.jatek_szavak[szo_index][0] == False:
                # Ha a szó még nincs a táblában
                max_x = (len(karaktertomb[i])-len(self.szavak_adatbazis[szo_index])) # maximum kezdőérték az x tengelyen
                random_x = random.randint(0,max_x)
                self.jatek_szavak[szo_index][0] = True
                betu_index = 0
                for j in range(random_x, random_x+len(self.szavak_adatbazis[szo_index])):
                    # Elhelyezés a táblában
                    karaktertomb[i][j] = self.szavak_adatbazis[szo_index][betu_index]
                    betu_index += 1
        self.av_szolista.s_uj_szoveglista([self.szavak_adatbazis[x] for x in self.jatek_szavak.keys() if self.jatek_szavak[x][0] == True])
        self.av_grid.szolista = karaktertomb

    # setter függvények
    def s_uj_szint(self, leptek):
        try:
            # Új szólista generáció
            self.grid_list = self.uj_racs(leptek)
        except Exception as kivetel:
            # Lehet, hogy a játék sincs még elkezdve. Ilyenkor nem lehet szintet lépni.
            print(f"[H] Hiba történt az új szintre lépés közben: {str(kivetel)}")

    def s_uj_jatek(self, jatekablak: Ablakvezerlo.Ablak, grid_n=16, t=180):
        if type(t) != int:
            t = 180
            print(f"[F] [Jatekvezerlo] Az idő csak egész szám lehet")
        self.jatek_adatok["szint"] = 0 # Szint nullázása
        self.jatek_adatok["jatekido"] = (pg.time.get_ticks()//1000 + t) # Játékidő meghatározása: jelenlegi + össz
        self.av_grid = jatekablak.ELEMEK["racs"] # Ablakvezérlő rács hozzárendelése a játékhoz
        self.av_szolista = jatekablak.ELEMEK["szavak"] # Ablakvezérlő rács szólista hozzárendelése a játékhoz
        # Új szólista generáció
        self.grid_list = self.uj_racs(grid_n)

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

    # Választás ellenőrzése
    def szo_ellenor(self, koord: list):
        # Koordináták alapján ellenőrzés
        szo = "".join([str(self.av_grid.szolista[i[1]][i[0]]) for i in koord])
        for i in self.jatek_szavak.keys():
            if self.szavak_adatbazis[i] == szo:
                self.av_szolista.szovegek[szo].szin = (255,0,0)
                self.jatek_szavak[i][1] == True
                self.jatek_adatok["pont"] += 1