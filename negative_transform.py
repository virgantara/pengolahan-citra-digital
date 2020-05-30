import cv2
import numpy as np

img = cv2.imread('images/sample.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h,w = image.shape

gr = np.zeros([h,w], dtype=np.uint8)

t = 110
for y in range(0, h):
  for x in range(0, w):
    v = int(img[y,x,0])

    gr[y, x] = 255 - v

cv2.imshow('gray',gr)
cv2.waitKey(0)
cv2.destroyAllWindows()