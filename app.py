from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    # Get the value of the 'yt_url' query parameter from the request
    yt_url = request.args.get('yt_url')

    if yt_url:
        # If 'yt_url' is provided in the query string, you can use it
        return f'You provided a YouTube URL: {yt_url}'
    else:
        # If 'yt_url' is not provided, return a default response
        return 'OK'

if __name__ == '__main__':
    app.run(debug=True)