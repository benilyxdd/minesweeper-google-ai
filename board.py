from piece import Piece

class Board():
    def __init__(self, board_size, piece_length, bomb_left):
        self.board_size = board_size
        self.piece_length = piece_length
        self.bomb_left = bomb_left
        self.board = []
        self.set_board()

    def set_board(self):
        piece_position = [0 + self.piece_length / 2, 160 + self.piece_length / 2] # first piece postion
        for row in range(self.board_size[0]):
            row = []
            for col in range(self.board_size[1]):
                row.append((Piece(), (round(piece_position[0]), round(piece_position[1]))))
                piece_position[1] += self.piece_length # next col piece position
            self.board.append(row)
            piece_position[0] += self.piece_length #next row piece position
            piece_position[1] = 160 + self.piece_length