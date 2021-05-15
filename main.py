# https://www.google.com/fbx?fbx=minesweeper - target website
from time import sleep
from difficulty import Difficulty
from board import Board
from ai import AI

# let user switch to the page
sleep(2)
diff = Difficulty().get_diff()

# width, height = 1440, 900 # changable
board_size = {'hard' : (20, 24), 'medium' : (14, 18), 'easy' : (8, 10)}
piece_length = {'hard' : 25, 'medium' : 30, 'easy' : 45}
bombs_number = {'hard': 99, 'medium': 40, 'easy': 10}

# change this
starting_position = (0, 160)

board = Board(board_size[diff], piece_length[diff], bombs_number[diff], starting_position)
AI(board).play()