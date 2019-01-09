from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds121248.mlab.com:21248/c4e25"

# 1. Connect to mLab
client = MongoClient(uri)

# 2. Get a database
db = client.get_database()

# 3. Get a collection
post_collection = db["posts"]

# 4. Create a document
new_post = {
    "title": "Hôm nay trời nhiều mây", # field title(trường)
    "content": "Tôi ra đường, à mà thôi ở nhà code", # field title
}
# 5. Insert document
# post_collection.insert_one(new_post)

# Lazy Loading
post_list = post_collection.find() # Cursor(con trỏ)
# fist_post = post_list[1]
# print(fist_post)
for p in post_list:
    print(p)
# 6. Close connection
client.close()

