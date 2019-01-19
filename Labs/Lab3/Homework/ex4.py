from turtle import *
from ex3 import draw_square
for i in range(30):
    draw_square(i * 5, 'blue')
    left(17)
    penup()
    forward(i * 2)
    pendown()

    