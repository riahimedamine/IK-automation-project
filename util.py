import datetime
import pyautogui
import time
import random


def log(action):
    with open("bot_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {action}\n")


def SHORT_DELAY():
    return random.uniform(0.3, 0.8)


def LONG_DELAY():
    return random.uniform(0.8, 1.2)


def click_button(
    image_path, description, confidence=0.8, delay=SHORT_DELAY(), gray=True
):
    try:
        button_location = pyautogui.locateOnScreen(
            image_path, confidence=confidence, grayscale=gray
        )
    except:
        print(f"{description} not found")
        return False
    if button_location:
        x, y = pyautogui.center(button_location)
        pyautogui.click(x, y)
        log(f"Clicked {description}")
        print(f"Clicked {description}")
        time.sleep(delay)  # Short delay after clicking
        return True
    else:
        print(f"{description} not found")
        return False


def back(n=1):
    for _ in range(0, n):
        pyautogui.hotkey("esc")
        time.sleep(SHORT_DELAY())


def no_quitting():
    if pyautogui.locateOnScreen("assets/quit.png", confidence=0.8):
        back()


def wait_loading():
    while pyautogui.locateOnScreen("assets/loading.png", confidence=0.8):
        time.sleep(0.5)
