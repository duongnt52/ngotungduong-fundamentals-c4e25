#Routing
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, I'm again"  

@app.route("/c4e25")
def c4e25():
    return "This is C4E25, happy coding !!!!"

@app.route("/hi/quan")
def hi_quan():
    return "Hello Quan"

@app.route("/hi/<name>")
def hi(name):
    return "Hi " + name + ". Have a nice day"

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    return str(x + y)

@app.route("/simple_html")
def simple_html():
    return "<h3>Simple, indeed</h3>"

@app.route("/html")
def html():
    return render_template("sample.html")

food_list = [
    "Bún đậu",
    "Bún chả",
    "Gà rán",
    "Nem lụi"
]

@app.route("/menu")
def menu():
    return render_template("menu.html", food_list=food_list)

@app.route("/food/<int:index>") # detail  (trang con)
def food(index):
    return render_template("food.html",title= food_list[index])

detail = {
    'title': 'Bún chả',
    'image': 'http://www.savourydays.com/wp-content/uploads/2016/08/c%C3%A1ch-l%C3%A0m-b%C3%BAn-ch%E1%BA%A3-banner.jpg.jpg'
}

@app.route("/food_detail")
def food_detail():
    return render_template("food_detail.html", detail=detail)

if __name__ == '__main__':
  app.run(debug=True)