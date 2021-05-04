import pyautogui
from time import sleep

sleep(3)
image = pyautogui.screenshot(region = (0, 100, 120, 59))
image.save('game_screenshot/game.png')