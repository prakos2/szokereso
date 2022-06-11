import pygame as pg
import Ablakvezerlo
import random
# Fájlkezeléshez
import sys
import os

class Jatekvezerlo():
    def __init__(self): 
        # Játékállás
        self.JATEKALLASOK = ("menu", "jatek", "vegeredmeny") # Sorrendben lévő játékállások
        self.jatekallas = self.JATEKALLASOK[0]               # Első lehetséges játékállás megadása
        self.MAX_SZINT = 12                                  # A játékon belül elérhető maximális szintek
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
        # Fájl elérési útja
        try:
            if sys.argv[1:3][0] == "-fajl" and os.path.isfile(sys.argv[1:3][1]):
                FAJL_UTVONAL = sys.argv[1:3][1]
        except:
            FAJL_UTVONAL = os.path.dirname(os.path.abspath(__file__)) + "\szavak.txt"

        try:
            with open(FAJL_UTVONAL, encoding="utf-8-sig") as SZAVAK_FAJL:
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
        '''
        Új rács generálása, megváltoztatja a grafikus elemeket is
        '''
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
        '''
        Új szintre lépés megadott rácsnövekedéssel
        '''
        try:
            # Új szólista generáció
            self.grid_list = self.uj_racs(leptek)
        except Exception as kivetel:
            # Lehet, hogy a játék sincs még elkezdve. Ilyenkor nem lehet szintet lépni.
            print(f"[H] Hiba történt az új szintre lépés közben: {str(kivetel)}")

    def s_uj_jatek(self, jatekablak: Ablakvezerlo.Ablak, grid_n=3, t=180):
        '''
        Új játék indítása, minden nullázódik
        '''
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
        '''
        A grafikus koordináták alapján hivatkozás a karakterkoordinátákra
        '''
        # Koordináták alapján ellenőrzés
        szo = "".join([str(self.av_grid.szolista[i[1]][i[0]]) for i in koord])
        for i in self.jatek_szavak.keys():
            # jatek_szavak.keys -> szó adatbázis indexek
            if self.szavak_adatbazis[i] == szo:
                # ha létező szó képződik
                self.av_szolista.szovegek[szo].szin = (255,0,0)
                self.jatek_szavak[i][1] = True
                self.jatek_adatok["pont"] += 1
        # Eddig a pályán megtalált szavak
        megtalalt_szavak = [self.jatek_szavak[x][1] for x in self.jatek_szavak.keys() if self.jatek_szavak[x][0] != False]
        if not False in megtalalt_szavak:
            # Ha minden szó meglett
            if self.jatek_adatok["szint"]+1 < self.MAX_SZINT:
                self.jatek_adatok["szint"] += 1
                self.s_uj_szint(self.av_grid.feloszt_meret+1)
            else:
                self.s_jatekallas("vegeredmeny")