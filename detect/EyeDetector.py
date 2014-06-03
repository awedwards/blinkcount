import cv2
import os
import numpy as np

class EyeDetector:

    def __init__(self,cascade_fn="../cascades/rightEyeCascade.xml", minNeighbors=5, minSize=(100,100)):
        if not os.path.exists(cascade_fn):
            raise IOError("Cascade not found in path %s." % cascade_fn)
        self.cascade = cv2.CascadeClassifier(cascade_fn)
        self.minNeighbors = minNeighbors
        self.minSize = minSize

    def detect(self, image):
        if np.ndim(image) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect eyes in image 
        eyes = self.cascade.detectMultiScale(image, minNeighbors=self.minNeighbors,minSize=self.minSize)

        if len(eyes) != 1:
            return []

        else:
            (x,y,w,h) = eyes[0]
            return image[y:y+h, x:x+w]
