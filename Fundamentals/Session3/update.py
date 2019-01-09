favs = ["quan", "ao", "giay", "mu"]
print("Danh sách các món đồ yêu thích của bạn!\n ", favs)
i = int(input("Bạn muốn thay đổi món đồ nào? "))
new_items = input("Món đồ mới bạn muốn đổi là: ")
favs[i - 5] = new_items
print(favs)
