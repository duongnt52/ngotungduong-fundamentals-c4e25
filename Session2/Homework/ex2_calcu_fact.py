n = int(input("Nhap n = "))
s = 1
for i in range(1, n + 1):
    s *= i
print("The factorial of", n, "is:", s)