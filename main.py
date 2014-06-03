import cv2
import detect

def main():

    cap = cv2.VideoReader("movie")

    ret,frame = cap.imread

    T = Threshold()
    T.calibrate(frame)
    th = T.binaryThreshold(frame)
