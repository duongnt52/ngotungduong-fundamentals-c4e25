import user_mlap
from models.user import User

user_mlap.connect()
u = User(username="admin", password="admin1")
u.save()