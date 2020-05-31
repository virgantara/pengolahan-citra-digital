import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/pollen_dark.jpg') #load rgb image

h,w,c = img.shape

image = np.zeros([h,w,c], dtype=np.uint8)

val = 140
for y in range(0, h):
  for x in range(0, w):
    r = int(img[y,x,2])
    g = int(img[y,x,1])
    b = int(img[y,x,0])
    image[y, x, 2] = r + val
    image[y, x, 1] = g + val
    image[y, x, 0] = b + val



f = plt.figure()
f.add_subplot(2,2, 1).title.set_text('Dark Image')
plt.imshow(img)
f.add_subplot(2,2, 2).title.set_text('Histogram')
plt.hist(img.ravel(),256,[0,256])
f.add_subplot(2,2, 3).title.set_text('Bright Image')
plt.imshow(image)
f.add_subplot(2,2, 4).title.set_text('Histogram')
plt.hist(image.ravel(),256,[0,256])

# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# h,s,v = hsv.shape
#
# imageHSV = np.zeros([h,s,v], dtype=np.uint8)

# f.add_subplot(4,2, 5).title.set_text('Low Contrast Image')
# plt.imshow(image)
# f.add_subplot(4,2, 6).title.set_text('Histogram')
# plt.hist(image.ravel(),256,[0,256])
plt.show(block=True)