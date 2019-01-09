# from random import randint
# n = randint(-99, 100)
# list_number = []
# for i, num in enumerate(n):
#     list_number.append(num)
# print(list_number)
#for i, num in enumerate()
import random
nums = []
for i in range(4):
        nums.append(random.randint(-99, 100))
print(nums)
min_num = 9999
for index, i in enumerate(nums):
    if i < min_num:
        min_num = i
        min_index = index
print(min_num)
print(min_index)