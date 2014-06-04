import cv2
import detect

def main():

    cap = cv2.VideoCapture("/Users/edwardsa/Google Drive/BCD/blinktrainingdata/blinks0.mov")

    ret,frame = cap.read()

    T = detect.Threshold()
    T.calibrate(frame)
    th = T.binaryThreshold(frame)
    print th

main()
