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
    cnj = request.json.get('processo', None)
    if not cnj:
        message = {'Message': 'Invalid request, verify the body content'}
        return Response(response=json.dumps(message), mimetype='application/json', status=400)
    controller = Controller(cnj)
    controller.consult_process()
    return Response(response=json.dumps(controller.collections_result), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
