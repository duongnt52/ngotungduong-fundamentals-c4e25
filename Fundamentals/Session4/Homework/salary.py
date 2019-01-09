a = {
    "name": ["Huy", "Quan", "Duc"],
    "salary": [25, 25, 30],
    "hour": [30, 20, 40],
}
s = 0
total = 0
for i in a["salary"]:
    salary_perhour = i * a["hour"][s]
    print("Luong hang tuan cua", a["name"][s], "la:", salary_perhour)
    s += 1
    total += salary_perhour

print("Tong luong:", total)

