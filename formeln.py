import numpy as np

import visual
from custom_types import Matrix

max_block_pos_x = visual.max_block_pos_x
max_block_pos_y = visual.max_block_pos_y
blockSize = visual.blockSize


def calculate_electric_field(q: float, epsilon_1: float, num_of_rows: int, num_of_cols: int) -> Matrix:
    """
    Calculates the electric field of a block.
    :param q: The charge
    :param epsilon_1: permittivity
    :param num_of_rows: number of rows
    :param num_of_cols: number of columns
    :return: a flattened field of values
    """
    field_of_values = np.zeros((num_of_rows, num_of_cols))
    k = 8.9875517923e9
    for x in range(num_of_rows):
        for y in range(num_of_cols):
            ex, ey = 0, 0
            for charge in visual.drawn_circles:
                cx, cy = (charge[0] // blockSize), (charge[1] // blockSize)
                dx, dy = cx - x, cy - y
                distance_squared = dx ** 2 + dy ** 2
                if distance_squared != 0:
                    r = np.sqrt(distance_squared)
                    ex += k * q * dx / (epsilon_1 * r ** 3)
                    ey += k * q * dy / (epsilon_1 * r ** 3)
            field_of_values[x, y] = np.sqrt(ex ** 2 + ey ** 2)
    return field_of_values.flatten()
