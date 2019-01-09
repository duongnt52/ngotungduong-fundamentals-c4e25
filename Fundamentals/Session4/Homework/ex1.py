inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print(inventory)
#   Add a key to inventory called 'pocket'.
inventory["pocket"] = ["seashell", "strange berry", "lint"]
print(inventory)
#   remove "dagger"
inventory["backpack"].remove("dagger")
print(inventory)
#   add 50
inventory["gold"] += 50
print(inventory)