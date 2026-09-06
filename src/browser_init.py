import webbrowser
from pynput.keyboard import Controller, Key

keyboard = Controller()

def init_browser(link):
    webbrowser.open(link, new=True, autoraise=True)


def press_button(name):
    keyboard.press(name)
    keyboard.release(name)