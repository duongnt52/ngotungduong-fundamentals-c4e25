# 1. so ngau nhien 1 - 100
# 2. cho nguoi dung doan
# 3. dung - bingo, sai - doan lai
from random import randint
x = randint(0, 100)
loop = True
while loop:
    y = int(input("Moi ban doan so: "))
    if y < x:
        print("So ban doan nho hon x")
        loop = True
    elif y > x:
        print("So ban doan lon hon x")
        loop = True
    else:
        print("Bingo!")
        loop = False
