import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1:背景画像surfaceの生成
    tori_img = pg.image.load("ex01/fig/3.png")#練習2:こうかとん画像surfaceの生成
    tori_img = pg.transform.flip(tori_img,True,False)#練習2:こうかとんの反転
    tori_imgs = [tori_img,pg.transform.rotozoom(tori_img,10,1.0)]#練習3:回転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#練習4:背景画像の表示
        screen.blit(tori_imgs[1],[200,200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()