from flask_wtf import FlaskForm
from  wtforms.validators import Required
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,HiddenField,SelectField
from  wtforms import ValidationError
from .. models import User

class PitchForm(FlaskForm):
  title = StringField('Enter pitch title', validators=[Required()])
  body = TextAreaField('Pitch goes here...', validators=[Required()])
  category = HiddenField('Choose category', validators=[Required()])
  submit = SubmitField('add pitch')

class PitchCommentForm(FlaskForm):
  comment = StringField('what can you say about this comment', validators=[Required()])
  submit = SubmitField('submit')
