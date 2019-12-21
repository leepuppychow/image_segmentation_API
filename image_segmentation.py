import cv2
import numpy as np

img = cv2.imread('HEP1.png', 0) # this will grayscale
# img = cv2.resize(img, None, fx=0.25, fy=0.25)
cv2.imshow("Original image", img)
# cv2.imshow("grey", img_small)

edged = cv2.Canny(img, 30, 200)
# cv2.imshow("Canny edges", edged)
_, contours, _= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# hierarchy, contours, _= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(edged, contours, -1, (0,255,0))

cv2.imshow("image with contours", edged)

print('Number of contours found = ', len(contours))
print(hierarchy)

#DRAWING A CONTOUR
# one_contour = np.zeros((img.shape[0], img.shape[1], 3))
# cv2.drawContours(one_contour, contours, 0, (0,255,0))
# cv2.imshow("One contour", one_contour)

#Getting one image from one contour's contents

x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

segment = img[y:y+h, x:x+w]

cv2.imwrite("one_exercise.jpg", segment)   #This will save the segment to an image file :)
cv2.imshow("segment", segment)

cv2.waitKey(0)
cv2.destroyAllWindows()
