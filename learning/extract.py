import cv2
import numpy as np
import os

#load training video
path = "/Users/austinedwards/Google\ Drive/BCD/blinktrainingdata/"
movie = "blinks1.mov"
moviename = movie[:-4]
cap = cv2.VideoReader(path+movie)
nframes = cap.get(7)

framenum = 0
cframenum = 0
oframenum = 0
last = ""
last_state = ""

while(1):

    ret, frame = cap.retreive(framenum)

    cv2.imshow("Frame",frame)

    usr_input = str(raw_input("'c' for closed, 'o' for open, 'b' for back"))

    if usr_input == "c":
        last = "/Users/awedwards/pyworkspace/blinkcount/training/closed/" \            + moviename + "_" + cframenum
        cv2.imwrite(last, frame)
        cframenum+=1
        last_state = "c"

    elif usr_input == "o":
        last = "/Users/awedwards/pyworkspace/blinkcount/training/open/" \            + moviename + "_" + cframenum
        cv2.imwrite(last, frame)
        oframenum+=1
        last_state = "o"

    elif usr_input == "b":
        os.remove(last)
        framenum -= 1
