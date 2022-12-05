import random
import settings

symbols = settings.SYMBOLS


class Machine:

    def __init__(self):
        self.squares = []

    def generate_squares(self):
        for _ in range(9):
            self.squares += random.choice(symbols)

    def generate_lines(self):

        self.squares = []
        self.generate_squares()
        squares = self.squares

        for row in range(3):
            print("|", squares[3*row], "|", squares[3*row+1], "|", squares[3*row+2], "|")
            print("--------------")

        return squares
