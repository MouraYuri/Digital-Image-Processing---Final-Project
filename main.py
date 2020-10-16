import cv2
import numpy as np

image = cv2.imread("./image.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurryImage = cv2.blur(image,(5,5))
ret,thresh1 = cv2.threshold(blurryImage,140,255,cv2.THRESH_BINARY)
kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(thresh1,kernel,iterations = 1)

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 255

# Filter by Area.
params.filterByArea = True
params.minArea = 1
params.maxArea = 1000000

params.filterByCircularity = False

params.filterByColor = False

params.filterByInertia = False

params.filterByConvexity = False

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(thresh1)

print(len(keypoints))
#cv2.imshow("erosion",erosion)
#cv2.waitKey(0)
cv2.destroyAllWindows()