import pyautogui

class AI():
    def __init__(self, board):
        self.board = board
        self.finished = False
        self.possible_moves = []

    # getters
    def get_finished(self):
        return self.finished

    def get_possible_moves(self):
        return self.possible_moves
    
    # setters
    def set_finished(self, value):
        self.finished = value

    def append_possible_moves(self, value):
        self.possible_moves.append(value)
    
    def clear_possible_moves(self):
        self.possible_moves.clear()

    # methods    
    def play(self):
        self.start_game()
        while not self.game_finish(): 
            if (not self.has_possible_moves()):
                print("The game cannot be finished!")
                self.set_finished(True) # the game cannot be finished
            else:
                pass
            
    def start_game(self):
        # click on (board[0][0]) to start the game
        self.click_event(self.board.get_board_position()[0][0])

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