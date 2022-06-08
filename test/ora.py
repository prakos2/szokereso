import pygame as pg
pg.init()
FELBONTAS=(pg.display.Info().current_w, pg.display.Info().current_h)
KEPERNYO=pg.display.set_mode((FELBONTAS[0]//1.5, FELBONTAS[1]//1.5))
fps=60
ora=pg.time.Clock()
BETUTIPUS=pg.font.SysFont('Consolas', 30)
perc_szoveg=''
masodperc_szoveg=''
while True:
    cl = pg.time.Clock()
    t = 650
    cl.tick(60)
    ct = pg.time.get_ticks()//1000
    perc_szoveg=(t-ct)//60
    masodperc_szoveg=(t-ct)%60
    KEPERNYO.fill((0,0,0))
    if perc_szoveg>=10:
        if masodperc_szoveg>=10:
            KEPERNYO.blit(BETUTIPUS.render(f"{perc_szoveg}:{masodperc_szoveg}", True, (255,255,255)), (32, 48))
        else:
            KEPERNYO.blit(BETUTIPUS.render(f"{perc_szoveg}:0{masodperc_szoveg}", True, (255,255,255)), (32, 48))
    else:
        if masodperc_szoveg>=10:
            KEPERNYO.blit(BETUTIPUS.render(f"0{perc_szoveg}:{masodperc_szoveg}", True, (255,255,255)), (32, 48))
        else:
            KEPERNYO.blit(BETUTIPUS.render(f"0{perc_szoveg}:0{masodperc_szoveg}", True, (255,255,255)), (32, 48))
        
    ora.tick(fps)
    pg.display.update()