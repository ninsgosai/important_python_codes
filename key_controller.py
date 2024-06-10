import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, Controller as KeyboardController

mouse = Controller()
keyboard = KeyboardController()

def press_keys():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.alt)
    keyboard.press(Key.shift)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.alt)
    keyboard.release(Key.shift)

def click_and_press_keys():
    mouse.click(Button.left)
    press_keys()

def on_press(key):
    if key == Key.esc:
        return False  # Stop the listener

with Listener(on_press=on_press) as listener:
    while listener.running:
        random_delay = random.randint(1, 5)
        time.sleep(random_delay)
        click_and_press_keys()
