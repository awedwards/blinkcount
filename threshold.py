import cv2
import numpy as np
import math


def calibrate(self, image):
    #convert to grayscale
    if np.ndim(image)==3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #get size, max intensity of the gray image
    w, h = image.shape[:2]
    m = np.amax(image)

    #Calculate target thresholded image
    target = (w*h*255)/2

    #initialize t, tnew (threshold values)
    tnew = math.floor(m/2)
    t = 0

    while (t-tnew != 0):
        t = tnew
        ret, th = cv2.threshold(image,t,m,cv2.THRESH_BINARY)
        if th.sum() < 0.95*target:
            tnew = int(math.floor(t-t*0.1))
        elif th.sum() > 1.05*target:
            tnew = int(math.floor(t+t*0.1))

        t = t
        return

def binaryThreshold(self,image,t):
    #t = threshold
    m = np.amax(image)

    if np.ndim(image)==3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, th = cv2.threshold(image,t,m,cv2.THRESH_BINARY)
    return th

