import pyglet as gl

class DOT():
    def __init__(self):
        self.size = 32
        self.Vector = [1, 1]
        self.Position = [self.size+1, self.size+1]
    def update(self):
        if self.Position[0] >= 960-self.size:
            self.Vector[0] *= -1
        elif self.Position[0] <= self.size:
            self.Vector[0] *= -1

        if self.Position[1] >= 540-self.size:
            self.Vector[1] *= -1
        elif self.Position[1] <= self.size:
            self.Vector[1] *= -1

        self.Position[0] += self.Vector[0]
        self.Position[1] += self.Vector[1]
    def draw(self):
        gl.shapes.Circle(self.Position[0], self.Position[1], self.size).draw()

window = gl.window.Window()
dots = [DOT()]

@window.event
def on_draw():
    window.clear()
    for dot in dots:
        dot.draw()
        dot.update()

gl.app.run()