import pygame as pg


class Player():
    def __init__(self, position=[0, 0], size=32, color=(255, 0, 0)):
        self.pos = position
        self.color = color
        self.size = size

        self.DIED = False

    def draw(self, window):
        pg.draw.circle(window, self.color, self.pos, self.size)

    def update(self, window, rects):
        x, y = pg.mouse.get_pos()
        self.pos = [x, y]

        collisions = pg.draw.circle(window, (255, 255, 255), self.pos, 31).collideobjects(rects)
        
        if collisions != None:
            self.DIED = True

        self.draw(window)