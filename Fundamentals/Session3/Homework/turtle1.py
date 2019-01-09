from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]
x = 3
for i in colors:
    color(i, i)
    for u in range(x):
        fd(100)
        lt(360/x)
    x += 1    
exitonclick()
