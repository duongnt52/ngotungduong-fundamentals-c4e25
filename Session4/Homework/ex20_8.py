strings = input("Enter string: ").lower()
read_string = {}
for i in strings:
    read_string[i] = read_string.get(i, 0) + 1
del read_string[" "]
for k, v in sorted(read_string.items()):       
    print(k, " ", v)
# from operator import itemgetter #sap xep value
# myDic={10: 'b', 3:'a', 5:'c'}
# for k, v in sorted(myDic.items(), key = itemgetter(1), reverse = False):
#     print(k, v)