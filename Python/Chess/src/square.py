class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece is not None

    def is_empty(self):
        return not self.has_piece()

    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color

    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    def is_empty_or_enemy(self, color):
        return self.is_empty() or self.has_enemy_piece(color)

    @staticmethod
    def in_range(*args):
        return not any(arg < 0 or arg > 7 for arg in args)
