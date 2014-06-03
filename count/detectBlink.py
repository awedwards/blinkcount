import numpy as np
import cv2
import calibrate
import findEye

cap = cv2.VideoCapture("blinks1.mov")
sums = []
while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eye = findEye(gray,'rightEyeCascade,xml')
    t = calibrate(eye)

    ret, theye = cv2.threshold(eye,t,np.amax(eye),cv2.THRESH_BINARY)

    if eye!=None:
        sums.append(theye.sum())


    #if eye!=None:
    #    if (theye.sum() < 1000000) and (prev_frame_val > 1000000):
    #        print "BLINK"
    #    cv2.imshow('Thresholded Image', theye)
    #    
    #    prev_frame_val = theye.sum()
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

cv2.destroyAllWindows()
