from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
     return render_template('index.html')

@app.route("/index.html")
def hello1():
     return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

@app.route("/data-input")
def datainput():
    return render_template('Data-Input.html')

@app.route('/viewdata', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fullname = request.form.get('fname')
        age = request.form.get('age')
        
        return f'{fullname}, your age is {age}'
    return render_template('Data-Input.html')

@app.route('/viewdata1', methods=['GET', 'POST'])
def home1():
    if request.method == 'POST':
        fullname = request.form.get('fname')
        age = request.form.get('age')
        return render_template('Display-Data.html', fullname=fullname,age=age)
    

@app.route('/viewdata2', methods=['GET', 'POST'])
def home2():
    if request.method == 'POST':
        fullname = request.form.get('fname')
        age = request.form.get('age')
        return render_template('Display-Data1.html', fullname=fullname,age=int(age))
    if request.method == 'GET':
        return render_template('get-is-not-supported.html')