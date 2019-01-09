from random import randint
x = randint(1, 100)
print(x)
n = int(input("moi ban doan so"))
while x!=n:
    if n >  x:
        print("A little too big")
    elif n < x:
        print("A little too small")
    n = int(input("moi ban doan so"))
print("Bingo")