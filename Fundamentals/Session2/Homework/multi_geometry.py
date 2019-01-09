from turtle import *
fillcolor("red")
for i in range(3,7):
    if i % 2 == 0:
        pencolor("red")
    else:
        pencolor("blue")
    x = i
    for j in range(x):
        fd(100)
        lt(360/x)
mainloop()    