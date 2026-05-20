# Program: Kaleido Spiral using Turtle Graphics library

import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'violet'])

def draw_circle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle - 20, shift - 10)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30, 0, 1)


# Once done you can make this changes for more outcomes:
# change line 13 to - draw_circle(size + 10, angle + 10, shift + 1)
#                   - draw_circle(size + 5, angle - 20, shift - 10)
#
# to make other shapes do this changes -
# def draw_shape(size, angle, shift, shape):
#   turtle.pencolor(next(colors))
#   next_shape = ''
#   if shape == 'circle':
#       turtle.circle(size)
#       next_shape = 'square'
#   elif shape == 'square':
#       for i in range(4):
#           turtle.forward(size * 2)
#           turtle.left(90)
#       next_shape = 'circle'
#   turtle.right(angle)
#   turtle.forward(shift)
#   draw_shape(size + 5, angle + 1, shift + 1, next_shape)
