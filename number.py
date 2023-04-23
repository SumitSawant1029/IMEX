# import cv2
# import pytesseract
#
# ## Python-tesseract is an optical character recognition (OCR) tool for python ##
# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#
#
# ## Fetch the image from respective Directory ##
# image = cv2.imread("samples/13.jpg")
#
# ## Convert image into RGB values from BGR ##
# ## pytesseract works good so ##
# image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(image))
#
#
# ## Detecting Digits ##
# heightImage,weightImage,_ = image.shape
# ## Configuration to detect digits from images ##
# cong = r"--oem 3 --psm 6 outputbase digits"
# boxes = pytesseract.image_to_boxes(image,config=cong)
# ## Forming bounding box around digits ##
# for b in boxes.splitlines():
#     b = b.split(" ")
#     print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(image,(x,heightImage-y),(w,heightImage-h),(0,0,255),3)
#     cv2.putText(image,b[0],(x,heightImage-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(20,30,255),2)
#
#
#
#
# cv2.imshow("Detecting Digits", image)
# cv2.waitKey(0)

import cv2
import pytesseract

## Python-tesseract is an optical character recognition (OCR) tool for python ##
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

## Fetch the image from respective Directory ##
image = cv2.imread("samples/30.png")

## Convert image into RGB values from BGR ##
## pytesseract works good so ##
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(image))


## Detecting Digits ##
heightImage,weightImage,_ = image.shape
## Configuration to detect digits from images ##
cong = r"--oem 3 --psm 6 outputbase digits"
boxes = pytesseract.image_to_boxes(image,config=cong)
## Forming bounding box around digits ##
for b in boxes.splitlines():
    b = b.split(" ")
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,heightImage-y),(w,heightImage-h),(0,0,255),3)
    digit = b[0]
    if digit.isdigit() and int(digit) >= 0 and int(digit) <= 9:
        ## Check for double digits ##
        if len(b[0]) == 2 and boxes.count(b[0][1] + " " + str(x)) > 1:
            continue
        cv2.putText(image,digit,(x,heightImage-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(20,30,255),2)

cv2.imshow("Detecting Digits", image)
cv2.waitKey(0)



