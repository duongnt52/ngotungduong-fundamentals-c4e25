items = ["T-Shirt", "Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
loop = True
while loop:
    if n == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items: ", end="")
        print(*items, sep = ", ")
        loop = True
        n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    elif n == "R":
        print("Our items: ", end="")
        print(*items, sep = ", ")
        loop = True
        n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    elif n == "U":
        for (i, val) in enumerate(items):
            print(i + 1, val, end = " ")
        update = int(input("\nUpdate position? "))
        new_item = input("New item? ")
        items[update - 1] = new_item
        print("Our items: ", end="")
        print(*items, sep = ", ")
        loop = True
        n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    elif n == "D":
        for (i, val) in enumerate(items):
            print(i + 1, val, end = " ")
        delete = int(input("\nDelete position? "))
        items.pop(delete - 1)
        print("Our items: ", end="")
        print(*items, sep = ", ")
        loop = True
        n = input("Welcome to our shop, what do you want (C, R, U, D)? ")       
    else:
        q = input("You wanna Quit? Y/N? ")
        if q == "N" or q == "n":
            loop = True
            n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
        elif q == "Y" or q == "y":
            loop = False    

