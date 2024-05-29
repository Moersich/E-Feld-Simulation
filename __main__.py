import sys

import pygame

import colors
import formeln
import input
import setup
import visual


def main():
    global SCREEN, CLOCK


if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(colors.WHITE)
    heat_field = formeln.calculate_electric_field(0, setup.epsilon_1, setup.num_of_rows, setup.num_of_cols)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
                visual.draw_grid()
            if event.type == pygame.FULLSCREEN:
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == input.LEFT_MOUSE_BUTTON:
                charge = visual.draw_charge()
                heat_field = formeln.calculate_electric_field(charge, setup.epsilon_1, setup.num_of_rows,
                                                              setup.num_of_cols)

        visual.draw_heat(heat_field)
        visual.draw_grid()
        pygame.display.update()
        CLOCK.tick(60)
