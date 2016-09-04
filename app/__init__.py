from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config.from_object('config')

db = SQLAlchemy(app)

from app.models import *

db.create_all()

from app.routes import *
