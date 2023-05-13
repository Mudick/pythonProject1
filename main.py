import pygame
from pygame import *
clock = pygame.time.Clock()
window = display.set_mode((800,600))
display.set_caption('Enter_Sandman')
background = transform.scale(image.load('i_4r315.jpg'),(800,600))
speed_x = 5
speed_y = 5
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 8:
           self.rect.y  -= 8
        if key_pressed[K_s] and self.rect.y < 800:
            self.rect.y  += 8
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 8:
           self.rect.y  -= 8
        if key_pressed[K_DOWN] and self.rect.y < 800:
            self.rect.y  += 8
game = True
p2 = Player('Rectangle 1.png',50,150,50)
p1 = Player('Frame 1.png',700,150,50)
ball = Player('Star 1.png',400,300,100)
finish = False
FPS = 40
while game:

    window.blit(background, (0, 0))
    p1.reset()
    p1.update_r()
    p2.reset()
    p2.update_l()
    ball.reset()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
    if ball.rect.y > 600-50 or ball.rect.y < 0:
            speed_y *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()