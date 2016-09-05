import datetime

from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.dialects.mysql import LONGTEXT, TIMESTAMP, INTEGER

from app import db


class DocumentModel(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    status_enum = ('public', 'block', 'hidden')

    id = Column(
        INTEGER(20, unsigned=True),
        primary_key=True
    )
    board_id = Column(
        INTEGER(20, unsigned=True),
        ForeignKey('boards.id')
    )
    title = Column(
        String(250),
        nullable=False
    )
    content = Column(
        LONGTEXT,
        nullable=False
    )
    read_count = Column(
        INTEGER(unsigned=True),
        default=0
    )
    comment_count = Column(
        INTEGER(unsigned=True),
        nullable=False,
        default=0
    )
    like_count = Column(
        INTEGER(unsigned=True),
        nullable=False,
        default=0
    )
    user_id = Column(
        INTEGER(20, unsigned=True),
        ForeignKey('users.id'),
        nullable=False
    )
    status = Column(
        Enum(*status_enum),
        default=status_enum[0],
        nullable=False
    )
    created_date = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow
    )
