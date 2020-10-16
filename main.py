import cv2
import numpy as np

image = cv2.imread("./image.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurryImage = cv2.blur(image,(5,5))
ret,thresh1 = cv2.threshold(blurryImage,140,255,cv2.THRESH_BINARY)
kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(thresh1,kernel,iterations = 1)

detector = cv2.SimpleBlobDetector()
detector.detect(thresh1)

#print(len(keypoints))
#cv2.imshow("erosion",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()