import itertools
import pygame

from settings import *
from board import Board
from dragger import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # Show methods

    def show_bg(self, surface):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            color = LIGHT_GREEN if (row + col) % 2 == 0 else DARK_GREEN
            rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

            pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row, col in itertools.product(range(ROWS), range(COLS)):
            if self.board.squares[row][col].has_piece():
                piece = self.board.squares[row][col].piece

                # All pieces except the one dragged
                if piece is not self.dragger.piece:
                    piece.set_texture(size=80)
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            # Loop all valid moves
            for move in piece.moves:
                # color
                color = MOVING_COLOR if (move.final.row + move.final.col) % 2 == 0 else MOVING_COLOR_2
                # rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
