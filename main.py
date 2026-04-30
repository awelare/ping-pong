from pygame import *
from settings import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, image_path, w, h, speed=4):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(image_path), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keyP = key.get_pressed()
        if keyP[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keyP[K_DOWN] and self.rect.y < ssY-40:
            self.rect.y += self.speed
class Player2(GameSprite):
    def move(self):
        keyP = key.get_pressed()
        if keyP[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keyP[K_s] and self.rect.y < ssY-100:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, x, y, image_path, speedx, speedy, w, h):
        super().__init__(x, y, image_path, w, h)
        self.speedx = speedx
        self.speedy = speedy

    def move(self, pl_1, pl_2):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if sprite.collide_rect(pl_1, self) or sprite.collide_rect(pl_2, self):
            self.speedx *= -1
        if self.rect.y > ssY - self.rect.height or self.rect.y < 0:
            self.speedy *= -1
        if self.rect.x > ssX or self.rect.x < 0:
            return True
        return False


window = display.set_mode((ssX, ssY))
display.set_caption('Пинг понг')
bg = window.fill(bgCol)

pl1 = Player(pl1x, pl1y, 'платформа.png', plx, ply)
pl2 = Player2(pl2x, pl2y, 'платформа.png', plx, ply)
ball = Ball(int(ssX/2), int(ssY/2), image_path='ball.png', speedx=randint(3, 7), speedy=randint(3, 7), w=ballx, h=bally)

clock = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(bgCol)
    pl1.reset()
    pl1.move()
    pl2.reset()
    pl2.move()
    ball.reset()
    if ball.move(pl1, pl2):
        game = False
    display.update()
    clock.tick(FPS)
