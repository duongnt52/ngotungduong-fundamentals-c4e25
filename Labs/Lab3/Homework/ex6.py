from turtle import *
from ex5 import draw_star
speed(0)
cl = ["blue", "red", "yellow", "green"]
for i in range(100):
    import random
    color(random.choice(cl))
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)