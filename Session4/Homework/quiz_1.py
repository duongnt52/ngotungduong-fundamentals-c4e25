answer = {
    "1. : 35 \n2. : 36 \n3. : 40 \n4. : 44" : 4
}
print("Answer the following algebra question:")
print("If x = 8, then what the value of 4(x + 3) ?")
for k in answer:
    print(k)
user = int(input("Your choice: "))
loop = True
while loop:
    if user != answer[k]:
        print(":(")
        loop = True
        user = int(input("Your choice: "))
    else:
        print("Bingo")
        loop = False