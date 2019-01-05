answer = {
    "Answer the following algebra question: \nIf x = 8, then what the value of 4(x + 3) \n1. : 35 \n2. : 36 \n3. : 40 \n4. : 44" : 4,
    "Estimate this answer (exact calculation not needed):\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? \n1. 55 \n2. 65 \n3. 75 \n4. 85" : 2
}
count = 0
for k in answer:
    print(k)
    user = int(input("Your choice: "))
    if user != answer[k]:
        print(":( \nThe correct answer is", answer[k], "\n")
    else:
        print("Bingo")
        count += 1
print("Your correctly answer", count, "out of", len(answer), "question")


    
