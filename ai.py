from PIL.ImageOps import grayscale
import pyautogui
import time

class AI():
    def __init__(self, board):
        self.board = board
        self.finished = False
        self.possible_moves = []
        self.must_bombs = []

    # getters
    def get_finished(self):
        return self.finished

    def get_possible_moves(self):
        return self.possible_moves

    def get_must_bombs(self):
        return self.must_bombs

    def get_board(self):
        return self.board
    
    # setters
    def set_finished(self, value):
        self.finished = value

    def append_possible_moves(self, value):
        self.possible_moves.append(value)
    
    def clear_possible_moves(self):
        self.possible_moves.clear()

    def append_must_bombs(self, value):
        self.must_bombs.append(value)
    
    def clear_must_bombs(self):
        self.must_bombs.clear()

    # methods    
    def play(self):
        self.start_game()
        self.process()
        
        while not self.game_finish(): 
            if (not self.has_possible_moves()):
                print("The game cannot be finished!")
                self.set_finished(True) # the game cannot be finished
            else:
                self.process()
    
    def process(self):
        self.scan_board()
        self.flag_all_must_bomb()
        self.find_possible_moves()
        self.click_all_possible_moves()
            
    def start_game(self):
        # click on the middle to start the game
        self.click_event(self.get_board().get_board()
            [round(self.get_board().get_board_size()[0] / 2 - 1)]
            [round(self.get_board().get_board_size()[1] / 2 - 1)].get_real_piece_position(), 'left'
        )

    def game_finish(self): 
        for row in self.get_board().get_board():
            for col in row:
                if (not col[0].get_clicked()) and (not col[0].get_flagged()): # check the piece is clicked or flagged
                    return False
        return True

    def has_possible_moves(self):
        return self.get_possible_moves() # whether the array has element

    def click_event(self, board_position, key):
        pyautogui.click(board_position[0] + self.get_board().get_piece_length() / 2,
                        board_position[1] + self.get_board().get_piece_length() / 2, button = key)
    
    def scan_board(self):
        image = self.screenshot_game()
        for row in self.get_board().get_board():
            for col in row:
                col.search_piece(image)

    def find_possible_moves(self):
        pass

    def click_all_possible_moves(self):
        for position in self.possible_moves:
            self.click_event(position, 'left')
        self.clear_possible_moves()

    def flag_all_must_bomb(self):
        self.must_bombs.extend(self.get_board().find_bomb())
        for x, y in self.get_must_bombs():
            self.get_board().get_board()[x][y].set_flagged(True)
            self.click_event(self.get_board().get_board()[x][y].get_real_piece_position(), 'right')

    def screenshot_game(self):
        board_size = self.get_board().get_board_size()
        piece_length = self.get_board().get_piece_length()
        # region = (0, 100, board_size[1] * piece_length, board_size[0] * piece_length + 60) for whole game
        image = pyautogui.screenshot(region = (0, 160,
                                     board_size[1] * piece_length, board_size[0] * piece_length))
        image.save('game_screenshot/game.png')
        return image

    # test, will be deleted afterward
    def click_all(self):
        for row in self.get_board().get_board():
            for col in row:
                self.click_event(col.get_real_piece_position(), 'left')

    def get_certain_pixel(self):
        image = self.screenshot_game()
        self.get_board().get_board()[6][6].configure_piece(image)