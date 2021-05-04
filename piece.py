class Piece():
    def __init__(self, has_bomb):
        self.has_bomb = has_bomb
        self.flagged = False
        self.clicked = False