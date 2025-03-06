import pygame as pg
from settings import WINDOW_SIZE


class Pipe():
    def __init__(self, position=[0, 0], color=(0, 255, 0)):
        self.pos = position
        self.color = color

        self.W, self.H = 16, 48

        self.speed = 3

    def draw(self, window):
        pg.draw.rect(window, self.color, [self.pos[0], 0, self.W, self.pos[1]-self.H])
        pg.draw.rect(window, self.color, [self.pos[0], self.pos[1]+self.H, self.W, WINDOW_SIZE[1]-self.pos[1]-self.H])

    def update(self, window, deltaFPS):
        self.pos[0] -= self.speed * deltaFPS

        self.draw(window)

        return [pg.Rect(self.pos[0], 0, self.W, self.pos[1]-self.H), pg.Rect(self.pos[0], self.pos[1]+self.H, self.W, WINDOW_SIZE[1]-self.pos[1]-self.H)]