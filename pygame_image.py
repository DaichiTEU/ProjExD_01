import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img,2.5,1.0),pg.transform.rotozoom(kk_img,5,1.0),pg.transform.rotozoom(kk_img,7.5,1.0),pg.transform.rotozoom(kk_img,10,1.0)]
    tmr = 0
    i = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if (tmr >= 800) and (tmr <= 3200):
            screen.blit(bg_img2,[-tmr+1600,0])
        if tmr <= 1600:
            screen.blit(bg_img,[-tmr,0])
        if tmr >= 2400:
            screen.blit(bg_img,[-tmr+3200,0])
        if tmr == 3200:
            tmr = 0
        if tmr%5 == 4:
            screen.blit(kk_imgs[0],[300,200])
        if tmr%5 == 3:
            screen.blit(kk_imgs[1],[300,200])
        if tmr%5 == 2:
            screen.blit(kk_imgs[2],[300,200])
        if tmr%5 == 1:
            screen.blit(kk_imgs[3],[300,200])
        if tmr%5 == 0:
            screen.blit(kk_imgs[4],[300,200])
        pg.display.update()
        tmr += 1     
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()