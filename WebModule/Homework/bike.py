from mongoengine import Document, StringField, IntField
# Design cấu trúc của dữ liệu
class Bike(Document): # Food kế thừa từ class Document
    model = StringField()
    daily_fee = IntField()
    img = StringField()
    year = IntField()