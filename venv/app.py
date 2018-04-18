from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import urllib
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route("/v1")
def welcome():
    return "Welcome to image segmentation"

@app.route("/v1/images", methods=['POST'])
def test_post():
    request_url = request.args.get('image')
    image_url = urllib.request.urlopen(request_url)
    image_array = np.asarray(bytearray(image_url.read()), dtype=np.uint8)
    img = cv2.imdecode(image_array, 0) # This is now an image file

    edges = cv2.Canny(img, 30, 200)

    _, contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]

    i = 0
    for contour in contours:
        i = i + 1
        x,y,w,h = cv2.boundingRect(contour)
        segment = img[y:y+h, x:x+w]
        filename = "segment" + str(i) + ".jpg"
        cv2.imwrite(filename, segment)
        cv2.imshow(filename, segment)

    response = {
        "image": len(contours)
    }

    return jsonify(response)
