import cv2
import numpy as np

def adjust_size(img, x_size, y_size):
    x, y, z = img.shape
    x_size, y_size = max(x_size, x), max(y_size, y)
    x_adjust, y_adjust = int((x_size-x)/2), int((y_size-y)/2)

    zero = cv2.resize(np.zeros((1, 1, z), np.float), (x_size, y_size))
    zero.resize(y_size, x_size, z)
    zero[y_adjust:y_adjust+y, x_adjust:x_adjust+x] = img
    return zero
