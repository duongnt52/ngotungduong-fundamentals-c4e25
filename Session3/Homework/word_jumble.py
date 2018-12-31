from random import randint
word = "champion"
a = list(word)
for i in range(len(a)):
    b = randint(0, len(a) - 1)  # lay ngau nhien so tu 0 - (len(a))
    a.append(a[b])              # them gia tri o tri random "b" vao cuoi list
    a.pop(b)                    # moi khi them moi gia tri o vtri "b" thi xoa di phan tu o vi tri "b" truoc do
print(*a)
loop = True
user = input("Your answer: ")
while loop:
    if user == word:
        print("Hura")
        loop = False
    else:
        print(":(")
        loop = True
        user = input("Your answer: ")
    

#print(list(a[random.randint(0, 2)]))
# print(a)
# print(b)
# print(len(a))
