import pygame, sys
import pygame.freetype
import time
import random

#Initialization of global variables
size = width, height = 320,240
blue = 0, 0, 255
white = 255, 255, 255
y = 100
z = 0
word = "Test"

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
    pygame.freetype.font.render_to(screen, dest, lines, text_colour)
    pygame.display.update()

#Prints character one by one
def character_render(z):
    text = word[z]
    dest = (150,150)

    pygame.freetype.font.render_to(screen, dest, text, white)
    pygame.display.update()

def render(word,x,y,z):
    screen.fill(blue)
    #Function call to render moving word
    word_render(word,x,y)
    #Function call to render single character
    z = character_render(z)

#Changes the colour of text randomly
def random_colour():
    colour = random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)
    return colour

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for x in range(0,width,5):
        z += 1
        if (z > len(word)-1):
            z = 0
        render(word,x,y,z)

    for x in range(width,0,-5):
        z += 1
        if (z > len(word)-1):
            z = 0
        render(word,x,y,z)

    pygame.display.flip()
