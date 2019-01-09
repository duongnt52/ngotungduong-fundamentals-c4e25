yob_str = input("Your year of birth? ")

while not yob_str.isdigit(): # neu nguoi dung nhap sai
    print("Not a number, enter again") # in ra 
    yob_str = input("Your year of birth? ") # nhap lai
  
yob = int(yob_str)
age = 2018 - yob
print(age)
