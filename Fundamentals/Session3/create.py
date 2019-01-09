# initialite( khai bao ) 1 list
favs = ["quan", "ao", "giay", "mu"]
print("Hi there, here you favorite things so far:")
for i in favs:
    print(i, end=', ')
new_item = input("\nName one thing you want to add?")
favs.append(new_item)
print(favs)
