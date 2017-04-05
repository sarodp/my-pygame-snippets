# From http://inventwithpython.com

# http://inventwithpython.com/cat.png
# http://inventwithpython.com/bounce.wav
# http://inventwithpython.com/background.mid

#"""
#Game loop :
#* handle event
#* update game state
#* draw screen
#"""

# ----------------------------------
#! /usr/bin/python3

import pygame, sys
from pygame.locals import *
# pygame.locals has the constants like QUIT, MOUSEMOTION, and K_ESCAPE

# init needs to be called before any other pygame code.
pygame.init()
# the Clock object makes sure our program run (at most at a certain FPS)
fps_clock = pygame.time.Clock()

# set_mode() create the window Pram is (width, height) in piels.
# The Surface object returned is drawn to the screen when
# pygame.display.update() is called
windos_surface_obj = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pygame cheat sheet")

# load() will return a Surface object with the imgae drawn on it.
# Can be png, gif, bmp, jpg and others.
cat_sirface_obj = pygame.image.load("cat.png")
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)
white_color = pygame.Color(255, 255, 255)
mousex, mousey = 0, 0

# Create a Font object with a font size of 32
font_obj = pygame.font.Font("freesansbold.ttf", 32)
msg = "Hello World !"

# Load a background sound.
#and only one sound file can be loaded at a time.
pygame.mixer.music.load("background.mid")
# The first parameter give the number of time the music should be repeated (after
# the first play). -1 -> infinit time
# The second parameter give the starting position of the song playing (seconds)
pygame.mixer.music.play(-1, 0.0)
# To stop the music.
#pygame.mixer.music.stop()
# Create a Sound object from a file (wav, ogv or mp3)
# Will only be played when we specifically want them to.
sound_obj = pygame.mixer.Sound("bounce.wav")

# This loop is the main application loop
while True:
    # The fill() function will completely fill the Surface with white.
    windos_surface_obj.fill(white_color)
    
    # Draw functions draw shape to a specific Surface object with a specific
    # color (a Color or a (R, G, B) tuple of integer).
    # Coordinates are either (x, y) or (top, left, width, height)
    # the last parameter is the width, '0' means filled in and no param
    # default to a width of 1 pixel.
    pygame.draw.polygon(windos_surface_obj, green_color, ((146, 0), (291, 106),
                                             (236, 277), (56, 277), (0, 106))) 
    pygame.draw.circle(windos_surface_obj, blue_color, (300, 50), 20, 0)
    pygame.draw.ellipse(windos_surface_obj, red_color, (300, 250, 40, 80), 1)
    pygame.draw.rect(windos_surface_obj, red_color, (10, 10, 50, 100))
    pygame.draw.line(windos_surface_obj, blue_color, (60, 160), (120, 160),4)
    
    # To draw individual pixel on a Surface, create a PixelAray object.
    # After making change, you must delete the PixelArray object.
    pix_arr = pygame.PixelArray(windos_surface_obj)
    for x in range(100, 200, 4):
        for y in range(100, 200, 4):
            pix_arr[x][y] = red_color
    del pix_arr
    
    # blit() method draws one Surface to another Surface, specifying the
    # (left, top) coordinates.
    windos_surface_obj.blit(cat_sirface_obj, (mousex, mousey))
    
    # render() creates a Surface object with the text drawn on it in the
    # specified font and color.
    msg_surface_obj = font_obj.render(msg, False, blue_color)
    msg_rect_obj = msg_surface_obj.get_rect()
    # Rect objects have attributes for specifying their position and size.
    msg_rect_obj.topleft = (10, 20)
    windos_surface_obj.blit(msg_surface_obj, msg_rect_obj)
    
    # pygame.event.get() returns a list off all Event objects that happened
    # since the last time get() was called.
    # The Event object has type, pos, key and other attributes depending on
    # type of event it is.
    for event in pygame.event.get():
        if event.type == QUIT:
            # quit() is the opposite of init()
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            # Call play() method to play the sound. The code continues on
            # while it plays.
            sound_obj.play()
            if event.button in (1, 2, 3):
                msg = "left, middle or right mouse click"
            elif event.button in (4, 5):
                msg = "mouse scrolled up or down"
                
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                msg = ("Arrow key pressed")
            if event.key == K_a:
                msg = "'a' key pressed"
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    
    # The window is not drawn to the actual screen until 
    # pyagme.display.update() is called.
    pygame.display.update()
    # wait long enough to run at 30 frame per second.
    # To call after pyagme.display.update()
    fps_clock.tick(30)
