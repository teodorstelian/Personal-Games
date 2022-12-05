import settings


class Lines:

    def __init__(self):
        self.tokens = 0
        self.amount_won = 0

    def check_line(self, squares, tokens):
        self.tokens = tokens
        self.criteria_line(squares)
        return self.amount_won

    def criteria_line(self, squares):
        if squares[0] == squares[1] == squares[2]:
            self.amount_won += self.tokens * settings.WON_MULTIPLIER
