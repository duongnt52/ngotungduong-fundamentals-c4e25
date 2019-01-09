a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
c = float(input("Nhap c = "))
delta = b*b - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem!")
elif a == 0:
    x = -c/b
    print("Phuong trinh bac 1 co 1 nghiem la x = ",x)    
elif delta == 0:
    x = -b/(2*a)
    print("Phuong trinh co 1 nghiem x = ",x)
else:
    x1 = (-b + delta**0.5) / 2*a
    x2 = (-b - delta**0.5) / 2*a
    print("Phuong trinh co 2 nghiem la: \n x1 = ",x1, "\n x2 =",x2)