from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def send_json():
    x = [9,20,25]
    return jsonify(sting='Value', list=x)

@app.route('/receive', methods=['POST'])
def receive():
    postedjson = json.loads(request.data.decode())
    print(postedjson)
    return "success"

if __name__ == "__main__":
    app.run(port=1887, debug=True)
