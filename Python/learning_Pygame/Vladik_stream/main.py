import pygame as pg
import random
import objects.colors as colors
from settings import *
from objects.player import Player
from objects.pipe import Pipe


pg.font.init()


window = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption(WINDOW_NAME)
font = pg.font.SysFont('Comic Sans MS', 30)

clock = pg.time.Clock()
runGame = True
score = 0
tick = 0

player = Player((640, 360))
pipes = []


run = True
while run:
    clock.tick(MAXFPS)
    fps = clock.get_fps()

    if fps>0:
        deltaFPS = MAXFPS/fps
    else:
        deltaFPS = 0

    if player.DIED:
        run = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if tick/MAXFPS >= score and runGame:
        pipes.append(Pipe([WINDOW_SIZE[0], random.randint(48, WINDOW_SIZE[1]-48)]))
        score += 1


    window.fill(colors.BLACK)

    rects = []
    for pipe in pipes:
        rcts = pipe.update(window, deltaFPS)
        rects.append(rcts[0])
        rects.append(rcts[1])

    player.update(window, rects)

    text = font.render(str(score), False, colors.WHITE)
    window.blit(text, (8, 0))

    pg.display.update()

    for pipe in pipes:
        if pipe.pos[0] < -pipe.W:
            pipes.pop(0)

    tick += deltaFPS

pg.quit()
exit()