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

previous_time = 0
# Main loop

while True:
    is_cam_running, img = video.read() # Reading one frame per integration
    key = cv2.waitKey(2)
    if key == ord("q") or not is_cam_running:
        quit_menu() # Coming later
        break

    current_time = time.time()

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
    if config.SHOW_FPS:
        fps: float = 1 / (current_time - previous_time)
        cv2.putText(img, f"Fps: {int(fps)}", (config.TOP_LEFT_ROW_2 if config.SHOW_VERSION else config.TOP_LEFT_ROW_1),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.8, (114, 84, 14), 2)
        previous_time = current_time

    if config.SHOW_VERSION:
        cv2.putText(img, f"Version: {config.VERSION}", config.TOP_LEFT_ROW_1, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (86, 37, 222), 4)

    cv2.imshow("TikTokDoomscroller", img)
