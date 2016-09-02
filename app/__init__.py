from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# 이런식으로 임포트 해도 됨 (url중 __all__ 참조)
# from app.models import user , ...
# https://wikidocs.net/1418#all

from app.models import *

db.create_all()

from app.routes import *
