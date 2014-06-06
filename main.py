import cv2
import detect
import threshold
import numpy as np

def main():

    cap = cv2.VideoCapture(0)

    ret,frame = cap.read()
    cv2.imshow("test",frame)
    eye = detect.detectEye(frame)
    t = threshold.calibrate(eye)
    thEye = threshold.binaryThreshold(eye,t)
    bthresh = np.sum(thEye)/2
    
    while True:

        ret,frame = cap.read()
        eye = detect.detectEye(frame)
        if eye != None:
            cv2.imshow("eye",eye)
            thEye = threshold.binaryThreshold(eye,t)
            cv2.imshow("th",thEye)
            b = detect.detectBlink(thEye,bthresh)
        
            if b == True:
                print "blink"
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

main()
