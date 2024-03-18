import os
import openai
from openai import OpenAI
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .ask_form import AskmeForm

ask_blueprint = Blueprint('askme', __name__)

@ask_blueprint.route('/askme',methods=['GET', 'POST'])
@app.route('/askme',methods=['GET', 'POST'])
def askme():
  form = AskmeForm(request.form)
  
  if request.method == 'POST':
      if form.validate() == False:
        return render_template('askme.html', form=form)
      else:
        # The following response code adapted from example on: 
        # https://platform.openai.com/docs/api-reference/chat/create
        client = OpenAI()
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",

  "id": "modr-XXXXX",
  "model": "text-moderation-005",
  "results": [
    {
      "flagged": true,
      "categories": {
        "sexual": false,
        "hate": false,
        "harassment": false,
        "self-harm": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": true,
        "violence": true,
      },
      "category_scores": {
        "sexual": 1.2282071e-06,
        "hate": 0.010696256,
        "harassment": 0.29842457,
        "self-harm": 1.5236925e-08,
        "sexual/minors": 5.7246268e-08,
        "hate/threatening": 0.0060676364,
        "violence/graphic": 4.435014e-06,
        "self-harm/intent": 8.098441e-10,
        "self-harm/instructions": 2.8498655e-11,
        "harassment/threatening": 0.63055265,
        "violence": 0.99011886,
      }
    }
  ],
          messages=[
            #{"role": "system", "content": "You use Gen Z slang but are embarrassed when you do use it."},
            
            {"role": "user", "content": form.prompt.data}
          ],
          max_tokens=150
        )

        display_text = response.choices[0].message.content
        return render_template('askme.html', ask_me_prompt=form.prompt.data,ask_me_response=display_text,success=True)
      
  elif request.method == 'GET':
      return render_template('askme.html', form=form)