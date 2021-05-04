import pyautogui
from time import sleep

try: 
    while True:
        x, y = pyautogui.position()
        print(x, y, flush=True)
        sleep(1)
except KeyboardInterrupt:
    print('\n')