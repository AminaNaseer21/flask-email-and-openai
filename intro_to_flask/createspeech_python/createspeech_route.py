# Assuming this is a Python script, consider renaming the file to createspeech_routes.py
from flask import render_template, request, Blueprint
from .createspeech_form import CreatespeechForm
import openai

createspeech_blueprint = Blueprint('createspeech', __name__)

@createspeech_blueprint.route('/createspeech', methods=['GET', 'POST'])
def createspeech():
    form = CreatespeechForm(request.form)

    if request.method == 'POST' and form.validate():
        # Ensure you have set the OpenAI API key elsewhere in your application
        response = openai.Audio.create(
            engine="tts-1",
            format="mp3",
            text=form.prompt.data
        )
        if response:
            display_audio_url = response["data"][0]["url"]
            return render_template('createspeech.html', create_speech_prompt=form.prompt.data, create_speech_response=display_audio_url, success=True)
        else:
            # Handle errors or unsuccessful API calls
            return render_template('createspeech.html', form=form, error="Failed to generate speech.")
    else:
        return render_template('createspeech.html', form=form)
