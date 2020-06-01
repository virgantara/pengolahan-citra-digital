import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/pollen_dark.jpg',0) #load rgb image

h,w = img.shape

imhist = cv2.equalizeHist(img)

row = 2
col = 2
f = plt.figure()
f.add_subplot(row,col, 1).title.set_text('Dark Image')
plt.gray()
plt.imshow(img)
f.add_subplot(row,col, 2).title.set_text('Histogram')
plt.hist(img.ravel(),256,[0,256])

f.add_subplot(row,col, 3).title.set_text('Histogram Equalized')
plt.gray()
plt.imshow(imhist)

f.add_subplot(row,col, 4).title.set_text('Histogram')

plt.hist(imhist.ravel(),256,[0,256])

plt.show(block=True)