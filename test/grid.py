import pygame as pg
pg.init() 
res = (pg.display.Info().current_w, pg.display.Info().current_h)
wres = (res[0]//1.5, res[1]//1.5)
screen = pg.display.set_mode(wres)
fps = 60
clock = pg.time.Clock()
delta2 = 50
N = 8
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
    clock.tick(fps)
    pg.display.update()
    screen.fill((169,52,12))
    pg.draw.rect(screen, (0,0,0), pg.Rect(wres[0]/4, delta2, wres[0]/2, wres[1]-(delta2*2)), 2)
    for i in range(N):
        for j in range(N):
            pg.draw.rect(
                screen,
                (255,255,255),
                pg.Rect(
                    wres[0]/4+i*(wres[0]/(2*N)), 
                    delta2+(j*(wres[1]-delta2*2)/N), 
                    wres[0]/(2*N), 
                    (wres[1]-delta2*2)/N
                    ),
                1
            )