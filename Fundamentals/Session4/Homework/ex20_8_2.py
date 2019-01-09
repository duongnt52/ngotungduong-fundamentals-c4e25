import collections
user = input("Enter string: ").lower()
count = collections.Counter(user)
del count[" "]
for k, v in sorted(count.items()):
    print(k, v, sep = "  ")

