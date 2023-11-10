import connect4
import cv2

cameraId = 1 # give a specific camera id connected to the computer
connect4game = connect4.connect4(10,7) #testing class connection

# start video stream
capture = cv2.VideoCapture(cameraId) 
cv2.namedWindow('camera', cv2.WINDOW_NORMAL)  # open a window to show
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        if frame is not None:
            cv2.imshow('camera', frame)  # show the frame
            cv2.waitKey(1)
    
# clear up
capture.release()
cv2.destroyAllWindows()

