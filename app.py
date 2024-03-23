from flask import Flask, request
from controller.controller import Controller


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {'Message' : 'The server is running'}

@app.route('/collect', methods=['POST'])
def collect():
    data = request.json
    if not 'processo' in data:
        return {'Message': 'Error'}
    cnj = data['processo']
    controller = Controller(cnj)
    return controller.consult_process()



if __name__ == '__main__':
    app.run(debug=True)