
import pytesseract
import datetime
import pandas as pd
import cv2
import cv2
import numpy as np



## Python-tesseract is an optical character recognition (OCR) tool for python ##
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

## Fetch the image from respective Directory ##
image = cv2.imread("Test13.jpg")
image = cv2.resize(image, (500, 500))
## Convert image into RGB values from BGR ##
## pytesseract works good so ##
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
l1=pytesseract.image_to_string(image)
print(l1)

## Detecting Words ##
heightImage, weightImage, _ = image.shape
boxes = pytesseract.image_to_data(image)
# print(boxes)
## Forming bounding boxes around words ##
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        # print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(image, (x, y), (w + x, h + y), (0, 0, 255), 3)
            cv2.putText(image, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (20, 30, 255), 2)

cv2.imshow("Detecting Words", image)
cv2.waitKey(0)


words = l1.split('\n')
print(words)


def Predict_the_Name_of_Student(test_value, dataset):
    scores = []

    for element in dataset:
        score = sum([1 for i, j in zip(test_value, element) if i == j])
        scores.append(score)

    max_val = scores[0]  # initialize max_val to the first element of the list
    max_idx = 0  # initialize max_idx to 0
    for i in range(1, len(scores)):
        if scores[i] > max_val:
            max_val = scores[i]
            max_idx = i
    return max_idx



dataset = ['XXXXXX', 'Afzal', 'Sumit', 'Nigel', 'Abhay', 'Cyril']
for i in range(len(words)):
    max1 = Predict_the_Name_of_Student(words[i], dataset)
    print(dataset[max1])