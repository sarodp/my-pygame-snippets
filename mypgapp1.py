#! /usr/bin/python  
# -*- coding: utf-8 -*-

# Simple game clock example
# Reference: http://www.pygame.org/docs/ref/time.html

import pygame, sys
from pygame.locals import *

import time
import os
import sys
import random
import RPi.GPIO as GPIO


#init global vars
xcounter1 = 0

  
def myquit():
    ''' Self explanatory '''
    pygame.quit()
    sys.exit(0)

def TIMER1_tick(xvar):
    xvar+=1

def switchDN(channel):
	global xcounter1
	xcounter1 -=1

def switchUP(channel):
	global xcounter1
	xcounter1 +=1

def switchRND(channel):
	global xcounter1
	xcounter1 = random.randint(0,100)
     
def initGPIO():
	#02--set IO, interrupt/callback
	swUP = 16
	swDN = 18
	swRND = 22
	
	#debounce time in msec.
	msecdebounce = 300  
	
	#configure as board
	GPIO.setmode(GPIO.BOARD)                                 
	
	# pull up active, we can use ground closure
	GPIO.setup(swUP, GPIO.IN, pull_up_down=GPIO.PUD_UP)        
	GPIO.setup(swDN, GPIO.IN, pull_up_down=GPIO.PUD_UP)        
	GPIO.setup(swRND, GPIO.IN, pull_up_down=GPIO.PUD_UP)        

	# interrupt & callback
	GPIO.add_event_detect(swUP, GPIO.FALLING, callback=switchUP, bouncetime=msecdebounce)
	GPIO.add_event_detect(swDN, GPIO.FALLING, callback=switchDN, bouncetime=msecdebounce) 
	GPIO.add_event_detect(swRND, GPIO.FALLING, callback=switchRND, bouncetime=msecdebounce) 


#--init PG screenvar
FPS = 10
SCREEN_HEIGHT = 600 					#900,800,700,600
SCREEN_WIDTH = SCREEN_HEIGHT * 16 / 9 	#1600
  
def main():
    global xcounter1 
    
    #00--init GPIO
    initGPIO()

    #00-Initialize Pygame
    pygame.init()
  
    #00-init screen
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.get_surface() # This is where images are displayed
    
    pygame.display.set_caption('Game Clock') # Set the window bar title
  
    #01-init fonts, colors
    pgRed = pygame.Color(255, 0, 0)
    pgGreen = pygame.Color(0, 255, 0)
    pgBlue = pygame.Color(0, 0, 255)
    pgWhite = pygame.Color(255, 255, 255)  
    pgGray = pygame.Color(235, 235, 235)  
    
    #/usr/share/fonts/...    
    fonts36 = pygame.font.SysFont('droidsans', 28)
    fonts28 = pygame.font.SysFont('droidsans', 24)
    fonts24 = pygame.font.SysFont('droidsans', 16)
    fonts16 = pygame.font.SysFont('droidsans', 14)
    
    #/working path/*.ttf
    font36 = pygame.font.Font('Waree.ttf', 36)
    font28 = pygame.font.Font('Waree.ttf', 28)
    font24 = pygame.font.Font('Waree.ttf', 24)
    font16 = pygame.font.Font('Waree.ttf', 16)
    
    xGray = (240,240,240)
    xWhite = (255,255,255)
    xcolor1 = (0,111,0)
    xcolor2 = (111,0,0)
    xcolor3 = (0,0,111)
    
    #02-init clock
    clock = pygame.time.Clock()
 
    #03-init PGTIMER1
    PGTIMER1 = USEREVENT + 1
    pygame.time.set_timer(PGTIMER1, 1000) # Used to correctly implement seconds
    seconds = 0
  
    while True: # for each frame
	    #1---init screen	
        clock.tick(FPS)
        screen.fill(xGray)    
        x0 =20
        y0 =300
        
        #1aa--draw...
        pygame.draw.rect(window, pgWhite, (10, 10, SCREEN_WIDTH-20, y0-30))
 
        pygame.draw.polygon(window, pgGreen,((146, 0), (291, 106),(236, 277), (56, 277), (0, 106)))
        pygame.draw.circle(window,pgBlue,(300, 50),20,0)
        pygame.draw.ellipse(window,pgRed,(300, 250,40, 80), 1)
        pygame.draw.rect(window, pgRed, (10, 10, 50, 100))
        pygame.draw.line(window, pgBlue, (60, 160), (120, 160),4)

        pygame.draw.rect(window, pgWhite, (x0, y0, SCREEN_WIDTH-40, SCREEN_HEIGHT-y0-20))
 
        
        #2a---render(text.xxx)
        RDseconds = font24.render("Timer1 Seconds: " + str(seconds), 1, xcolor3)
        RDxcounterlbl = font24.render(u"GPIO counter1 นับเลขได้: " , 1, xcolor3)
        RDxcounterval = font24.render( ("%4d" % xcounter1), 1, xcolor3)

        RDpgtime = font16.render("PG Time: " + str(clock.get_time()), 1, xcolor1)
        RDpgrawtime = font16.render("PG Raw Time: " + str(clock.get_rawtime()), 1, xcolor1)
        
        RDfps = font16.render(("FPS: %3.1f" % clock.get_fps()), 1, xcolor2)
        RDpgticktotal = font16.render("PG Ticks total: " + str(pygame.time.get_ticks()), 1, xcolor2)
        

        #2b---blit(text.xxx)
        screen.blit(RDseconds, (x0+10, y0+10))

        screen.blit(RDxcounterlbl, (x0+10, y0+35))

        pygame.draw.rect(window, pgGray, (x0+400, y0+35, 100,25 ))
        screen.blit(RDxcounterval, (x0+450, y0+35))

        screen.blit(RDpgtime, (x0+10, SCREEN_HEIGHT-40-15))
        screen.blit(RDpgrawtime, (x0+10,SCREEN_HEIGHT-40))
        
        screen.blit(RDfps, (SCREEN_WIDTH/2,SCREEN_HEIGHT-40-15))
        screen.blit(RDpgticktotal, (SCREEN_WIDTH/2,SCREEN_HEIGHT-40))
        
        
        
        
        #99--doevents        
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
            elif event.type == PGTIMER1:
                seconds+=1                        
                print(seconds) 
                
        #99a--display.frameRefresh
        pygame.display.flip()
 
if __name__ == "__main__":
	main()
  
