import pygame

from game_sprite import GameSprite

# create background pic
pygame.init()
screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/xingyun1.jpg")
screen.blit(bg, (0, 0))
# create my air
hreo = pygame.image.load("./images/hero0.png")
screen.blit(hreo, (150, 500))
# create Enemy air
enemy = GameSprite("./images/enemy2.png")
enemy1 = GameSprite("./images/enemy2.png", 4)
enemyGroup = pygame.sprite.Group(enemy, enemy1)

clock = pygame.time.Clock()
plane_init_place = pygame.Rect(150, 300, 102, 126)
while True:
    # 用于指定循环体内的代码执行次数,即帧数
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print("Quit-------------------------------------")
            pygame.quit()
            exit()
    # update air's place
    plane_init_place.y -= 5
    if plane_init_place.y <= 0:
        plane_init_place.y = 700
    # 重新绘制背景
    screen.blit(bg, (0, 0))
    # 绘制图像
    screen.blit(hreo, plane_init_place)
    enemyGroup.update()
    enemyGroup.draw(screen)
    # 刷新图像
    pygame.display.update()

pygame.quit()