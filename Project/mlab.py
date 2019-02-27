import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds337985.mlab.com:37985/c4e25-foods

# 1. Connect
host = "ds337985.mlab.com"
port = 37985
db_name = "c4e25-foods"
user_name = "admin"
password = "admin1"

# 1.2 Design file food.py

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())