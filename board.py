from piece import Piece

class Board():
    def __init__(self, board_size):
        self.board_size = board_size

    def set_board(self):
        self.board = []
        for row in range(self.board_size[0]):
            row = []
            for col in range(self.board_size[1]):
                piece = Piece(False)
                row.append(piece)
            self.board.append(row)
