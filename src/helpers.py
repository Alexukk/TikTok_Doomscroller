import datetime
from datetime import timedelta
import math
import cv2
import config
import time


def show_stats(img, begin_time, end_time, videos_total):
    cv2.putText(img, "Session stats:", config.TOP_LEFT_ROW_3, cv2.FONT_HERSHEY_PLAIN, 1.3, (16, 195, 35), 4)
    cv2.putText(img, f"Time spent: {str(end_time - begin_time).split('.')[0]}", config.TOP_LEFT_ROW_4, cv2.FONT_HERSHEY_PLAIN, 1, (16, 195, 35), 4)
    cv2.putText(img, f"Videos watched: {videos_total}", config.TOP_LEFT_ROW_5, cv2.FONT_HERSHEY_PLAIN, 1, (16, 195, 35), 4)


def get_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])