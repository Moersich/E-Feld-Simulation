import sys

import pygame

import visual

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED_APPEND = (255, 100, 100)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
LEFT = 1


def main():
    global SCREEN, CLOCK


if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
                SCREEN.fill(WHITE)
                visual.draw_grid(WINDOW_WIDTH, WINDOW_HEIGHT)
            if event.type == pygame.FULLSCREEN:
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                visual.draw_charge()

        visual.draw_grid(WINDOW_WIDTH, WINDOW_HEIGHT)
        visual.append_hover_charge(SCREEN, visual.drawn_circles)
        pygame.display.update()
        CLOCK.tick(60)
