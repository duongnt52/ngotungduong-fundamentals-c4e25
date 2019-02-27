from flask import Flask, render_template, request, redirect, flash
import mlab
import random
from models.test_foods import Nang, Lanh, Mat, Mua

app = Flask(__name__)
mlab.connect()

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/sunny')
def sunny():
    a = random.choice(Nang.objects())
    return render_template('sunny.html', nang = a)

@app.route('/cool')
def cool():
    a = random.choice(Mat.objects())
    return render_template('cool.html', nang = a)

@app.route('/rainy')
def rainy():
    a = random.choice(Mua.objects())
    return render_template('rainy.html', nang = a)

@app.route('/coldy')
def coldy():
    a = random.choice(Lanh.objects())
    return render_template('coldy.html', nang = a)


if __name__ == '__main__':
  app.run(debug=True)