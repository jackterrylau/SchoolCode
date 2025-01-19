import pygame, os, sys, time, random
from pygame.locals import *

def main():
    ### Step 1. initialize pygame module
    pygame.init()
    ###
    ### Step 2. New a pygame screen window with size(width,height)
    pgWindow = pygame.display.set_mode((600,300))
    # Set Screen widow background Color
    pgWindow.fill((0,255,255))
    pygame.display.set_caption("pygame : Move Object by Keyboard Event")
    ###

    pgFontH1 = pygame.font.Font(None, 40) # font size as 48, None: 不指定字體
    # font_object.render(text, "去除鋸齒?", Text Color, Text Background Color)
    pgWindowText = pgFontH1.render("Move airplane by keyboard",True,(0,0,0))
    # Print text on pygame window which point = (x,y) = (30,50)
    pgWindow.blit(pgWindowText, (30,50)) 

    pgFontContent = pygame.font.Font(None, 20)
    pgWindowContentText1 = pgFontContent.render("Description: Control airplane move left or right with keyboard,",True,(0,0,0))
    pgWindowContentText2 = pgFontContent.render("each step is moved 10 points",True,(0,0,0))


    # Load Image : pygame.transform.load(Image Path)
    air_plane_image = pygame.image.load(os.getcwd() + os.sep + "airplane.png")
    # Resize Image: pygame.transform.scale(IMAGE_OBJECT, (width, height)) => Resize Image
    airPlane = pygame.transform.scale(air_plane_image,(100, 100))

    # 飛機的座標 (x,y)
    air_plane_location_x = 10 ;  air_plane_location_y = 120 

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
            if event.type == pygame.KEYDOWN:
                # 檢查是按下哪個鍵(event.key)
                # pygame.K_UP :向右鍵, pygame.K_RIGHT : 向左鍵, pygame.K_LEFT
                if event.key == pygame.K_RIGHT:
                    air_plane_location_x += 10

                if event.key == pygame.K_LEFT:
                    air_plane_location_x -= 10

        # 更新遊戲畫面
        pgWindow.fill((0,255,255))
        pgWindow.blit(pgWindowText, (30,50)) 
        pgWindow.blit(pgWindowContentText1, (30,80)) 
        pgWindow.blit(pgWindowContentText2, (110,100))
        pgWindow.blit(airPlane,(air_plane_location_x,air_plane_location_y))
        pygame.display.update()

if __name__ == '__main__':
    main()
        