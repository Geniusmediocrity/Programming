import turtle


def drawing_squares(side):
    turtle.bgcolor("black")
    turtle.pencolor("red")
    turtle.speed(0)
    for _ in range(30):
        for _ in range(18):
            turtle.left(20)
            for _ in range(4):
                turtle.forward(side)
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

    def square(self) -> turtle:
        turtle.shape("square")
        for _ in range(4):
            turtle.forward(self.side)
            turtle.right(90)

    def equilateral_triangle(self) -> turtle:
        turtle.shape("triangle")
        for _ in range(3):
            turtle.forward(self.side)
            turtle.left(120)

    def nine_side(self) -> turtle:
        # turtle.Screen().addshape("rocket.gif")
        # turtle.shape("rocket.gif")
        turtle.shape("turtle")
        for _ in range(9):
            turtle.forward(self.side)
            turtle.left(45)


class GeometricShapes():

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def rectangle(self) -> turtle:
        for _ in range(4):
            turtle.forward(self.width)
            turtle.left(90)
            self.width, self.height = self.height, self.width


window = turtle.Screen()
turtle.showturtle()

# drawing_squares(100)
# EightSquares(100).eight_squares()

window.mainloop()
