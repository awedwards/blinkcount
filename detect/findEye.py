import cv2

def findEye(image,cascade):
    # Returns cropped image of eye

    # Create cascade object
    eye_cascade = cv2.CascadeClassifier(cascade)

    # Detect eyes in image 
    eyes = eye_cascade.detectMultiScale(image)

    if len(eyes) > 1:
        for e in range(len(eyes)):
            if eyes[e][2] > 100 and eyes[e][3] > 100:
                (x,y,w,h) = eyes[e]
                return image[y:y+h, x:x+w]
    elif len(eyes) == 1:
        (x,y,w,h) = eyes[0]
        return image[y:y+h,x:x+w]

    else:
        return None
