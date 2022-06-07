import pygame as pg
pg.init() 
res = (pg.display.Info().current_w, pg.display.Info().current_h)
wres = (res[0]//1.5, res[1]//1.5)
screen = pg.display.set_mode(wres)
fps = 60
clock = pg.time.Clock()
N = 16
lambda_val = 50
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
    clock.tick(fps)
    pg.display.update()
    screen.fill((169,52,12))
    pg.draw.rect(screen, (0,0,0), pg.Rect((wres[0]/2)/2, lambda_val, (wres[0]/2), (wres[1]-lambda_val*2)), 2)
    #print(str((pg.mouse.get_pos()[0]-((wres[0]/2)/2))//159))
    for i in range(N):
        for j in range(N):
            print(j)
            pg.draw.rect(
                screen,
                (255,255/(i+1),255/(i+1*2)),
                pg.Rect(((wres[0]/2)/2)+(i*((wres[0]/2)/N)), lambda_val, (wres[0]/2)/N, (wres[1]-lambda_val*2)/N),
            )