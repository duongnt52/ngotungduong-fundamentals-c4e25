import random
# dung ham choice cho 1 list, cho 2 kq = 0 ty le win cao hon
# choice[-1, 0, 0, 1]
x = random.randint(0, 10)
y = random.randint(0, 10)
op = random.choice(["x", "-", "*", "/"])
error = random.randint(-2, 2)
kq = x + y + error
print(x, op, y, "=", kq)
user_input = input("Your answer(Y/N?) ").upper()
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