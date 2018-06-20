# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

faceCascade = cv2.CascadeClassifier('./src/haarcascade_frontalface_default.xml')

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

time.sleep(0.2)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame.vflip = True
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]  

    cv2.imshow('video',image)
    rawCapture.truncate(0)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

camera.close()
cv2.destroyAllWindows()
