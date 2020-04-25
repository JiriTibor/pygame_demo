import pygame, sys
import pygame.freetype
import time
import random

size = width, height = 320,240
black = 0, 0, 0
white = 255, 255, 255
y = 100

screen = pygame.display.set_mode(size)

def word_render(lines):
    time.sleep(0.05)
    dest = (x,y)
    text_colour = random_colour()

    screen.fill(black)
    pygame.freetype.init()
    pygame.freetype.font = pygame.freetype.Font(None, 20)
    pygame.freetype.font.origin = True
    pygame.freetype.font.render_to(screen, dest, lines, text_colour)
    pygame.display.flip()

def random_colour():
    colour = random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)
    return colour

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    lines = "Sedlor"

    for x in range(0,240,5):
        word_render(lines)

    for x in range(240,0,-5):
        word_render(lines)

    pygame.display.flip()
