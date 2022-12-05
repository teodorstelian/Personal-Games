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

        self.generate_squares()
        squares = self.squares

        print()

        print("|", squares[0], "|", squares[1], "|", squares[2], "|")
        print("--------------")

        print("|", squares[3], "|", squares[4], "|", squares[5], "|")
        print("--------------")

        print("|", squares[6], "|", squares[7], "|", squares[8], "|")
        print()

        return squares
