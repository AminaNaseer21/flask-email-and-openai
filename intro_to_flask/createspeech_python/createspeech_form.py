import sys
sys.dont_write_bytecode = True
# Ensure you have the necessary packages installed:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired

class CreatespeechForm(FlaskForm):
    prompt = TextAreaField("What would you like me to say?", validators=[InputRequired("Please enter a prompt.")])
    submit = SubmitField("Send")