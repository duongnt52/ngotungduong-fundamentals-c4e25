from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]

for i in colors:
    pencolor(i)
    fillcolor(i)
    begin_fill()
    for j in range(2):
        fd(50)
        rt(90)
        fd(100)
        rt(90)
    fd(50)
    end_fill()

exitonclick()