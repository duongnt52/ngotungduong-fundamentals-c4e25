from mongoengine import Document, StringField
# Design cấu trúc của dữ liệu
class Food(Document): # Food kế thừa từ class Document
    title = StringField()
    link = StringField()