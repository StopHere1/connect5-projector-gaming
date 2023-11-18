import connect4
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

cameraId = 0 # give a specific camera id connected to the computer
connect4game = connect4.connect4(10,7) #testing class connection


mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print(result.gestures)
    for gesture in result.gestures:
        print([category.category_name for category in gesture])
    # print('gesture recognition result: {}'.format(result))

base_options = BaseOptions(model_asset_path='gesture_recognizer.task')
options = GestureRecognizerOptions(base_options=base_options, running_mode = VisionRunningMode.LIVE_STREAM,result_callback=print_result)
recognizer = GestureRecognizer.create_from_options(options)

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 1, trackCon = 1):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)
        return lmlist

# start video stream
capture = cv2.VideoCapture(cameraId) 
cv2.namedWindow('capture', cv2.WINDOW_NORMAL)  # open a window to show
pTime = 0
cTime = 0
detector = handDetector()
timestamp = 0
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        if frame is not None:
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frameRGB)
            frame = detector.findHands(frame)
            lmlist = detector.findPosition(frame)
            if len(lmlist) != 0:
                print(lmlist[4])
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            timestamp+=1
            recognizer.recognize_async(mp_image, timestamp)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        #print(id,lm)
                        h, w, c = frame.shape
                        cx, cy = int(lm.x *w), int(lm.y*h)
                        #if id ==0:
                        cv2.circle(frame, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
                    
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow('camera', frame)  # show the frame
        cv2.waitKey(1)


# clear up
capture.release()
cv2.destroyAllWindows()

