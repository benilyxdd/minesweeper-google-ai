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
        self.scan_board()
        self.find_possible_moves()
        
        while not self.game_finish(): 
            if (not self.has_possible_moves()):
                print("The game cannot be finished!")
                self.set_finished(True) # the game cannot be finished
            else:
                self.scan_board()
                self.click_all_possible_moves()
                self.flag_all_possible_bomb()
            
    def start_game(self):
        # click on the middle to start the game
        self.click_event(self.board.get_board_position()
            [round(self.board.get_board_size()[0] / 2 - 1)]
            [round(self.board.get_board_size()[1] / 2 - 1)]
        )

    def game_finish(self): 
        for row in self.board.get_board():
            for col in row:
                if (not col[0].get_clicked()) and (not col[0].get_flagged()): # check the piece is clicked or flagged
                    return False
        return True

    def has_possible_moves(self):
        return self.get_possible_moves() # whether the array has element

    def click_event(self, board_position):
        pyautogui.click(board_position[0], board_position[1])

    def scan_board(self):
        pass

    def find_possible_moves(self):
        pass

    def click_all_possible_moves(self):
        for position in self.possible_moves:
            self.click_event(position)
        self.clear_possible_moves()

    def flag_all_possible_bomb(self):
        pass

    #test
    def click_all(self):
        for row in self.board.get_board_position():
            for col in row:
                self.click_event((
                    col[0] + self.board.get_piece_length() / 2,
                    col[1] + self.board.get_piece_length() / 2
                ))