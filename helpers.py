import numpy as np
import cv2

def correct_gamma(image, gamma):
    pwr = 1.0 / gamma
    table = np.array([
        ((i / 255.0) ** pwr) * 255
        for i in np.arange(0, 256)
    ]).astype("uint8")
    return cv2.LUT(image, table)

