from flask import Flask, request, render_template
app = Flask(__name__)

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
        print(t, l)
        return "POST"

        
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