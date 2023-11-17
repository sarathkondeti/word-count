from flask import Flask, request
from pytube import YouTube
import speech_recognition as sr
import re
import os
from flask_cors import CORS
from pydub import AudioSegment


AUDIO_PATH = '/tmp/word-count'  # Change this to your preferred temporary folder
AUDIO_FILE = 'youtube_audio'

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/', methods=['GET'])
def hello():
    # Get the value of the 'yt_url' query parameter from the request
    yt_url = request.args.get('yt_url')
    word_to_count = request.args.get('word_to_count')
    # Create a YouTube object
    try:
        yt = YouTube(yt_url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4')
        print(audio_stream)
        audio_stream.first().download(output_path = AUDIO_PATH, filename = AUDIO_FILE + '.mp4')
        print(f"Video {yt.title} downloaded")
    except:
        return "URL invalid"

    # return "downloaded"
    audio_file = os.path.join(AUDIO_PATH,AUDIO_FILE)
    audio = AudioSegment.from_file(audio_file + '.mp4', format="mp4")
    audio.export(audio_file + '.flac', format="flac")
    
    # return 'converted'

    recognizer = sr.Recognizer()
    audio_data = None
    with sr.AudioFile(audio_file + '.flac') as source:
        audio_data = recognizer.listen(source)
    try:
        transcription = recognizer.recognize_sphinx(audio_data)  # You can use other recognition engines like 'recognize_sphinx' - offline
        print("Transcription: " + transcription)
        count = 0
        for word in transcription.split(' '):
            if word_to_count is word:
                count+=1
        return f'The word {word_to_count} is spoken {count} time(s)'
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


    return "Transcription: failed"
    

if __name__ == '__main__':
    app.run(debug=True)
