import mlab
from food import Food

mlab.connect()

        # 1. Create
# B1: Create a food
f = Food(title="Banh sai", link="<<link sai>>")
# B2: Save it
# f.save()

         # 2. Read
# B1: Get cursor
f_objects = Food.objects() # Lazy loading # Same as list
# B2: Process cursor
# f_first = f_objects[0] # Thực sự truyền dữ liệu
# print(f_first.title)
# print(f_first.link)

# print(len(f_objects))
# print(f_objects.count()) # Bảo database đếm

# for f in f_objects:
#     print(f.title)
#     print(f.link)
#     print("----------------")

# f = f_objects[4]
# f.update(set__title= "Banh rat rat ngon", set__link= "Link ngon") 
#             #op__prop: hành động __ cần thay đổi
#             # chỉ xảy ra trong database
# f.reload()
# print(f.title)
# f.delete()

f = f_objects.with_id("5c4d7d930dd5311e8833223d") # 1
if f != None:
    f.delete()
else:
    print("Not found")