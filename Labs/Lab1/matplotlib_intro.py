from matplotlib import pyplot
# 1. Prepape Data (Chuẩn bị data)
machine_counts = [18, 4, 2]

# 2. Prepape Lebels
machine_names = ["PC", "MAC", "Linux"]

# 3. Draw pie
pyplot.pie(machine_counts, labels=machine_names, autopct="%1.1f%%", shadow=True, explode=[0, 0.15, 0])
pyplot.title("PC vs MAC vs Linux usage")
pyplot.axis("equal")

# 4. Show
pyplot.show()
