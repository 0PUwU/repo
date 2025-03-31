# Owen Perez
# 3/21/2025
# repo

import pygame
import random
import sys
import config

def main():
    screen = config.init_game()
    clock = pygame.time.Clock()

    running = True
    x1, y1 = 200, 250  # Initial rectangle position
    x2, y2 = 200, 200  # Initial rectangle position

    while running:
        screen.fill(config.COLORS["DARK_GREEN"])
        config.draw_sky(screen)

        # Draw movable rectangle
        config.draw_rect(screen, x1, y1, 100, 500, "RED")
        #second rectangle
        config.draw_rect(screen, x2, y2, 200, 55, "GREEN")

        # Handle events to update x1, y1
        x1, y1, x2, y2, running = config.handle_events(x1, y1, x2, y2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()