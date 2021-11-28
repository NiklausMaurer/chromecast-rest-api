import os
from multiprocessing import Process
import validators
from flask import Flask, request
import json

app = Flask(__name__)


def cast(url):
    if validators.url(url):
        os.system(f"python -m catt.cli cast {url}")


@app.route('/cast', methods=['PUT'])
def set_play_state():
    data = json.loads(request.data)
    url = data["url"]

    process = Process(target=cast, args=(url,))
    process.start()

    return data['url']


if __name__ == '__main__':
    app.run(host="0.0.0.0")
