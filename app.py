import datetime

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.sql.expression import text

app = Flask(__name__)
app.config.from_object('config')

db=SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True)
    created_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow(),
        server_default=text('CURRENT_TIMESTAMP')
    )

db.create_all()

@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/users/<string:username>')
def user(username):
    return render_template('index.html',name=username)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_user = UserModel(
            username=request.form.get('username'),
            password=request.form.get('password'),
            email=request.form.get('email'),
            created_date=datetime.datetime.utcnow()
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'success': True,
            'messages': [
                '회원가입에 성공했습니다. 다시 로그인해 주세요!!'
            ]
        })

    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':

        user = UserModel.query. \
            filter_by(username=request.form.get('username')). \
            filter_by(password=request.form.get('password')). \
            first()

        if user is None:
            raise Exception('Not Found!')
        else:
            return jsonify({
                'success': True,
                'messages': [
                    '로그인에 성공하셨습니다!'
                ]
            })

    return render_template('signin.html')

app.run(host='0.0.0.0',port=8880,debug=True)
