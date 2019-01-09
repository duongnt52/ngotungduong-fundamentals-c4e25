from matplotlib import pyplot

count = [1938, 3902, 1132]
references = ["Advertisements", "Events", "Word of Mouth"]

pyplot.pie(count, labels=references, autopct="%.1f%%", shadow=True, explode=[0, 0, 0.15])
pyplot.title("References of customers")
pyplot.axis("equal")
pyplot.show()