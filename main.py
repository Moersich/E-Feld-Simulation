import sys

import pygame

import formeln
import visual

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED_APPEND = (255, 100, 100)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
LEFT = 1
num_of_rows = 40
num_of_cols = 40
q = 1 * 10 ** (-6)
epsilon_1 = 1


def main():
    global SCREEN, CLOCK


if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    heat_field = formeln.calculate_electric_field(q, epsilon_1, num_of_rows, num_of_cols)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
                SCREEN.fill(WHITE)
                visual.draw_grid()
            if event.type == pygame.FULLSCREEN:
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                visual.draw_charge()
                heat_field = formeln.calculate_electric_field(q, epsilon_1, num_of_rows, num_of_cols)

        visual.append_hover_charge(SCREEN, visual.drawn_circles)
        visual.draw_heat(heat_field)
        visual.draw_grid()
        pygame.display.update()
        CLOCK.tick(60)
