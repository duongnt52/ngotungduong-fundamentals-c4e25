from flask import Flask, render_template, request
app = Flask(__name__)
import database
from bike import Bike
@app.route('/bike', methods=["GET", "POST"])
def bike():
    if request.method == "GET":
        return render_template('bike.html')
    elif request.method == "POST":
        database.connect()
        form = request.form
        model = form['model']
        daily_fee = form['daily_fee']
        img = form['img']
        year = form['year']
        b = Bike(model = model, daily_fee = int(daily_fee), img = img, year = int(year))
        b.save()
        print(model, daily_fee, img, year)
        return "OK"
  
if __name__ == '__main__':
  app.run(debug=True)