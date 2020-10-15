import cv2

image = cv2.imread("./image.png")
cv2.imshow("Raw Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()