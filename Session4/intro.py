         #name  age  location exes status friends 
person = ["Quan", 25, "Hanoi", 3, False, 125]
# Kho hieu


# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "Quan"
# }
# print(person)

person = {
    "name": "Quan",
    "age": 25,
    "location": "Hanoi",
    "exes": 3,
    "status": False,
    "friend": 125,
}
person["name"] = "A.Quan" # update
person["exp"] = 2 # create
# neu key ton tai thi la UPDATE, con k CREATE


# kiem tra xem tu ngu co ton tai hay ko!
# if "name" in person:
#     print("Exists")
# else:
#     print("Not exists")