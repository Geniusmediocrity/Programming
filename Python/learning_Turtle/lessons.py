import turtle


class Flower:
    def __init__(self, side):
        self.side = side
    
    def drawing_squares(self):
        turtle.bgcolor("black")
        turtle.pencolor("red")
        turtle.speed(0)
        for _ in range(30):
            for _ in range(18):
                turtle.left(20)
                for _ in range(4):
                    turtle.forward(self.side)
                    turtle.left(90)
            side += 5

class EightSquares():
  
  def __init__(self, side):
    self.side = side
    
  def square(self):
    for _ in range(4):
      turtle.forward(self.side)
      turtle.left(90)

  def eight_squares(self):
    for _ in range(8):
      turtle.left(45)
      self.square()

class CorrectGeometricShapes():

    def __init__(self, side):
        self.side = side

    def square(self) -> turtle: # квадрат
        turtle.shape("square")
        for _ in range(4):
            turtle.forward(self.side)
            turtle.right(90)

    def equilateral_triangle(self) -> turtle:   # правильный треуголник
        turtle.shape("triangle")
        for _ in range(3):
            turtle.forward(self.side)
            turtle.left(120)

    def nine_side(self) -> turtle:  # девятиуголлник
        # turtle.Screen().addshape("rocket.gif")
        # turtle.shape("rocket.gif")
        turtle.shape("turtle")
        for _ in range(9):
            turtle.forward(self.side)
            turtle.left(45)
            
    def hexagon(self):
        for _ in range(6):
            turtle.forward(self.side)
            turtle.left(60)
            


class GeometricShapes():

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def rectangle(self) -> turtle:  # прямоугольник
        for _ in range(4):
            turtle.forward(self.width)
            turtle.left(90)
            self.width, self.height = self.height, self.width


class Honeycombs:
    def __init__(self, side, amount):
      self.side = side
      self.amount = amount
    
    def hexagon(self):
        for _ in range(6):
            turtle.forward(self.side)
            turtle.left(60)
            
    def honeycombs_draw(self):
        for _ in range(self.amount):
            self.hexagon()
            turtle.right(120)

            

window = turtle.Screen()
turtle.showturtle()


Honeycombs(50, 7).honeycombs_draw()

window.mainloop()
