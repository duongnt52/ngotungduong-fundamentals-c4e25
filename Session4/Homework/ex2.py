prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for i in prices:
    print(i)
    print("prices:", prices[i])
    print("stock:", stock[i])
    print()

total = 0
for i in prices:
    gia = prices[i] * stock[i]
    total += gia
print("Would Money: ", total)