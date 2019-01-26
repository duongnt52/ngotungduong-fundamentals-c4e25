from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"
users = {
    'hao':  {
                "name": "Hoàng Anh Hào",
                "yob": 1997,
                "hobby": "playing football"

            },
    'an':   {
                "name": "Nguyễn Ngọc An",
                "yob": 1997,
                "hobby": "sing"
            },
    'bau':  {
                "name": "Ngọ Tùng Dương",
                "yob": 1997,
                "hobby": "guitar"
            }
}
@app.route('/user/<username>')
def user(username):
    user1 = {}
    for k, v in users.items():
        if k.lower() == username:
            for key, value in v.items():
                user1[key] = value
    if username not in users:
        return "<h1>User not found</h1>"
    else:
        return render_template('user.html', user = user1)
if __name__ == '__main__':
  app.run(debug=True)