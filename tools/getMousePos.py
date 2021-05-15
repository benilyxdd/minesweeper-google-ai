import pyautogui
from time import sleep

try: 
    while True:
        x, y = pyautogui.displayMousePosition()
        print(x, y, flush=True)
        sleep(0.5)
except KeyboardInterrupt:
    print('\n')