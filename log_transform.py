import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/cameraman.png')
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype=np.uint8)


f = plt.figure()
f.add_subplot(1,2, 1).title.set_text('Original Image')
plt.imshow(image)
f.add_subplot(1,2, 2).title.set_text('Log Transformed')
plt.imshow(log_image)
plt.show(block=True)