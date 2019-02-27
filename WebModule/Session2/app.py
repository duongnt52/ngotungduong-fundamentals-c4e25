from flask import Flask, request, render_template, redirect, flash, session
# import mlab
import user_mlap
from models.food import Food
from models.user import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "asdasdasda"

user_mlap.connect()
# mlab.connect()


@app.route('/login', methods=["GET" ,"POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        u = form['username']
        p = form['password']
        user = User.objects(username=u).first() # lọc ra những dữ liệu cần (filter) (truy cập 1 lần) #first tìm ra user đầu tiên
        print(user)
        if user != None:
            # user ton tai
            # check password
            print(user.password, p)
            if user.password == p:
                session["token"] = u
                return redirect('/menu')
            else:
                flash("Invalid password")
                return render_template("login.html")
        else:
            flash("User not found")
            return render_template("login.html")
        # for user in users:
        #     if user.username == u:
        #         return "OKK"
        #     else:
        #         return "NOT OK"

@app.route('/logout')
def logout():
    if "token" in session:
        del session["token"]
        return redirect('/login')
    else:
        return redirect('/login')



@app.route('/menu')
def menu():
    if "token" in session:
        food_objects = Food.objects()
        return render_template('menu.html', food_list=food_objects)
    else:
        return "Forbidden"


@app.route('/food/<food_id>')
def food_detail(food_id):
    f = Food.objects().with_id(food_id)
    # Invalid Id, Not found
    # if f = None:
    #     print("Not found")
    return render_template("food_detail.html", food=f)


@app.route('/update_food/<food_id>', methods=["GET", "POST"])
def update_food(food_id):
    f = Food.objects().with_id(food_id)
    if request.method == "GET":
        return render_template("update_food_form.html", food=f)
    elif request.method == "POST":
        form = request.form
        t = form["title"]
        l = form["link"]
        # Update - Automic Update
        f.update(set__title=t, set__link=l)
        return "OK"


# 1. Open both  methods: GET, POST
@app.route('/add_food', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('food_form.html')
    elif request.method == "POST":
        form = request.form
        # print(form)
        t = form['title']
        l = form['link']
        f = Food(title = t, link = l)
        f.save()
        return redirect("/food/" + str(f.id))

        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        u = form['username']
        p = form['password']
        print(u, p)
        return 'OK'



if __name__ == '__main__':
  app.run(debug=True)


