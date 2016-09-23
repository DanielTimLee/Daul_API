from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class DocumentForm(Form):
    title = StringField('Title', [
        DataRequired(message='제목을 입력해주세요.')
    ])
    content = TextAreaField('Contents', [
        DataRequired(message='내용을 입력해주세요.')
    ])
