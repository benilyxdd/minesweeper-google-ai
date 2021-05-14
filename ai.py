from board import Board

class AI():
    def __init__(self, board):
        self.board = board
        self.finished = False
        

    def play(self):
        self.start_game()
        print(self.board)

    def start_game(self):
        pass