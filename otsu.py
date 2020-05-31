import cv2

from matplotlib import pyplot as plt

img = cv2.imread('images/sample_otsu.jpg',0)

ukuranBlok = 15
C = 7
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
titles = ['Original Image', 'Global Manual Thresholding t = 127','Otsu Thresholding']
images = [img, th1, th2]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
