class Piece():
    def __init__(self, piece_position, piece_length):
        self.piece_position = piece_position
        self.piece_length = piece_length
        self.clicked = False
        self.has_bomb = None
        self.flagged = False
        self.bomb_near = 0 # how many bomb near the piece for now
        self.bomb_number = None # what is the number show in game
    
    # getters
    def get_piece_position(self):
        return self.piece_position

    def get_piece_length(self):
        return self.piece_length

    def get_clicked(self):
        return self.clicked

    def get_has_bomb(self):
        return self.has_bomb
    
    def get_flagged(self):
        return self.flagged
    
    def get_bomb_near(self):
        return self.bomb_near

    def get_bomb_number(self):
        return self.bomb_number

    # setters
    def set_clicked(self, value):
        self.clicked = value
    
    def set_has_bomb(self, value):
        self.has_bomb = value

    def set_flagged(self, value):
        self.flagged = value

    def set_bomb_near(self, value):
        self.bomb_near = value

    def set_bomb_number(self, value):
        self.bomb_number = value

    # methods
    