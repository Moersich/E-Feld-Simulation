import math

import numpy as np
import scipy.constants as constants

import visual
from visual import SCREEN


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
        raise ValueError("Cannot normalize a zero vector.")
    result = vec / norm
    return result


def e_field(q, p_1, p_2, epsilon_r):
    r = r_dir(p_1, p_2)
    r_magnitude_squared = np.dot(r, r)  # or np.sum(r ** 2)
    normal_vector = normal_vec(p_1, p_2)
    k = (1 / (constants.epsilon_0 * epsilon_r * 4 * np.pi))
    e = k * (q / r_magnitude_squared) * normal_vector
    return e


def calculations():
    q = math.pow(100 * 10, -6)
    i = 1
    j = 1
    x = 0
    while i != SCREEN.get_width() and j != SCREEN.get_height():
        p1 = visual.drawn_circles.index(x)
        p2 = np.array([i, j])
        sol = e_field(q, p1, p2, 1)
        print(sol)
        i += 1
        j += 1
        x += 1
