import json

from flask import Flask, request, Response
from controller.controller import Controller

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    message = {'Status': 'The server is running'}
    return Response(response=json.dumps(message), mimetype='application/json', status=200)


@app.route('/api', methods=['GET'])
def api():
    message = {'Status': 'The api is connected'}
    return Response(response=json.dumps(message), mimetype='application/json', status=200)


@app.route('/api/collect', methods=['POST'])
def collect():
    data = request.json
    if not 'processo' in data:
        message = {'Message': 'Invalid request '}
        return Response(response=json.dumps(message), mimetype='application/json', status=400)
    cnj = data['processo']
    controller = Controller(cnj)
    return Response(response=json.dumps(controller.consult_process()), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True)
