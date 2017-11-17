from flask import Flask, Response
import sys
import requests
app = Flask(__name__)

url = None  # Stream address
endpoint = '/'  # server endpoint

url = 'http://127.0.0.1:8000/pid/%s/stream.mp4' % (sys.argv[1])
endpoint = '/video_feed.mp4'


def gen():
    first = True
    while True:
        with requests.get(url, stream=True, timeout=60) as r:
            for chunk in r.iter_content(chunk_size=1024*50):
                if first:
                    first = False
                    print(chunk)
                yield(chunk)
        print('retrying')
        first = True


@app.route(endpoint)
def video_feed():
    return Response(gen())


if __name__ == '__main__':
    print('using: %s' % url)
    print('use: http://localhost:5000%s' % endpoint)
    app.run(host='0.0.0.0', debug=True)
