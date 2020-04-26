import pygame, sys
import pygame.freetype
import time
import random

#Initialization of variables
size = width, height = 320,240
black = 0, 0, 0
white = 255, 255, 255
y = 100
z = 0

#Initialization
screen = pygame.display.set_mode(size)
pygame.freetype.init()
pygame.freetype.font = pygame.freetype.Font(None, 20)
pygame.freetype.font.origin = True

#Function for rendering text
def word_render(lines,x,y):
    time.sleep(0.05)
    dest = (x,y)
    text_colour = random_colour()

    #Screen fils black, then font is rendered on screen
    screen.fill(black)
    pygame.freetype.font.render_to(screen, dest, lines, text_colour)

#Prints character one by one
def character_render(z):
    word = "LoremIpsum"
    text = word[z]
    dest = (150,150)
    pygame.freetype.font.render_to(screen, dest, text, white)
    pygame.display.update()

#Changes the colour of text randomly
def random_colour():
    colour = random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)
    return colour

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    #function call for rendering text at x
    for x in range(0,240,5):
        word_render("Sedlor",x,y)
        z += 1
        if (z > 9):
            z = 0
        character_render(z)

    for x in range(240,0,-5):
        word_render("Sedlor",x,y)
        z += 1
        if (z > 9):
            z = 0
        character_render(z)

    pygame.display.flip()
