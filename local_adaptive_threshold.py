import cv2

from matplotlib import pyplot as plt

img = cv2.imread('images/book.jpg',0)

ukuranBlok = 15
C = 7
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,ukuranBlok,C)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,ukuranBlok,C)

titles = ['Original Image', 'Adaptive Mean Thresholding','Adaptive Gaussian']
images = [img, th2, th3]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
