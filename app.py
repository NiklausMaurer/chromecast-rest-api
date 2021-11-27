from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['PUT'])
def set_play_state():  # put application's code here
    data = json.loads(request.data)
    return data['url']


if __name__ == '__main__':
    app.run()
