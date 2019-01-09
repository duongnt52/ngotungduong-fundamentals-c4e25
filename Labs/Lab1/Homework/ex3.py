from pymongo import MongoClient
url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(url)
db = client.get_database()
post_collection = db["posts"]
new_post = {
    "title": "C4E25",
    "author": "Ngo Tung Duong",
    "content": "- Trời ơi em ghét trời mưa.\n Ghét luôn màu tím chẳng ưa tý nào -\n Mặc dù trời mưa gió e vẫn đến học đều đặn, thích anh Huy và anh Quân rất nhiệt tình chỉ dạy"
}
post_collection.insert_one(new_post)

client.close