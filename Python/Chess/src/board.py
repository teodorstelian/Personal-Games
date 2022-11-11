import itertools
from settings import *
from square import Square
from piece import *
from move import Move


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # The piece has moved
        piece.moved = True

        # Clear valid moves
        piece.clear_moves()

        # Set last move
        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.moves

    def calculate_moves(self, piece, row, col):
        """
        Calculate all the possible moves of a specific piece
        """

        def pawn_moves():
            # Steps
            steps = 1 if piece.moved else 2
            # Vertical Moves
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))

            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].is_empty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        move = Move(initial, final)
                        piece.add_move(move)
                    # Blocked
                    else:
                        break
                # Not in range
                else:
                    break

            # Diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col - 1, col + 1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

            # En passant
            # TO DO

            # Promotion
            # TO DO

        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row - 2, col - 1),
            ]

            for possible_move in possible_moves:
                pm_row, pm_col = possible_move
                if Square.in_range(pm_row, pm_col):
                    if self.squares[pm_row][pm_col].is_empty_or_enemy(piece.color):
                        # Create new move
                        initial = Square(row, col)
                        final = Square(pm_row, pm_col)
                        move = Move(initial, final)
                        piece.add_move(move)

        def straight_line_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):

                        # Create the squares of the possible moves
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)

                        # Empty = Continue Looping
                        if self.squares[possible_move_row][possible_move_col].is_empty():
                            piece.add_move(move)

                        # Has enemy piece = Add Move + Break
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            piece.add_move(move)
                            break

                        # Has team piece = Break
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break

                    # Not in range
                    else:
                        break

                    # Incrementing
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            all_moves = [
                (row - 1, col - 1),  # up-left
                (row - 1, col),  # up
                (row - 1, col + 1),  # up-right
                (row, col - 1),  # left
                (row, col + 1),  # right
                (row + 1, col - 1),  # bottom-left
                (row + 1, col),  # bottom
                (row + 1, col + 1)  # bottom-right
            ]

            # Normal moves
            for move in all_moves:
                possible_move_row, possible_move_col = move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        # Create new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

            # Castling moves

            # Queen Castling

            # King Castling

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straight_line_moves([
                (-1, 1),  # up-right
                (-1, -1),  # up-left
                (1, 1),  # bottom-right
                (1, -1)  # bottom-left
            ])

        elif isinstance(piece, Rook):
            straight_line_moves([
                (-1, 0),  # up
                (1, 0),  # down
                (0, -1),  # left
                (0, 1)  # right
            ])

        elif isinstance(piece, Queen):
            straight_line_moves([
                (-1, 1),  # up-right
                (-1, -1),  # up-left
                (1, 1),  # bottom-right
                (1, -1),  # bottom-left
                (-1, 0),  # up
                (1, 0),  # down
                (0, -1),  # left
                (0, 1)  # right
            ])

        elif isinstance(piece, King):
            king_moves()

    def _create(self):

        for row, col in itertools.product(range(ROWS), range(COLS)):
            self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):

        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 1, Rook(color))
        self.squares[row_other][7] = Square(row_other, 6, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))
