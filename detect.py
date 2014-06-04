import cv2
import os
import numpy as np

def detectEye(image):

    #Initialize parameters for detection
    cascade_fn="./cascades/rightEyeCascade.xml"
    if not os.path.exists(cascade_fn):
        raise IOError("Cascade not found in path %s." % cascade_fn)
    minNeighbors=5
    minSize=(100,100)

    if np.ndim(image) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Create cascade
    cascade= cv2.CascadeClassifier(cascade_fn)

    # Detect eyes in image 
    eyes = cascade.detectMultiScale(image, minNeighbors=minNeighbors,minSize=minSize)

    if len(eyes) != 1:
        return None 

    else:
        (x,y,w,h) = eyes[0]
        return image[y:y+h, x:x+w]

def detectBlink(image,bthresh):
    # bthresh = blink threshold
    # image = thresholded image

    s = np.sum(image)
    print s, bthresh
    if s < bthresh:
        return True
    else:
        return False
