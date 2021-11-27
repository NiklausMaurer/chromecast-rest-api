import subprocess
import threading

from flask import Flask, request
import json

app = Flask(__name__)


def stream_video():
    subprocess.run(["/home/nmaurer/code/NiklausMaurer/chromecast-player/test-executable.sh",
                    "/home/nmaurer/code/NiklausMaurer/chromecast-player/output.txt"])


@app.route('/', methods=['PUT'])
def set_play_state():  # put application's code here
    data = json.loads(request.data)

    thread = threading.Thread(target=stream_video)
    thread.start()

    return data['url']


if __name__ == '__main__':
    app.run()
