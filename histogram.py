import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1 = cv.imread('images/pollen_dark.jpg',0)

f = plt.figure()
f.add_subplot(2,2, 1).title.set_text('Dark Image')
plt.imshow(img1)
f.add_subplot(2,2, 2).title.set_text('Histogram')
plt.hist(img1.ravel(),256,[0,256])

plt.show()
