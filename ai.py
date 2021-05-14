from board import Board

class AI():
    def __init__(self, board):
        self.board = board
        self.finished = False
        self.possible_moves = []
        
    def play(self):
        self.start_game()
        while not self.game_finish(): 
            if (not self.has_possible_moves()):
                print("The game cannot be finished!")
                self.finished = True # the game cannot be finished
            else:
                pass
            
    def start_game(self):
        # click on (board[0][0]) to start the game
        pass

    def game_finish(self): 
        for row in self.board:
            for col in row:
                if (not col[0].clicked) and (not col[0].flagged): # check the piece is clicked or flagged
                    return False
        return True

    def has_possible_moves(self):
        return self.possible_moves # whether the array has element
