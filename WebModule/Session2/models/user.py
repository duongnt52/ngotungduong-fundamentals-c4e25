from mongoengine import Document, StringField
# Design cấu trúc của dữ liệu
class User(Document): # Food kế thừa từ class Document
    username = StringField()
    password = StringField()