import cv2
import numpy as np

img = cv2.imread('photo_YAHHH.jpg', 0)
img = cv2.resize(img, None, fx=0.25, fy=0.25)
cv2.imshow("Greyscale original", img)

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
