# https://www.google.com/fbx?fbx=minesweeper - target website
import pyautogui
import keyboard
from time import sleep
from difficulty import Difficulty

# let user redirect to the page
sleep(5)

# screenshot to get the difficutly from the game

diff = getDiff(Difficulty(image))

width, height = 1440, 900
board_size = {'hard' : (20, 24), 'medium' : (14, 18), 'easy' : (8, 10)}
piece_length = {'hard' : 24, 'medium' : 28, 'easy' : 45}
starting_position = (0, 160)

play.ai()