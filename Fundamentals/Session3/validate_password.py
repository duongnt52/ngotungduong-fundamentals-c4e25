# lon hon 8 ky tu
# co ca so va chu
# co chu hoa chu thuong
loop = True
while loop:
    pwd = input("Your password: ")
    loop = False # assume password is valid
    if len(pwd) < 8:
        print("Password length must be greater than 8")
        loop = True
    if not pwd.isalnum():
        print("Password must not contain special characters")
        loop = True
    if pwd.isdigit():
        print("Password must contain letter")
        loop = True
    if pwd.isalpha():
        print("Password must contain digit")
        loop = True
    if pwd.isupper():
        print("Password must contain lower")
    if pwd.islower():
        print("Password must contain upper")    
print("Password OK")  