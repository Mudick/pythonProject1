from pygame import *
window = display.set_mode((800,600))
display.set_caption('Enter_Sandman')
background = transform.scale(image.load('i_4r315.jpg'),(800,600))
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
        if key_pressed[K_w] and self.rect.y > 10:
           self.rect.y  -= 10
        if key_pressed[K_y] and self.rect.y < 800:
            self.rect.y  += 10
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 10:
           self.rect.y  -= 10
        if key_pressed[K_DOWN] and self.rect.y < 800:
            self.rect.y  += 10
game = True
p1 = Player('Rectangle 1.png',50,150,50)
p2 = Player('Frame 1.png',50,150,50)

while game:

    window.blit(background, (0, 0))
    p1.reset()
    p1.update_r()
    p2.reset()
    p2.update_l()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()