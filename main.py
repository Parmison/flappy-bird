import pygame
pygame.init()

screen = pygame.display.set_mode((864,700))
bg = pygame.image.load("lesson 7/images/bg.png")
grass = pygame.image.load("lesson 7/images/ground.png")
flappy1 = pygame.image.load("lesson 7/images/flappy1.png")
flappy2 = pygame.image.load("lesson 7/images/flappy2.png")
flappy3 = pygame.image.load("lesson 7/images/flappy3.png")


grass_x = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [flappy1,flappy2,flappy3]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
    def update(self):
        self.counter += 1
        if self.counter >= 5:
            self.counter = 0
            self.index += 1
            if self.index >= 3:
                self.index = 0
        self.image = self.images[self.index]

flappy = Bird(50,300)
Flappy1 = pygame.sprite.Group()
Flappy1.add(flappy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("black")
    screen.blit(bg,(0,0))
    screen.blit(grass,(grass_x,600))
    grass_x -= 0.3
    if abs(grass_x) >30:
        grass_x = 0
    Flappy1.draw(screen)
    Flappy1.update()
    pygame.display.update()