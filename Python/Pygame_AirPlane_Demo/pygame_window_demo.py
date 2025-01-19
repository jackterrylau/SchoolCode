import pygame, os, sys, time, random
from pygame.locals import *

if __name__ == '__main__':
    ### Step 1. initialize pygame module
    pygame.init()
    ###
    ### Step 2. New a pygame screen window with size(width,height)
    pgWindow = pygame.display.set_mode((600,300))
    # Set Screen widow background Color
    pgWindow.fill((0,255,255))
    pygame.display.set_caption("pygame window demo")
    ###
    
    # a font object with size, no assign font type.
    pgFontH1 = pygame.font.Font(None, 40) # font size as 48, None: 不指定字體
    # font_object.render(text, "去除鋸齒?", Text Color, Text Background Color)
    pgWindowText = pgFontH1.render("Hello Pygame World",True,(0,0,0))
    # Print text on pygame window which point = (x,y) = (30,50)
    pgWindow.blit(pgWindowText, (30,50)) 

    pgFontContent = pygame.font.Font(None, 24)
    pgWindowContentText1 = pgFontContent.render("Step 1. initialize pygame module",True,(0,0,0))
    pgWindow.blit(pgWindowContentText1, (50,100))
    pgWindowContentText2 = pgFontContent.render("Step 2. New a pygame screen window with size(width,height)",
                                                True,(0,0,0))
    pgWindow.blit(pgWindowContentText2, (50,120))
    pgWindowContentText3 = pgFontContent.render("Step 3. Event Loop with a quit check",
                                                True,(0,0,0))
    pgWindow.blit(pgWindowContentText3, (50,140))
    
    # ***** 遊戲開始後 需要有一個 迴圈檢測 使用者是不是結束了遊戲 *****
    while True:
        # 取得所有的Event
        for event in pygame.event.get():
            # 如果event是QUIT，也就是按右上角的x
            if event.type == pygame.QUIT:
                # 將pygame殺掉
                pygame.quit()
                # 終止程式
                sys.exit(0)
        # 一直更新pygame的畫面
        pygame.display.update()