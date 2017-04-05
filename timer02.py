#! /usr/bin/python3  

# Simple game clock example
# Reference: http://www.pygame.org/docs/ref/time.html

import pygame, sys
from pygame.locals import *

#init global vars
FPS = 200
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
  
def myquit():
    ''' Self explanatory '''
    pygame.quit()
    sys.exit(0)

def TIMER1_tick(xvar):
    xvar+=1
     
  
def main():
    #00-Initialize Pygame
    pygame.init()
  
    #00-init screen
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.get_surface() # This is where images are displayed
    
    pygame.display.set_caption('Game Clock') # Set the window bar title
  
    #01-init font
    font1 = pygame.font.Font(None, 36)
    pgRed = pygame.Color(255, 0, 0)
    pgGreen = pygame.Color(0, 255, 0)
    pgBlue = pygame.Color(0, 0, 255)
    pgWhite = pygame.Color(255, 255, 255)  
    
    #02-init clock
    clock = pygame.time.Clock()
 
    #03-init TIMER1
    TIMER1 = USEREVENT + 1
    pygame.time.set_timer(TIMER1, 1000) # Used to correctly implement seconds
    seconds = 0
  
    while True: # for each frame
	    #1---init screen	
        clock.tick(FPS)
        screen.fill((255, 255, 255))    
        
        #1aa--draw...
        pygame.draw.polygon(window, pgGreen,((146, 0), (291, 106),(236, 277), (56, 277), (0, 106)))
        pygame.draw.circle(window,pgBlue,(300, 50),20,0)
        pygame.draw.ellipse(window,pgRed,(300, 250,40, 80), 1)
        pygame.draw.rect(window, pgRed, (10, 10, 50, 100))
        pygame.draw.line(window, pgBlue, (60, 160), (120, 160),4)

        
        #2a---get clock.xxx
        xcolor1 = (0,111,0)
        xcolor2 = (111,0,0)
        xcolor3 = (0,0,111)
        xcolor = xcolor3
        
        time_display = font1.render("Time: " + str(clock.get_time()), 1, xcolor)
        rawtime_display = font1.render("Raw Time: " + str(clock.get_rawtime()), 1, xcolor)
        fps_display = font1.render("FPS: " + str(clock.get_fps()), 1, xcolor)
        pygame_total_ticks_display = font1.render("Pygame Ticks (total): " + str(pygame.time.get_ticks()), 1, xcolor)
        seconds_display = font1.render("Seconds: " + str(seconds), 1, xcolor)

        #2b---disp clock.xxx
        x0 = 50
        y0 =300
        screen.blit(time_display, (x0, y0+10))
        screen.blit(rawtime_display, (x0, y0+35))
        screen.blit(fps_display, (x0, y0+60))
        screen.blit(pygame_total_ticks_display, (x0, y0+85))
        screen.blit(seconds_display, (x0, y0+110))
        
        
        
        #99--doevents        
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
            elif event.type == TIMER1:
                seconds+=1                        
                print(seconds) 
        #99a--display.frameRefresh
        pygame.display.flip()
 
  
main()
  
