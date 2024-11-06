from flask import Flask, request, jsonify
import os

app = Flask(__name__)



@app.route('/', methods=['GET'])
def call_server():
    return jsonify({'msg': 'hello!'}), 200


if __name__ == '__main__':
    app.run(debug=True)
