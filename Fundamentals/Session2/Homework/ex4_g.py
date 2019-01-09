n = int(input("n= "))
m = int(input("m= "))
print("Enter n: ", n,"\nEnter m: ", m, sep="")
for i in range(1, m*n + 1):
    print("* ", end="")
    if i % n == 0:
        print()