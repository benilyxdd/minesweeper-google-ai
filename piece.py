class Piece():
    def __init__(self, piece_position, piece_length, starting_position):
        self.piece_position = piece_position
        self.piece_length = piece_length
        self.starting_position = starting_position
        self.clicked = False
        self.has_bomb = None
        self.flagged = False
        self.bomb_near = 0 # how many bomb near the piece for now
        self.bomb_number = None # what is the number show in game
    
    # getters
    def get_piece_position(self):
        return self.piece_position
    
    def get_real_piece_position(self):
        return (self.piece_position[0] + self.starting_position[0],
                self.piece_position[1] + self.starting_position[1])

    def get_piece_center_position(self):
        return (self.piece_position[0] + round(self.piece_length / 2),
                self.piece_position[1] + round(self.piece_length / 2))

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
    def configure_piece(self, image):
        # rgb(44, 115, 208) 1 (blue)
        # rgb(122, 166, 104) 2 (green)
        # rgb(205, 44, 54) 3 (red)
        # rgb(121, 18, 161) 4 (purple)
        # rgb(249, 144, 33) 5 (orange)
        # rgb(59, 155, 162) 6 (cyan)
        # rgb(213, 184, 154) 0 - dark
        # rgb(227, 195, 160) 0 - light
        # rgb(187, 223, 121) covered - dark
        # rgb(193, 227, 127) covered - light
        r, g, b = image.getpixel(self.get_piece_center_position())
        print(r, g, b)