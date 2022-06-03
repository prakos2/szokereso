import pygame

pygame.init()

ablak=pygame.display.set_mode((128, 128))

ora=pygame.time.Clock()

masodperc_szamlalo=5
masodperc_szoveg=str(masodperc_szamlalo)
perc_szamlalo=2
perc_szoveg=str(perc_szamlalo)

pygame.time.set_timer(pygame.USEREVENT, 1000)

BETUTIPUS=pygame.font.SysFont('Consolas', 30)

while True:
    if masodperc_szamlalo!=0:
        for i in pygame.event.get():
            if i.type==pygame.USEREVENT: 
                masodperc_szamlalo-=1
                if masodperc_szamlalo>0:
                    masodperc_szoveg=str(masodperc_szamlalo)
                else:
                    if perc_szamlalo!=0:
                        perc_szamlalo-=1
                        masodperc_szamlalo=60
                        if perc_szamlalo==0:
                            break
                    else:
                        break
        else:
            ablak.fill((0,0,0))
            ablak.blit(BETUTIPUS.render(f"{perc_szoveg}:{masodperc_szoveg}", True, (255,255,255)), (32, 48))
            pygame.display.flip()
            ora.tick(60)
            continue
        break
    break