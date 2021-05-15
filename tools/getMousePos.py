import pyautogui
from time import sleep

try: 
    while True:
        x, y = pyautogui.displayMousePosition()
        print(x, y)
        sleep(0.5)
except KeyboardInterrupt:
    print('\n')