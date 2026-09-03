import cv2
import mediapipe as mp
from browser_init import init_browser
import config
from helpers import quit_menu

video = cv2.VideoCapture(0) # Initializing WebCam usage

mpHands = mp.solutions.hands # Edited max_hands from 2 to 1
hands = mpHands.Hands()


mpDraw = mp.solutions.drawing_utils

if config.SHOW_FPS:
    import time
    global current_time
    global previous_time


# Main loop

while True:
    is_cam_running, img = video.read() # Reading one frame per integration
    key = cv2.waitKey(2)
    if key == ord("q") or not is_cam_running:
        quit_menu() # Coming later
        break

    # Adjusting and processing frames
    camRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(camRGB)

    p = {}
    fingers = [0, 0, 0, 0, 0]

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            if config.SHOW_DEBUG_DATA:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            width, height, _ = camRGB.shape

            for id, point in enumerate(handLms.landmark):

                cx, cy = int(point.x * height), int(point.y * width)
                p[id] = (cx, cy)


    cv2.imshow("TikTokDoomscroller", img)
