from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return "Hello"
@app.route("/bmi/<int:h>/<int:w>")
def bmi(h, w):
    BMI = round(h / (w*w*0.0001), 1)
    return render_template("bmi.html", BMI = BMI)
@app.route("/BMI/<int:w>/<int:h>")

# Without render_template
def BMI(w, h):
    h1 = h / 100
    BMI = w / (h1*h1)
    if BMI < 16:
        return "Severely underweight"
    elif BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
        return "Normal"
    elif BMI < 30:
        return "Overweight"
    else:
        return "Obese"  
if __name__ == '__main__':
  app.run(debug=True)