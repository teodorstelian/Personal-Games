import settings


class Lines:

    def __init__(self):
        self.tokens = 0
        self.amount_won = 0
        self.lines = []

    def check_line(self, squares, tokens):
        self.tokens = tokens
        self.amount_won = 0
        self.add_lines()
        self.criteria_line(squares)
        return self.amount_won

    def add_lines(self):
        self.lines = [settings.LINE1, settings.LINE2, settings.LINE3]

    def criteria_line(self, squares):
        for line in self.lines:
            if squares[line[0]] == squares[line[1]] == squares[line[2]]:
                self.amount_won += self.tokens * settings.WON_MULTIPLIER
