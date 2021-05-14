# https://www.google.com/fbx?fbx=minesweeper - target website
from time import sleep
from difficulty import Difficulty
from board import Board
from ai import AI

# let user switch to the page
sleep(3)

# screenshot to get the difficutly from the game
diff = Difficulty().get_diff()

width, height = 1440, 900 # changable
board_size = {'hard' : (20, 24), 'medium' : (14, 18), 'easy' : (8, 10)}
piece_length = {'hard' : 24, 'medium' : 28, 'easy' : 45}
starting_position = (0, 160)

board = Board(board_size[diff], piece_length[diff])

AI(board.board).play()