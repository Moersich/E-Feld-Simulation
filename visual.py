import pygame

import main

WINDOW_WIDTH = main.WINDOW_WIDTH
WINDOW_HEIGHT = main.WINDOW_HEIGHT
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
RED_APPEND = main.RED_APPEND
RED = (255, 0, 0)
LEFT = main.LEFT
BLACK = main.BLACK
blockSize = main.blockSize
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
    draw_grid()
    draw_all_circles(screen, circles)
    pygame.draw.circle(screen, RED_APPEND, set_charge(), blockSize // 2)


def get_blocks():
    for x in range(0, main.WINDOW_WIDTH, blockSize):
        for y in range(0, main.WINDOW_HEIGHT, blockSize):
            pos = x - (x % blockSize) + blockSize // 2, y - (y % blockSize) + blockSize // 2


def draw_block(x, y, color, size):
    block_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    block_surface.fill(color)
    SCREEN.blit(block_surface, (x, y))


def draw_charge():
    pos = set_charge()
    drawn_circles.append(pos)
    pygame.draw.circle(SCREEN, RED, pos, blockSize // 2)
    return True, pos


def draw_grid():
    global blockSize
    window_width = SCREEN.get_width()
    window_height = SCREEN.get_height()
    blockSize = min(window_width // 40, window_height // 40)  # Adjust based on the number of blocks

    grid_surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
    grid_color = (*BLACK, 100)  # 100 is the alpha value for lower opacity

    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(grid_surface, grid_color, rect, 1)

    SCREEN.blit(grid_surface, (0, 0))


def draw_heatmap(SCREEN, heatmap, blockSize):
    window_width = SCREEN.get_width()
    window_height = SCREEN.get_height()
    num_blocks_x = window_width // blockSize
    num_blocks_y = window_height // blockSize
    # print(f"num_blocks_x (draw): {num_blocks_x}, num_blocks_y (draw): {num_blocks_y}")  # Debug print

    for j in range(num_blocks_y):
        for i in range(num_blocks_x):
            if j < len(heatmap) and i < len(heatmap[j]):  # Ensure indices are within bounds
                intensity = heatmap[j][i]
                color = (255, 0, 0, int(255 * intensity))
                draw_block(i * blockSize, j * blockSize, color, blockSize)
                # print(f"Drawing block at ({i}, {j}) with intensity {intensity}")  # Debug print
            else:
                print(f"IndexError: heatmap[{j}][{i}] is out of range")  # Debug print
