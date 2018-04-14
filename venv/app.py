from flask import Flask, request, jsonify
from flask_cors import CORS
import image_segmentation

app = Flask(__name__)
CORS(app)

@app.route("/v1/")
def welcome():
    return "Welcome to image segmentation"

@app.route("/v1/images", methods=['POST'])
def test_post():
    age = request.args.get('age')
    name = request.args.get('name')

    response = {
        "age": age,
        "name": name,
    }

    return jsonify(response)
