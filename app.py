from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

db.create_all()

@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/users/<string:username>')
def user(username):
    return render_template('index.html',name=username)

@app.route('/login',methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == '1234':
        return "Hi Admin!!"
    else:
        return "Back Off Stranger!!"

app.run(host='0.0.0.0',port=8880,debug=True)
