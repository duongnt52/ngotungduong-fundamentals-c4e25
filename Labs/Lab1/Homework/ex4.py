from pymongo import MongoClient
url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(url)
db = client.get_database()
post_collection = db["customers"]
ads = 0
events = 0
worn = 0
post_list = post_collection.find()
for i in post_list:
    a = i["ref"]
    if a == "ads":
        ads += 1
    if a == 'events':
        events += 1
    if a == 'wom':
        worn += 1
print(ads, events, worn)
client.close()