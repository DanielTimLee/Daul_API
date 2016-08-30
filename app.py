from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/login',methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == '1234':
        return "Hi Admin!!"
    else:
        return "Back Off Stranger!!"

app.run(host='0.0.0.0',port=8880,debug=True)
