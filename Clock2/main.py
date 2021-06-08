import pygame
import os
from datetime import datetime

Width = 1000
Height = 1000
FPS = 60
White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (230, 230, 230)

pygame.init()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Best Clock")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Img')
back_ground = pygame.image.load(os.path.join(img_folder, 'NewClock_bg.png'))
back_ground.set_colorkey(White)
back_ground.set_colorkey(Grey)
new_back_ground = pygame.image.load(os.path.join(img_folder, 'NewVO.png'))
new_back_ground.set_colorkey(White)
new_back_ground.set_colorkey(Grey)
Sec = pygame.image.load(os.path.join(img_folder, 'sec.png'))
Sec.set_colorkey(White)
Min = pygame.image.load(os.path.join(img_folder, 'min.png'))
Min.set_colorkey(White)
Hour = pygame.image.load(os.path.join(img_folder, 'hour.png'))
Hour.set_colorkey(White)


def rotation(image, angle):
    rotation_image = pygame.transform.rotate(image, -angle)
    rotation_rect = rotation_image.get_rect(center=(500, 500))
    return screen.blit(rotation_image, rotation_rect)


run = True
while run:
    clock.tick(FPS)
    current_minute = datetime.now().minute
    current_hour = datetime.now().hour
    current_second = datetime.now().second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(White)
    if 30 <= current_second <= 59:
        screen.blit(new_back_ground, (131, 131))
    screen.blit(back_ground, (131, 131))

    Angle_Hour = current_hour * 30 + 0.5 * current_minute
    rotation(Hour, Angle_Hour)

    Angle_Minute = current_minute * 6
    rotation(Min, Angle_Minute)

    Angle_Second = current_second * 6
    rotation(Sec, Angle_Second)

    pygame.display.update()
