import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('images/pollen_low_contrast.jpg',0)

f = plt.figure()
f.add_subplot(1,2, 1).title.set_text('Original Image')
plt.imshow(img)
f.add_subplot(1,2, 2).title.set_text('Histogram')
plt.hist(img.ravel(),256,[0,256])
plt.show()
