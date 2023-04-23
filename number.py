import cv2
import pytesseract

## Python-tesseract is an optical character recognition (OCR) tool for python ##
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


## Fetch the image from respective Directory ##
image = cv2.imread("samples/13.jpg")

## Convert image into RGB values from BGR ##
## pytesseract works good so ##
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(image))


## Detecting Digits ##
heightImage, weightImage, _ = image.shape
## Configuration to detect digits from images ##
cong = r"--oem 3 --psm 6 outputbase digits"
boxes = pytesseract.image_to_boxes(image,config=cong)

## Create an empty list to store detected digits
detected_digits = []

## Forming bounding box around digits and storing the detected digits in a list
for b in boxes.splitlines():
    b = b.split(" ")
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,heightImage-y),(w,heightImage-h),(0,0,255),3)
    detected_digit = b[0]
    detected_digits.append(detected_digit)
    cv2.putText(image,detected_digit,(x,heightImage-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(20,30,255),2)

## Print the list of detected digits
print(detected_digits)

cv2.imshow("Detecting Digits", image)
cv2.waitKey(0)
