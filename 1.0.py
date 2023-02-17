import pygame
import random
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_SPEED = 5
POLICE_SPEED = 4
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Police")
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
class Police(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = POLICE_SPEED
        self.player = player

    def update(self):
        if self.rect.y < self.player.rect.y:
            self.rect.y += self.speed
        if self.rect.x < self.player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > self.player.rect.x:
            self.rect.x -= self.speed
all_sprites = pygame.sprite.Group()
police_group = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(3):
    police = Police(player)
    all_sprites.add(police)
    police_group.add(police)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, police_group, False)
    if hits:
        running = False

    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
