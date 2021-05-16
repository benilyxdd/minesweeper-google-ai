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

    def extend_possible_moves(self, value):
        self.possible_moves.extend(value)
    
    def clear_possible_moves(self):
        self.possible_moves.clear()

    def extend_must_bombs(self, value):
        self.must_bombs.extend(value)
    
    def clear_must_bombs(self):
        self.must_bombs.clear()

    # methods    
    def play(self):
        self.start_game()
        self.find_all()
        self.process()
        
        while not self.game_finish() and not self.get_finished(): 
            time.sleep(1.5)
            self.find_all()
            if (not self.has_possible_moves() and not self.get_finished()):
                print("That's all my power")
                self.set_finished(True) # the game cannot be finished
                return
            else:
                self.process()
    
    def find_all(self):
        self.scan_board()
        self.find_possible_moves()

    def process(self):
        self.flag_all_must_bomb()
        self.click_all_possible_moves()
            
    def start_game(self):
        # click on the middle to start the game
        self.click_event(self.get_board().get_board()
            [round(self.get_board().get_board_size()[0] / 2 - 1)]
            [round(self.get_board().get_board_size()[1] / 2 - 1)].get_real_piece_position(), 'left'
        )
        time.sleep(2)

    def game_finish(self): 
        for row in self.get_board().get_board():
            for col in row:
                if (not col.get_clicked()) and (not col.get_flagged()): # check the piece is clicked or flagged
                    return False
        return True

    def has_possible_moves(self):
        return (len(self.get_possible_moves()) != 0) # whether the array has element

    def click_event(self, board_position, key):
        pyautogui.click(board_position[0] + self.get_board().get_piece_length() / 2,
                        board_position[1] + self.get_board().get_piece_length() / 2, button = key)
    
    def scan_board(self):
        image = self.screenshot_game()
        for row in self.get_board().get_board():
            for col in row:
                col.search_piece(image)

    def find_possible_moves(self):
        self.extend_possible_moves(self.get_board().find_possible_moves())

    def click_all_possible_moves(self):
        for x, y in self.possible_moves:
            self.click_event(self.get_board().get_board()[x][y].get_real_piece_position(), 'left')
        self.clear_possible_moves()

    def flag_all_must_bomb(self):
        self.extend_must_bombs(self.get_board().find_bomb())
        for x, y in self.get_must_bombs():
            self.get_board().get_board()[x][y].set_bomb()
            self.click_event(self.get_board().get_board()[x][y].get_real_piece_position(), 'right')
        self.clear_must_bombs()

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
        self.get_board().get_board()[9][9].search_piece(image)