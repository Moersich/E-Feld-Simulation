import sys

import pygame

import formeln
import visual

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED_APPEND = (255, 100, 100)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
LEFT = 1
blockSize = 20


def main():
    global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, blockSize
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    drawn_circles = []  # Initialize the list of drawn circles

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                old_surface_saved = SCREEN
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                surface.blit(old_surface_saved, (0, 0))
                WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
                SCREEN.fill(WHITE)
                visual.draw_grid()
                heatmap = formeln.calculate_heatmap(SCREEN, blockSize, drawn_circles)
                visual.draw_heatmap(SCREEN, heatmap, blockSize)
                del old_surface_saved
            if event.type == pygame.FULLSCREEN:
                SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                visual.draw_charge()
                print(visual.drawn_circles)

        SCREEN.fill(WHITE)
        visual.draw_grid()
        heatmap = formeln.calculate_heatmap(SCREEN, blockSize, drawn_circles)
        visual.draw_heatmap(SCREEN, heatmap, blockSize)
        visual.append_hover_charge(SCREEN, visual.drawn_circles)
        pygame.display.update()
        CLOCK.tick(60)


if __name__ == '__main__':
    main()
