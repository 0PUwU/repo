# import pygame
# import sys
# import pygame
# import random
# import sys

import pygame
import random
import sys

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
COLORS = {
    "WHITE": (255, 255, 255), "BLUE": (135, 206, 250), "DARK_BLUE": (25, 25, 112),
    "GREEN": (34, 139, 34), "DARK_GREEN": (0, 100, 0), "BROWN": (139, 69, 19),
    "GRAY": (169, 169, 169), "DARK_GRAY": (105, 105, 105),
    "RED": (255, 0, 0), "PURPLE": (128, 0, 128), "ORANGE": (255, 165, 0)
}

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move Rectangles with Keys")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

# def draw_mountain(screen, x, y, w, h, color):
#     pygame.draw.polygon(screen, COLORS[color], [(x, y), (x + w // 2, y - h), (x + w, y)])

# def draw_tree(screen, x, y):
#     pygame.draw.rect(screen, COLORS["BROWN"], (x + 10, y + 40, 10, 30))
#     pygame.draw.polygon(screen, COLORS["GREEN"], [(x, y + 40), (x + 15, y), (x + 30, y + 40)])

def draw_sky(screen):
    for i in range(SCREEN_HEIGHT // 2):
        pygame.draw.line(screen, (135 - i // 10, 206 - i // 10, 250 - i // 10), (0, i), (SCREEN_WIDTH, i))

# def draw_text(screen, text, font_size, font_name, font_color, position, anti_aliased=True, italic=False, bold=False, rotation=0):
#     font = pygame.font.Font(font_name, font_size)
#     font.set_italic(italic)
#     font.set_bold(bold)
#     text_surface = font.render(text, anti_aliased, font_color)
    
#     text_rect = text_surface.get_rect(center=position)  # Assign text_rect before using it

#     if rotation != 0:
#         text_surface = pygame.transform.rotate(text_surface, rotation)
#         text_rect = text_surface.get_rect(center=position)  # Update text_rect after rotation

#     screen.blit(text_surface, text_rect.topleft)  

def draw_rect(screen, x, y, w, h, color):
    pygame.draw.rect(screen, COLORS[color], (x, y, w, h))
    x1, y1 = 200, 250  # Initial rectangle position

def handle_events(x1, y1, x2, y2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return x1, y1, False # To stop the game
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y1 -= 10 # Move text up
    if keys[pygame.K_DOWN]:
        y1 += 10 # Move text down
    if keys[pygame.K_LEFT]:
        x1 -= 10 # Move text left
    if keys[pygame.K_RIGHT]:
        x1 += 10 # Move text right

    if keys[pygame.K_w]:
        y2 -= 10 # Move text up
    if keys[pygame.K_s]:
        y2 += 10
    if keys[pygame.K_a]:
        x2 -= 10
    if keys[pygame.K_d]:
        x2 += 10

    return x1, y1, x2, y2, True