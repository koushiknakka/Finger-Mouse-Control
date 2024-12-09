import cv2
import mediapipe as mp
import pyautogui

video_capture = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    _, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks :
        landmarks = results.multi_hand_landmarks[0].landmark
        for handlms in results.multi_hand_landmarks:
            for Id, lm in enumerate(handlms.landmark):

                x, y = int(lm.x*w), int(lm.y*h)

                if Id == 8:
                    cv2.circle(frame, (x,y), 10, (109, 27, 23))
                    screen_x = screen_w/w * x
                    screen_y = screen_h/h * y
                    pyautogui.moveTo(screen_x, screen_y)
            mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)
        left = [landmarks[4], landmarks[8]]
        for landmark in left:
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (x, y), 5, (0, 255, 255))
        if (left[0].y-left[1].y) < 0.07:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow("image", frame)
    cv2.waitKey(1)
