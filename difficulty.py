class Difficulty():
    def __init__(self, src):
        self.src = src

    def getDiff(self):
        image = pyautogui.screenshot(region = (0, 100, 120, 59)) # region different on every pc
        image.save('game_screenshot/game.png')

        