from random import *
from calc import eval
def generate_quiz():
    # Hint: Return [x, y, op, result]
    a = randint(0, 10)
    b = randint(0, 10)
    error = choice([-2, -1, 0, 0, 0, 1, 2])
    op = choice(["+", "-", "*", "/"])
    s = eval(a, b, op)
    result = s + error
    return a, b, op, result
def check_answer(x, y, op, result, user_choice):
    if eval(x, y, op) == result:
        if user_choice == True:
            return True
        else:
            return False
    else:
        if user_choice == True:
            return False
        else:
            return True
    
