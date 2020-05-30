
import cv2
import numpy as np

img = cv2.imread('images/Lenna.png')
#cv2.imshow('rgb',img)
h,w,c = img.shape

gr = np.zeros([h,w], dtype=np.uint8)

for y in range(0, h):
  for x in range(0, w):
    r = int(img[y,x,2])
    g = int(img[y,x,1])
    b = int(img[y,x,0])
    v = (r + g + b) / 3
    gr[y,x] = v

minValue = gr.min()
maxValue = gr.max()


imout = np.zeros([h,w], dtype=np.uint8)

a = minValue
b = maxValue
c = a + 50
d = b - 50



for y in range(0, h):
  for x in range(0, w):
     v = gr[y,x]
     imout[y,x] = (v - c) * ((b - a)/(d - c)) + a

#image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#print image
cv2.imshow('gray2',gr)
cv2.imshow('cs',imout)

cv2.waitKey(0)
cv2.destroyAllWindows()