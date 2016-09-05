import datetime

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TIMESTAMP, INTEGER

from app import db


class BoardModel(db.Model):
    __tablename__ = 'boards'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = Column(
        INTEGER(20, unsigned=True),
        primary_key=True
    )
    name = Column(
        String(80),
        unique=True,
        nullable=False
    )
    title = Column(
        String(100),
        nullable=False
    )
    created_date = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow()
    )
