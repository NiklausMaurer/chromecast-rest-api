import subprocess
import threading

from flask import Flask, request
import json

app = Flask(__name__)


def stream_video(url):
    subprocess.run(["catt", "cast", url])


@app.route('/play', methods=['PUT'])
def set_play_state():
    data = json.loads(request.data)
    url = data["url"]

    thread = threading.Thread(target=stream_video, args=(url,))
    thread.start()

    return data['url']


if __name__ == '__main__':
    app.run()
