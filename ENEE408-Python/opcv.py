import cv2
import numpy as np

image_path = 'image.jpg'
original = cv2.imread(image_path)
cv2.imshow('original', original)

gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray scale' ,gray)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=100, threshold2=200)
cv2.imshow("Canny Edges", edges)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# 4. Draw rectangles around the detected objects and detect eyes within faces
for (x, y, w, h) in faces:
    cv2.rectangle(original, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w] # Extract Region of Interest (ROI) for eyes
    roi_color = original[y:y+h, x:x+w] # Corresponding ROI in color image

cv2.imshow('Object Detection using Haar Cascade', original)

cv2.waitKey(0)
cv2.destroyAllWindows()