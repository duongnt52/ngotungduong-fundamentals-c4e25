sheep_size = [10, 56, 4, 9, 100, 350, 25, 142, 347, 92]
print("Hello, my name is Duong and these are my sheep sizes\n", sheep_size)
print()
for k in range(1,4):
    for (i, val) in enumerate(sheep_size):
        sheep_size[i] = val + 50
    print("Month", k, ": \nOne month has passed, now here's my flock\n", sheep_size, sep = "")
    m = max(sheep_size)
    print("Now biggest sheep has size", m, "let's shear it")
    for (i,x) in enumerate(sheep_size):  # lay vi tri cua max number
        if x == m:                       # c2 : dung shep_size.index(max(sheep_size))
            sheep_size[i] = 8
    print("After shearing, here is my flock", sheep_size, sep = "")
    print()
for (i, val) in enumerate(sheep_size):
    sheep_size[i] = val + 50
print("Month 4: \n", "One month has passed, now here's my flock\n", sheep_size, sep = "")
print()
s = sum(sheep_size)
print("My flock has size in total: ",s)
money = s * 2
print("I would get ", s, " * ", "2$ = ", money, "$", sep = "")