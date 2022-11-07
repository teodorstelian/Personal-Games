import pygame
from pygame import locals

from settings import Settings

pygame.init()

# Define settings
screen_width = Settings.Width
screen_height = Settings.Height
tile_size = Settings.Tile_Size

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Test')

# Load images
background_img = pygame.image.load(Settings.Background)
sun_img = pygame.image.load(Settings.Sun)


def draw_grid():
    for line in range(30):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


run = True

while run:

    screen.blit(background_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
