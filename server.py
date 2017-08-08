from flask import Flask, Response
import requests
app = Flask(__name__)

url = None  # Stream address
endpoint = '/'  # server endpoint


def gen():
    r = requests.get(url, stream=True)
    for chunk in r.iter_content(chunk_size=1024*10):
        yield(chunk)


@app.route(endpoint)
def video_feed():
    return Response(gen())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
