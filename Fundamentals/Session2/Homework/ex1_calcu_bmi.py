h = int(input("Your height(kg): "))
w = int(input("Your weight(cm): "))
if h and w > 0:
    BMI = h / (w*w*0.0001)
    print("Your BMI is: ",round(BMI, 1)) #lam tron den so thu 2
    if BMI < 16:
        print("Severely underweight :((!")
    elif BMI < 18.5:
        print("Underweight :(")
    elif BMI < 25:
        print("Normal :D")
    elif BMI < 30:
        print("Overweight !")
    else:
        print("Obese @@")
else:
    print("Wrong input values :)")


