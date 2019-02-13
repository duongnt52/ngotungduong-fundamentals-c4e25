import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds213755.mlab.com:13755/c4e25-web

# 1. Connect
host = "ds213755.mlab.com"
port = 13755
db_name = "c4e25-web"
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