# 0201.py
import cv2

imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
font = cv2.FONT_HERSHEY_SIMPLEX
text = "hello"
img = cv2.putText(img, text, (100, 100), font, 2, (0, 0, 0), 1, cv2.LINE_AA)
cv2.imshow('Lena',img)

cv2.imwrite("./data/sample.jpg",img)


cv2.waitKey()
cv2.destroyAllWindows()
