import random
from calc import eval

# Sinh bieu thuc
x = random.randint(0, 10)
y = random.randint(0, 10)
error = random.choice([-2, -1, 0, 0, 0, 1, 2, 3])
op = random.choice(["+", "-", "*", "/"])
kq = eval(x, y, op) + error
print(x, op, y, "=", kq)
user_input = input("Your answer (Y/N)").upper()
result = ""
if error == 0:
    if user_input == "Y":
        result = "Yay"
    elif user_input == "N":
        result = "Nay"
else:
    if user_input == "Y":
        result = "Wrong"
    elif user_input == "N":
        result = "Yay"
print(result)