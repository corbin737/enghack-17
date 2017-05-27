from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired

class MessageForm(Form):
    recipient = TextField('recipient', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired()])
