from flask import Flask, make_response, jsonify, request
from bd import Times

app = Flask(__name__)

@app.route('/times', methods=['GET'])
def get_times():
    return make_response(
        jsonify(Times)
    )

@app.route('/times', methods=['POST'])
def create_time():
    time = request.json
    Times.append(time)
    return make_response(
        jsonify(time)
    )

app.run()