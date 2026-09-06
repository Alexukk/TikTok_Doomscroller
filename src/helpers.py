import datetime
from datetime import timedelta
import math
import cv2
import config
import time


def show_stats(img, begin_time, end_time, videos_total):
    cv2.putText(img, "Session stats:", config.TOP_LEFT_ROW_3, cv2.FONT_HERSHEY_PLAIN, 1.3, config.DARK_GREEN, 4)
    cv2.putText(img, f"Time spent: {str(end_time - begin_time).split('.')[0]}", config.TOP_LEFT_ROW_4, cv2.FONT_HERSHEY_PLAIN, 1.2, config.DARK_GREEN, 4)
    cv2.putText(img, f"Videos watched: {videos_total}", config.TOP_LEFT_ROW_5, cv2.FONT_HERSHEY_PLAIN, 1.2, config.DARK_GREEN, 4)


def get_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])



def show_help(img):
    cv2.putText(img, "General Keybinds: ", config.TOP_LEFT_ROW_6, cv2.FONT_HERSHEY_PLAIN, 1.3, config.GREEN, 4)
    cv2.putText(img, f"Q - Terminate session", config.TOP_LEFT_ROW_7, cv2.FONT_HERSHEY_PLAIN, 1.2, config.GREEN, 4)
    cv2.putText(img, f"V - toggle version", config.TOP_LEFT_ROW_8, cv2.FONT_HERSHEY_PLAIN, 1.2, config.GREEN, 4)
    cv2.putText(img, f"F - toggle fps", config.TOP_LEFT_ROW_9, cv2.FONT_HERSHEY_PLAIN, 1.2, config.GREEN, 4)
    cv2.putText(img, f"S - toggle stats", config.TOP_LEFT_ROW_10, cv2.FONT_HERSHEY_PLAIN, 1.2, config.GREEN, 4)
    cv2.putText(img, f"H - toggle help", config.TOP_LEFT_ROW_11, cv2.FONT_HERSHEY_PLAIN, 1.2, config.GREEN, 4)


def process_gesture(gesture): # Takes an array of fingers activity
    try:
        data = config.GESTURES_V2[gesture]
    except Exception as e:
        return "No gesture was matched"
    return data