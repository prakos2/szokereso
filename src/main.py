import pygame as pg

class Szokereso():
    """
    Inicializálás
    """
    def __init__(self):
        pg.init()
        self.FELBONTAS=self.SZELESSEG, self.MAGASSAG=(pg.display.Info().current_w, pg.display.Info().current_h) # A képernyő teljes mérete.
        self.ABLAK_MERET=(self.SZELESSEG/1.5, self.MAGASSAG/1.5)
        self.FPS=60
        self.KEPERNYO=pg.display.set_mode(self.ABLAK_MERET)
        self.ORA = pg.time.Clock()
        pg.display.set_caption("Szókereső")
    
    """
    Tickre változó függvény
    """
    def _folyamat(self):
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    return
            pg.display.flip()
            self.ORA.tick(self.FPS)

if __name__ == "__main__":
    jatek_peldany = Szokereso()
    jatek_peldany._folyamat()
    exit()