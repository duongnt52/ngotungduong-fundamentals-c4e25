loop_count = 0
loop = True
while loop:
    print("Hi")
    loop_count += 1
    print(loop_count)
    if loop_count >= 3:
        loop = False