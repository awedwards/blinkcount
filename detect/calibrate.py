import cv2
import numpy as np
import math

cap = cv2.VideoCapture("blinks1.mov")

def calibrate(img):
    # img = frame from videocapture

    #convert to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #get size, max intensity of the gray image
    w,h = gray.shape[:2]
    m = np.amax(gray)

    #Calculate target thresholded image
    target = (w*h*255)/2

    #initialize t, tnew (threshold values)
    tnew = math.floor(m/2)
    t = 0

    while (t-tnew != 0):
        t = tnew
        ret, th = cv2.threshold(gray,t,m,cv2.THRESH_BINARY)
        if th.sum() < 0.95*target:
            tnew = int(math.floor(t-t*0.1))
        elif th.sum() > 1.05*target:
            tnew = int(math.floor(t+t*0.1))

    return t
