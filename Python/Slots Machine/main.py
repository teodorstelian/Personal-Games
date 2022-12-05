import settings
from lines import Lines
from machine import Machine

tokens = settings.TOKENS


class Main:

    def __init__(self):
        self.tokens = tokens
        self.machine = Machine()
        self.lines = Lines()

    def main_loop(self):

        print("Welcome to the CASINO.")
        while self.tokens > 0:
            print(f"You have {self.tokens} tokens")

            try:
                bet = int(input("Bet amount: "))
            except Exception:
                print("Please enter a number of tokens")
                continue

            if bet > self.tokens:
                print("Not enough tokens")
            else:
                self.tokens -= bet

                squares = self.machine.generate_lines()

                amount_won = self.lines.check_line(squares, bet)

                if amount_won > 0:
                    print(f"You won {amount_won} tokens.")
                else:
                    print("You lost this time.")

        print("You are out of tokens.")
        print("Thank you for playing.")
        print()


main = Main()
main.main_loop()
