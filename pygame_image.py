import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1:背景画像surfaceの生成
    bg2_img = pg.transform.flip(bg_img,True,False)
    tori_img = pg.image.load("ex01/fig/3.png")#練習2:こうかとん画像surfaceの生成
    tori_img = pg.transform.flip(tori_img,True,False)#練習2:こうかとんの反転
    tori_imgs = [tori_img,
                 pg.transform.rotozoom(tori_img,1,1.0),
                 pg.transform.rotozoom(tori_img,2,1.0),
                 pg.transform.rotozoom(tori_img,3,1.0),
                 pg.transform.rotozoom(tori_img,4,1.0),
                 pg.transform.rotozoom(tori_img,5,1.0),
                 pg.transform.rotozoom(tori_img,6,1.0),
                 pg.transform.rotozoom(tori_img,7,1.0),
                 pg.transform.rotozoom(tori_img,8,1.0),
                 pg.transform.rotozoom(tori_img,9,1.0),
                 pg.transform.rotozoom(tori_img,10,1.0),
                 pg.transform.rotozoom(tori_img,9,1.0),
                 pg.transform.rotozoom(tori_img,8,1.0),
                 pg.transform.rotozoom(tori_img,7,1.0),
                 pg.transform.rotozoom(tori_img,6,1.0),
                 pg.transform.rotozoom(tori_img,5,1.0),
                 pg.transform.rotozoom(tori_img,4,1.0),
                 pg.transform.rotozoom(tori_img,3,1.0),
                 pg.transform.rotozoom(tori_img,2,1.0),
                 pg.transform.rotozoom(tori_img,1,1.0)]#練習3:surface

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%4800
        screen.blit(bg_img, [-x, 0])#練習4:背景画像の表示
        screen.blit(bg2_img,[1600-x,0])#練習S6:動く背景画像
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(bg2_img, [4800-x, 0])
        screen.blit(tori_imgs[tmr%20],[300,200])#練習5:こうかとんが動く
        pg.display.update()
        tmr += 1        
        clock.tick(80)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()