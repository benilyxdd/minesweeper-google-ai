class Piece():
    def __init__(self, piece_position, piece_length, starting_position):
        self.piece_position = piece_position
        self.piece_length = piece_length
        self.starting_position = starting_position
        self.clicked = False
        self.has_bomb = False
        self.flagged = False
        self.bomb_near = 0 # how many bomb near the piece for now (bomb can see from the current map)
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
        if self.get_flagged() or self.get_clicked():
            return

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
            if (self.check_piece_number((r, g, b))):
                # print(self.get_bomb_number(), self.get_piece_position())
                return
        self.check_clicked(image.getpixel((self.get_piece_center_position()[0],
                                        self.get_piece_center_position()[1])))

    # rgb(165, 211, 76) covered - dark - ok
    # rgb(172, 217, 84) covered - light - ok    
    # check is it clicked
    def check_clicked(self, rgb):
        # rgb(213, 184, 154) 0 - dark - ok
        # rgb(227, 195, 160) 0 - light - ok 
        if (rgb == (213, 184, 154) or rgb == (227, 195, 160)):
            self.set_properties(0)

    # check is there number on grid
    def check_piece_number(self, rgb):
        # rgb(44, 115, 208) 1 (blue) - ok
        # rgb(65, 144, 61) 2 (green) - ok
        # rgb(205, 44, 54) 3 (red) - ok
        # rgb(120, 14, 161) 4 (purple) - ok
        # rgb(249, 144, 33) 5 (orange) - ok
        # rgb(59, 155, 162) 6 (cyan) - cannot find :(
        if (rgb == (44, 115, 208)):
            self.set_properties(1)
            return True
        elif (rgb == (65, 144, 61)):
            self.set_properties(2)
            return True
        elif (rgb == (205, 44, 54)):
            self.set_properties(3)
            return True
        elif (rgb == (120, 14, 161)):
            self.set_properties(4)
            return True
        elif (rgb == (249, 144, 33)):
            self.set_properties(5)
            return True
        elif (rgb == (59, 155, 162)): # not confirm
            self.set_properties(6)
            return True
        return False
    
    def set_properties(self, value):
        self.set_clicked(True)
        self.set_has_bomb(False)
        self.set_bomb_number(value)

    def set_bomb(self):
        self.set_bomb(True)
        self.set_flagged(True)