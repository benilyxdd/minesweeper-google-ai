from piece import Piece

class Board():
    def __init__(self, board_size, piece_length):
        self.board_size = board_size
        self.piece_length = piece_length
        self.set_board()

    def set_board(self):
        self.board = []
        for row in range(self.board_size[0]):
            row = []
            for col in range(self.board_size[1]):
                row.append(Piece())
            self.board.append(row)