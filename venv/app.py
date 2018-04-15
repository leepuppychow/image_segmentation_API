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

    edges = cv2.Canny(img, 125, 200) # (image_source, minVal, maxVal) for Canny edge detection

    _, contours, _= cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by area and take the largest ones? 
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:6]

    x,y,w,h = cv2.boundingRect(contours[0])
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

    segment = img[y:y+h, x:x+w]
    cv2.imwrite("segment.jpg", segment)

    response = {
        "image": len(contours)
    }

    return jsonify(response)
