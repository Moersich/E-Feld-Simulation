import math

import numpy as np
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
num_of_rows = main.num_of_rows
num_of_cols = main.num_of_cols
max_block_pos_y = num_of_cols * blockSize
max_block_pos_x = num_of_rows * blockSize
BLUE = main.BLUE
WHITE = main.WHITE
charge = main.q


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
    pos = set_charge()
    screen.fill(WHITE)
    draw_grid()
    draw_all_circles(screen, circles)
    if 0 < pos[0] < max_block_pos_x and 0 < pos[1] < max_block_pos_y:
        pygame.draw.circle(screen, RED_APPEND, set_charge(), blockSize // 2)


def draw_charge():
    pos = set_charge()
    if pos[0] < max_block_pos_x and pos[1] < max_block_pos_y:
        drawn_circles.append(pos)
        pygame.draw.circle(SCREEN, RED, pos, blockSize // 2)
    return True


def draw_grid():
    global blockSize
    for x in range(0, num_of_rows * blockSize, blockSize):
        for y in range(0, num_of_cols * blockSize, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def normalize_field(heat_field):
    max_magnitude = np.max(heat_field)
    if max_magnitude != 0:
        return heat_field / max_magnitude
    else:
        return heat_field


def field_to_color(value):
    blue = (0, 0, 255)
    red = (255, 0, 0)

    mid = (num_of_cols + num_of_rows) / 3
    scaling_factor = mid
    if value != 0:
        exponent = -0.2  # You can adjust this value to control the rate
        scaled_value = math.pow(math.e, exponent / value * 1 / scaling_factor)
    else:
        scaled_value = 0

    r = int(blue[0] + (red[0] - blue[0]) * scaled_value)
    g = int(blue[1] + (red[1] - blue[1]) * scaled_value)
    b = int(blue[2] + (red[2] - blue[2]) * scaled_value)
    return r, g, b


def draw_heat(heat_field):
    normalized_field = normalize_field(heat_field)
    index = 0
    for x in range(0, max_block_pos_x, blockSize):
        for y in range(0, max_block_pos_y, blockSize):
            value = normalized_field[index]
            color = field_to_color(value)
            pygame.draw.rect(SCREEN, color, pygame.Rect(x, y, blockSize - 1, blockSize - 1))
            index += 1
