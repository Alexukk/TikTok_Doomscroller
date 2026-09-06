# General Links and configurations
TIKTOK_LINK="https://www.tiktok.com/"
VERSION="1.0.0 (BETA)"

# Webcam window configuration
SHOW_WEBCAM=True     # Shows Video captured and processed by webcam
SHOW_DEBUG_DATA=True # Points and lines between the fingers
SHOW_FPS=True        # Shows debug data (fps) when toggled
SHOW_VERSION=True
SHOW_STATS=True
SHOW_HELP=False


# Coordinates & rows
TOP_LEFT_ROW_1=(10, 30)
TOP_LEFT_ROW_2=(10, 55)
TOP_LEFT_ROW_3=(10, 80)
TOP_LEFT_ROW_4=(10, 100)
TOP_LEFT_ROW_5=(10, 120)
TOP_LEFT_ROW_6=(10, 140)
TOP_LEFT_ROW_7=(10, 160)
TOP_LEFT_ROW_8=(10, 180)
TOP_LEFT_ROW_9=(10, 200)
TOP_LEFT_ROW_10=(10, 220)
TOP_LEFT_ROW_11=(10, 240)
TOP_LEFT_ROW_12=(10, 260)
TOP_LEFT_ROW_13=(10, 280)
TOP_LEFT_ROW_14=(10, 300)

# Colors in BGR
RED=(86, 37, 222)
DARK_GREEN=(28, 105, 25)
GREEN=(0, 205, 0)
NAVY_BLUE=(114, 84, 14)

# Gestures

# Structure: ["NAME", int(id), [0, 0, 0, 0, 0] <- fingers position]
GESTURES_V1 = [
    ["Like",  1, [1, 0, 0, 0, 0]],
    ["Down",  2, [0, 0, 0, 0, 1]],
    ["Up",    3, [0, 1, 0, 0, 0]],
    ["Close", 4, [0, 1, 1, 1, 1]], # First variation of opened palm
    ["Close", 5, [1, 1, 1, 1, 1]]  # Second variation of opened palm (big finger glitches sometimes)
]


GESTURES_V2 ={  (1, 0, 0, 0, 0) : "Like",
                (0, 0, 0, 0, 1) : "Previous",
                (0, 1, 0, 0, 0) : "Next",
                (0, 1, 1, 1, 1) : "Undone", # First variation of opened palm
                (1, 1, 1, 1, 1) : "Undone", # Second variation of opened palm (big finger glitches sometimes)
                (0, 1, 0, 0, 1) : "Close",
                (0, 1, 1, 0, 0) : "Reload"}


# Gesture recognition config
RECOGNITION_SPEED_MULTIPLIER=2 # Recognition multiplier, range 1 - 5 where. Where larger value means longer recognition (up to 5 seconds per gesture) but better definition.


# Browser config

BROWSER_RUNNING=False