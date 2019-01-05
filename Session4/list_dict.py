p1 = {
    "name": "Quan",
    "age": 25
}
p2 = {
    "name": "Linh",
    "age": 25
}

p3 = {
    "name": "Long",
    "age": 21
}


p_list = []

p_list.append(p1)

print(p_list)
p_list.append(p2)

print(p_list)
p_list.append(p3)
print(p_list)

# p_first = p_list[0]
# print(p_first)
# print(p_first["name"])

for p in p_list:
    print(p["name"], p["age"])