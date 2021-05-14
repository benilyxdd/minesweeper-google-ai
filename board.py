from piece import Piece

class Board():
    def __init__(self, board_size, piece_length, bomb_left):
        self.board_size = board_size
        self.piece_length = piece_length
        self.bomb_left = bomb_left
        self.board = []
        self.board_position = []
        self.set_board()

    # getters
    def get_board_size(self):
        return self.board_size
    
    def get_piece_length(self):
        return self.piece_length
    
    def get_bomb_left(self):
        return self.bomb_left
    
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
        self.bomb_left -= value;

    # methods
    def set_board(self):
        piece_position = [0 + self.get_piece_length() / 2, 160 + self.get_piece_length() / 2] # first piece postion
        for row in range(self.get_board_size()[0]):
            row = []
            row_position = []
            
            for col in range(self.get_board_size()[1]):
                row.append(Piece())
                row_position.append((round(piece_position[0]), round(piece_position[1])))

                piece_position[1] += self.get_piece_length() # next col piece position
            
            self.append_board(row)
            self.append_board_position(row_position)

            piece_position[0] += self.get_piece_length() #next row piece position
            piece_position[1] = 160 + self.get_piece_length()