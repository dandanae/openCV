import cv2
import numpy

img = cv2.imread("data/lena.jpg")
resize_img = cv2.resize(img, (768, 576))

cap = cv2.VideoCapture('./data/vtest.avi')
while True:
    ret, video = cap.read()
    
    alpha = 0.5
    beta = 0.5
    
    res1 = (resize_img * alpha + video * beta).astype(numpy.uint8)
    res2 = cv2.addWeighted(img, alpha, video, beta, 0)
    
    cv2.imshow('result', res2)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break

cap.release()
cv2.destroyAllWindows()

