# x = int(input("nhap x = "))
# y = int(input("nhap y = "))
# op = input("nhap phep tinh + - * / : ")

def eval(x, y, op):
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        if y == 0:
            pass
        else:
            result = x/y
    return result
# a = int(input("a = "))
# b = int(input("b = "))
# op = input("op = ")

# r = eval(a, b, op)
# print(r)



# def sayHi(n):
#     print("Hi")
#     print("Hi", n)
#     print("Bye Bye")
# def add(x, y):
#     r = x + y
#     return r
# s = add(5, 5)
# print(s)
# t = add(6, 7)
# print(t)