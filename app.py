import subprocess
import threading
import os

from flask import Flask, request
import json

app = Flask(__name__)


def cast(url):
    subprocess.run(["catt", "cast", url])


@app.route('/play', methods=['PUT'])
def set_play_state():
    data = json.loads(request.data)
    url = data["url"]

    thread = threading.Thread(target=cast, args=(url,))
    thread.start()

    return data['url']


if __name__ == '__main__':
    app.run(port=os.getenv('API_PORT', 5000))
