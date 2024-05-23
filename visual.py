import pygame

import main

WINDOW_WIDTH = main.WINDOW_WIDTH
WINDOW_HEIGHT = main.WINDOW_HEIGHT
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
RED_APPEND = main.RED_APPEND
RED = (255, 0, 0)
LEFT = main.LEFT
BLACK = main.BLACK
blockSize = 20
WHITE = main.WHITE

def set_charge():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pos = [mouse_x - (mouse_x % blockSize) + blockSize // 2, mouse_y - (mouse_y % blockSize) + blockSize // 2]
    return pos


drawn_circles = []


def draw_all_circles(screen, circles):
    for pos in circles:
        pygame.draw.circle(screen, RED, pos, blockSize // 2)
    return drawn_circles


def append_hover_charge(screen, circles):
    screen.fill(WHITE)
    draw_grid(WINDOW_WIDTH, WINDOW_HEIGHT)
    draw_all_circles(screen, circles)
    pygame.draw.circle(screen, RED_APPEND, set_charge(), blockSize // 2)


def draw_charge():
    pos = set_charge()
    drawn_circles.append(pos)
    pygame.draw.circle(SCREEN, RED, pos, blockSize // 2)
    return True


def draw_grid(window_width, window_height):
    global blockSize
    window_width = SCREEN.get_width()
    window_height = SCREEN.get_height()
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
