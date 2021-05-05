import time
import pyautogui
import keyboard  

x = [422, 450, 560, 620]
y = 462

time.sleep(4)

pyautogui.PAUSE = 0.01
def click(position):
    pyautogui.click(x = position[0], y = position[1])
    time.sleep(0.01)

while keyboard.is_pressed('q') == False:
    for xpos in x:
        position = (xpos, y)
        if pyautogui.pixel(position[0], position[1])[0] == 0:
            print("hi")
            # click(position)

