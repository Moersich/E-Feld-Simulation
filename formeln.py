import math

import numpy as np
import scipy.constants as constants

import visual

blockSize = visual.blockSize
drawn_circles = visual.drawn_circles


def r_dir(vec_1, vec_2):
    if len(vec_1) == 2 and len(vec_2) == 2:
        result = np.array([vec_2[0] - vec_1[0], vec_2[1] - vec_1[1]])
    elif len(vec_1) == 3 and len(vec_2) == 3:
        result = np.array([vec_2[0] - vec_1[0], vec_2[1] - vec_1[1], vec_2[2] - vec_1[2]])
    else:
        raise ValueError("Both input vectors must have the same dimension, either 2 or 3.")
    return result


def normal_vec(vec_1, vec_2):
    vec = r_dir(vec_1, vec_2)
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    result = vec / norm
    return result


def e_field(q, p_1, p_2, epsilon_r):
    r = r_dir(p_1, p_2)
    r_magnitude_squared = np.dot(r, r)  # or np.sum(r ** 2)
    normal_vector = normal_vec(p_1, p_2)
    k = (1 / (constants.epsilon_0 * epsilon_r * 4 * np.pi))
    if r_magnitude_squared == 0:
        return math.inf
    e = k * (q / r_magnitude_squared) * normal_vector
    return e


def calculate_heatmap(SCREEN, blockSize, drawn_circles):
    q = math.pow(100 * 10, -6)
    num_blocks_x = SCREEN.get_width() // blockSize
    num_blocks_y = SCREEN.get_height() // blockSize
    # print(f"num_blocks_x: {num_blocks_x}, num_blocks_y: {num_blocks_y}")  # Debug print

    # Initialize the heatmap with correct dimensions
    heatmap = np.zeros((num_blocks_y, num_blocks_x))

    if drawn_circles:
        for j in range(num_blocks_y):
            for i in range(num_blocks_x):
                field_strength = 0
                for circle in drawn_circles:
                    p1 = circle
                    p2 = np.array([i * blockSize + blockSize // 2, j * blockSize + blockSize // 2])
                    field = e_field(q, p1, p2, 1)
                    field_strength += np.linalg.norm(field)
                heatmap[j][i] = min(field_strength, 1)  # Ensure the value is capped at 1
                print(f"Heatmap[{j}][{i}] = {heatmap[j][i]}")  # Debug print
    return heatmap
