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
    def search_piece(self, image):
        check_length = round(self.get_piece_length() / 8)
        search_array_x = [-check_length, check_length, 0, 0,
                -check_length, -check_length, check_length, check_length, 0
        ]
        search_array_y = [0, 0, check_length, -check_length,
                -check_length, check_length, -check_length, check_length, 0
        ]
        for check in range(9):
            r, g, b = image.getpixel((self.get_piece_center_position()[0] + search_array_x[check],
                                    self.get_piece_center_position()[1] + search_array_y[check]))
            print(r, g, b)
    
    def configure_piece(self, rgb):
        # rgb(44, 115, 208) 1 (blue) - ok
        # rgb(65, 144, 61) 2 (green) - ok
        # rgb(205, 44, 54) 3 (red) - ok
        # rgb(120, 14, 161) 4 (purple) - ok
        # rgb(249, 144, 33) 5 (orange) - ok
        # rgb(59, 155, 162) 6 (cyan) - cannot find :(
        # rgb(213, 184, 154) 0 - dark - ok
        # rgb(227, 195, 160) 0 - light - ok
        # rgb(165, 211, 76) covered - dark - ok
        # rgb(172, 217, 84) covered - light - ok
        pass