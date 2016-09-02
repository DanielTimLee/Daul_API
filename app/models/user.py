import datetime

from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.sql.expression import text

from app import db


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
