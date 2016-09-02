import datetime

from flask import render_template, request, jsonify

from app import app, db
from app.models.user import UserModel


@app.route('/users/<string:username>')
def user(username):
    user = UserModel.query. \
        filter_by(username=username). \
        first()

    if user is None:
        raise Exception('Not Found!')

    else:
        return render_template('index.html', user=user)


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
