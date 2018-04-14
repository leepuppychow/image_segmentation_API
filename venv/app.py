from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import urllib
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route("/v1/")
def welcome():
    return "Welcome to image segmentation"

@app.route("/v1/images", methods=['POST'])
def test_post():
    request_url = request.args.get('image')
    image_url = urllib.request.urlopen(request_url)
    image_array = np.asarray(bytearray(image_url.read()), dtype=np.uint8)
    img = cv2.imdecode(image_array, -1) # This is now an image file

    edged = cv2.Canny(img, 30, 200)
    _, contours, _= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x,y,w,h = cv2.boundingRect(contours[1])
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

    cv2.imwrite("segment.jpg", segment)

    print(type(segment))


    response = {
        "image": len(contours)
    }

    return jsonify(response)
