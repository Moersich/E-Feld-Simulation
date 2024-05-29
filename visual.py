import math

import numpy as np
import pygame

import colors
from colors import Color

import setup

from custom_types import Matrix

SCREEN = pygame.display.set_mode((setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT), pygame.RESIZABLE)
blockSize = 20

max_block_pos_y = setup.num_of_cols * blockSize
max_block_pos_x = setup.num_of_rows * blockSize
charge = setup.q


def set_charge():
    """
    Sets the position of the charge to be drawn
    :return: a position within the grid
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pos = [mouse_x - (mouse_x % blockSize) + blockSize // 2, mouse_y - (mouse_y % blockSize) + blockSize // 2]
    return pos


drawn_circles = []


def draw_all_circles(screen, circles):
    """
    Draws all circles again
    :param screen: the pygame screen where the circles are drawn
    :param circles: the circles to be drawn
    :return: all drawn circles
    """
    for pos in circles:
        pygame.draw.circle(screen, colors.RED, pos, blockSize // 2)
    return drawn_circles


def draw_charge():
    """
    Sets and draws charge on the screen
    :return: a boolean value to indicate if charge is drawn
    """
    pos = set_charge()
    if pos[0] < max_block_pos_x and pos[1] < max_block_pos_y:
        drawn_circles.append(pos)
        pygame.draw.circle(SCREEN, colors.RED, pos, blockSize // 2)
    return True


def draw_grid():
    """
    Draws the grid
    :return:
    """
    global blockSize
    for x in range(0, setup.num_of_rows * blockSize, blockSize):
        for y in range(0, setup.num_of_cols * blockSize, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, colors.BLACK, rect, 1)


def normalize_field(heat_field: Matrix):
    """
    normalizes the heat field, to color it in :meth:`field_to_color`
    :param heat_field: the heat field to be normalized
    """
    max_magnitude = np.max(heat_field)
    if max_magnitude != 0:
        heat_field / max_magnitude


def field_to_color(value: float) -> Color:
    """
    Converts the field value into a color
    :param value: the value to be colored
    :return: color in r,g,b
    """
    blue = colors.BLUE
    red = colors.RED

    mid = (setup.num_of_cols + setup.num_of_rows) / 3
    scaling_factor = mid
    if value != 0:
        exponent = -0.2
        scaled_value = math.pow(math.e, exponent / value * 1 / scaling_factor)
    else:
        scaled_value = 0

    r = int(blue[0] + (red[0] - blue[0]) * scaled_value)
    g = int(blue[1] + (red[1] - blue[1]) * scaled_value)
    b = int(blue[2] + (red[2] - blue[2]) * scaled_value)
    return Color(r, g, b)


def draw_heat(heat_field):
    """
    Draws the heat field into the grid
    :param heat_field: the heat field to be drawn
    :return:
    """
    normalize_field(heat_field)
    index = 0
    for x in range(0, max_block_pos_x, blockSize):
        for y in range(0, max_block_pos_y, blockSize):
            value = heat_field[index]
            color = field_to_color(value)
            pygame.draw.rect(SCREEN, color, pygame.Rect(x, y, blockSize - 1, blockSize - 1))
            index += 1
