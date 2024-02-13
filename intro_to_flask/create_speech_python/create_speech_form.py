import sys 
sys.dont_write_bytecode = True
#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, validators, ValidationError

class SpeechForm(Form):
    prompt = TextAreaField("Enter test to be converted to audio!",  [validators.InputRequired("Please enter a prompt.")])
    submit = SubmitField("Generate Audio") 