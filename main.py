import cv2

img = cv2.imread('assets/troopy.jpg', -1)
img = cv2.resize(img, (700, 400))


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
