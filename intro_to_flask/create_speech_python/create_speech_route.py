import os
import openai
from openai import OpenAI
from pathlib import Path
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .create_speech_form import SpeechForm

speech_blueprint = Blueprint('create_speech', __name__)

@speech_blueprint.route('/create_speech',methods=['GET', 'POST'])
@app.route('/create_speech',methods=['GET', 'POST'])
def create_speech():
    form = SpeechForm(request.form)
  
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_speech.html', form=form)
        else:            
            client = OpenAI()
            
            speech_file_path =("intro_to_flask\speech.mp3")


            response = client.audio.speech.create(
                model="tts-1-hd",
                voice="onyx",
                input=form.prompt.data,
        )
            response.stream_to_file(speech_file_path)

            return render_template('create_speech.html', create_speech_prompt=form.prompt.data, create_speech_response="intro_to_flask\speech.mp3", success=True)
                
    elif request.method == 'GET':
    
     return render_template('create_speech.html', form=form)