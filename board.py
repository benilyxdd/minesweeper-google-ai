import math
from piece import Piece

class Board():
    def __init__(self, board_size, piece_length, bomb_left, starting_position):
        self.board_size = board_size
        self.piece_length = piece_length
        self.bomb_left = bomb_left
        self.starting_position = starting_position
        self.board = []
        self.set_board()

    # getters
    def get_board_size(self):
        return self.board_size
    
    def get_piece_length(self):
        return self.piece_length
    
    def get_bomb_left(self):
        return self.bomb_left
    
    def get_starting_position(self):
        return self.starting_position  

    def get_board(self):
        return self.board

    def get_board_position(self):
        return self.board_position

    # setters
    def append_board(self, value):
        self.board.append(value)
    
    def append_board_position(self, value):
        self.board_position.append(value)
    
    def miuns_bomb_left(self, value):
        self.bomb_left -= value

    # methods
    def set_board(self):
        piece_position = [ # first piece postion
            self.get_starting_position()[0],
            self.get_starting_position()[1]
        ]
        for row in range(self.get_board_size()[0]):
            row = []
            for col in range(self.get_board_size()[1]):
                row.append(Piece((piece_position[0], piece_position[1]), self.piece_length))
                piece_position[0] += self.get_piece_length() # next col position
            
            self.append_board(row)
            piece_position[1] += self.get_piece_length() #next row position
            piece_position[0] = self.get_starting_position()[0] # reset col position