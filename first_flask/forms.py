from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class MessageForm(Form):
  new_message = StringField('Message',
                            validators=[DataRequired(),
                                        Length(min=4, max=25)])
