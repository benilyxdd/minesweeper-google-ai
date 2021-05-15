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
        piece_position = [0, 0]
        for row in range(self.get_board_size()[0]):
            row = []
            for col in range(self.get_board_size()[1]):
                row.append(Piece((piece_position[0], piece_position[1]), self.piece_length, self.starting_position))
                piece_position[0] += self.get_piece_length() # next col position
            
            self.append_board(row)
            piece_position[1] += self.get_piece_length() #next row position
            piece_position[0] = self.get_starting_position()[0] # reset col position
    
    def find_bomb(self):
        search_array_x = [-1, 1, 0, 0, -1, -1, 1, 1]
        search_array_y = [0, 0, 1, -1, -1, 1, -1, 1]
        must_bomb_position = set([])
        row, col = self.get_board_size()
        for row_piece in range(row):
            for piece in range(col):
                covered_and_flagged_count = 0
                possible_bomb_position = set([])
                for search in range(8):
                    x = row_piece + search_array_x[search]
                    y = piece + search_array_y[search]
                    if x > -1 and x < row and y > -1 and y < col:
                        covered_and_flagged_count += (not self.get_board()[x][y].get_clicked() or 
                                                    self.get_board()[x][y].get_flagged())
                        if (not self.get_board()[x][y].get_clicked() and not self.get_board()[x][y].get_flagged()):
                            possible_bomb_position.add((x, y))
                if covered_and_flagged_count == self.get_board()[row_piece][piece].get_bomb_number():
                    must_bomb_position.update(possible_bomb_position)
        return must_bomb_position

    def find_possible_moves(self):
        search_array_x = [-1, 1, 0, 0, -1, -1, 1, 1]
        search_array_y = [0, 0, 1, -1, -1, 1, -1, 1]
        possible_click = set([])
        row, col = self.get_board_size()
        for row_piece in range(row):
            for piece in range(col):
                bomb_near = 0
                possible_moves_position = set([])
                for search in range(8):
                    x = row_piece + search_array_x[search]
                    y = piece + search_array_y[search]
                    if x > -1 and x < row and y > -1 and y < col:
                        bomb_near += (self.get_board()[x][y].get_flagged())
                        if (not self.get_board()[x][y].get_clicked() and 
                            not self.get_board()[x][y].get_flagged()):
                            possible_moves_position.add((x, y))
                if bomb_near == self.get_board()[row_piece][piece].get_bomb_number():
                    possible_click.update(possible_moves_position)
        return possible_click