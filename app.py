from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    # Get the value of the 'yt_url' query parameter from the request
    yt_url = request.args.get('yt_url')

    # Create a YouTube object
    try:
        yt = YouTube(yt_url)
    except:
        return "URL invalid"
    # Get the available caption tracks (subtitles)
    caption_tracks = yt.captions
    print('Received the URL: ', yt_url)
    # Loop through the caption tracks and download the subtitles
    for caption in caption_tracks:
        print(f"Language: {caption.code}")
        print(f"Caption: {caption.name}")

    if yt_url:
        # If 'yt_url' is provided in the query string, you can use it
        return f'You provided a YouTube URL: {yt_url}'
    else:
        # If 'yt_url' is not provided, return a default response
        return 'OK'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)