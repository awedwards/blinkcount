import cv2
import numpy as np
import math

class Threshold(image):
    # img = frame from videocapture

    def __init__(self, t=0, m=0, w=0, h=0):
        self.t = t
        self.m = m
        self.w = w
        self.h = h

    def calibrate(self, image):
        #convert to grayscale
        if np.ndim(image)==3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #get size, max intensity of the gray image
        self.w, self.h = gray.shape[:2]
        self.m = np.amax(gray)

        #Calculate target thresholded image
        target = (self.w*self.h*255)/2

        #initialize t, tnew (threshold values)
        tnew = math.floor(m/2)
        t = 0

        while (t-tnew != 0):
            t = tnew
            ret, th = cv2.threshold(image,t,self.m,cv2.THRESH_BINARY)
            if th.sum() < 0.95*target:
                tnew = int(math.floor(t-t*0.1))
            elif th.sum() > 1.05*target:
                tnew = int(math.floor(t+t*0.1))

        self.t = t

        return t

    def binaryThreshold(self,image):

        if np.ndim(image)==3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        ret, th = cv2.threshold(image,self.t,self.m,cv2.THRESH_BINARY)
        return th
