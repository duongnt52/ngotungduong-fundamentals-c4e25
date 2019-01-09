x = int(input("x = "))
print("Enter x number: ",x)
for i in range(1, x + 1):
    if i % 2 == 0:
        print("*", end="")
    else:
        print(" x ", end="")   