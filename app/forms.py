from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class EmailForm(Form):
    email = StringField('email', validators=[DataRequired()])
    body = TextAreaField('body', validators=[DataRequired()])