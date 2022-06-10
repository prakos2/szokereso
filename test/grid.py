import pygame as pg
import math
import random

pg.init() 
res = (pg.display.Info().current_w, pg.display.Info().current_h)
wres = (res[0]//1.5, res[1]//1.5)
screen = pg.display.set_mode(wres)
fps = 60
clock = pg.time.Clock()
delta2 = 50
N = 8
eger_le = False
selection = []
betuk = [[chr(random.randint(70,100)) for x in range(N)] for j in range(N)]
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
        elif i.type == pg.MOUSEBUTTONDOWN:
            eger_le = True
        elif i.type == pg.MOUSEBUTTONUP:
            eger_le = False
            selection = []
    N = pg.time.get_ticks()//1000
    clock.tick(fps)
    pg.display.update()
    screen.fill((169,52,12))
    #print((pg.mouse.get_pos()[0]-wres[0]/4)//(wres[0]/(2*N)),(pg.mouse.get_pos()[1]-delta2)//((wres[1]-delta2*2)//N))
    if eger_le:
        coords = (math.trunc(pg.mouse.get_pos()[0]-wres[0]/4)//(wres[0]/(2*N)), math.trunc(pg.mouse.get_pos()[1]-delta2)//((wres[1]-delta2*2)//N))
        if coords not in selection:
            selection.append(coords)
    for i in range(N):
        for j in range(N):
            if (i,j) in selection:
                color = (255,0,0)
            else:
                color = (0,0,0)
            pg.draw.rect(
                screen,
                color,
                pg.Rect(
                    wres[0]/4+i*(wres[0]/(2*N)), 
                    delta2+(j*(wres[1]-delta2*2)/N), 
                    wres[0]/(2*N), 
                    (wres[1]-delta2*2)/N),
                1
            )