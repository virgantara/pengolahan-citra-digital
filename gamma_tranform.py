import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from helpers import correct_gamma

img = cv2.imread('images/sample.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gr1 = correct_gamma(image, 1.5)
gr2 = correct_gamma(image, 1.75)
gr3 = correct_gamma(image, 2.0)

gr4 = correct_gamma(image, 0.75)
gr5 = correct_gamma(image, 0.5)
gr6 = correct_gamma(image, 0.25)

f = plt.figure()
f.add_subplot(2,4, 1).title.set_text('Original Image')
plt.imshow(image)
f.add_subplot(2,4, 2).title.set_text('Gamma Corrected with γ='+str(1.5))
plt.imshow(gr1)
f.add_subplot(2,4, 3).title.set_text('Gamma Corrected with γ='+str(1.75))
plt.imshow(gr2)
f.add_subplot(2,4, 4).title.set_text('Gamma Corrected with γ='+str(2.0))
plt.imshow(gr3)

f.add_subplot(2,4, 5).title.set_text('Gamma Corrected with γ='+str(0.75))
plt.imshow(gr4)
f.add_subplot(2,4, 6).title.set_text('Gamma Corrected with γ='+str(0.5))
plt.imshow(gr5)
f.add_subplot(2,4, 7).title.set_text('Gamma Corrected with γ='+str(0.25))
plt.imshow(gr6)

plt.show(block=True)

cv2.waitKey(0)
cv2.destroyAllWindows()