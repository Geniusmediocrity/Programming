import pygame as pg
from pygame.examples.go_over_there import delta_time

NAME = " ИГРА"
W,H = 1360,720
MAXFPS = 60
window = pg.display.set_mode((W,H))
pg.display.set_caption(NAME)
clock = pg.time.Clock()
run = True
while run:
    clock.tick()
    fps = clock.get_fps()
    try :
        delta = MAXFPS/fps
    except:
        delta = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    window.fill((70,80,2))
    pg.display.update()
pg.quit()
exit()