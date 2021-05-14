from PIL.ImageOps import grayscale
import pyautogui

class Difficulty():
    def __init__(self):
        pass

    def get_diff(self):
        # image = pyautogui.screenshot(region = (0, 100, 120, 59)) # region different on every pc
        # image.save('game_screenshot/difficulty.png')
        while True:
            if pyautogui.locateOnScreen('images/easy_tag.png', region = (0, 100, 120, 60), grayscale = True) != None:
                return 'easy'
            elif pyautogui.locateOnScreen('images/medium_tag.png', region = (0, 100, 120, 60), grayscale = True) != None:
                return 'medium'
            elif pyautogui.locateOnScreen('images/hard_tag.png', region = (0, 100, 120, 60), grayscale = True) != None:
                return 'hard'        