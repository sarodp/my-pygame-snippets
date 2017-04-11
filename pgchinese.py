# -*- coding: utf-8 -*-
# https://github.com/OptimalBits/vre/blob/master/test/fonts/Cyberbit.ttf

import pygame, sys


unistr = u"黒澤 明"
pygame.font.init()
srf = pygame.display.set_mode((640,480))
f = pygame.font.Font("Cyberbit.ttf",20)
srf.blit(f.render(unistr,True,(0,0,0)),(0,0))
pygame.display.flip()

while True:
    srf.blit(f.render(unistr,True,(255,255,255)),(0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
