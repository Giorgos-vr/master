import pygame
import math
import os


width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Orbital Resonance")
FPS = 30
sun = pygame.image.load(os.path.join("assets", "sun.png"))
sun_image = pygame.transform.scale(sun, (50, 50))
planet1 = pygame.image.load(os.path.join("assets", "planet1.png"))
planet1_image = pygame.transform.scale(planet1, (30, 30))
planet2 = pygame.image.load(os.path.join("assets", "planet2.png"))
planet2_image = pygame.transform.scale(planet2, (30, 30))
planet3 = pygame.image.load(os.path.join("assets", "planet3.png"))
planet3_image = pygame.transform.scale(planet3, (34, 27))
planet4 = pygame.image.load(os.path.join("assets", "planet4.png"))
planet4_image = pygame.transform.scale(planet4, (35, 35))


def draw_window():
    orbit1 = pygame.draw.circle(win, (247, 12, 36), (605, 337), 60, 2)
    orbit2 = pygame.draw.circle(win, (12, 224, 247), (605, 337), 142, 2)
    orbit3 = pygame.draw.circle(win, (247, 224, 12), (605, 337), 254, 2)
    orbit4 = pygame.draw.circle(win, (12, 247, 32), (605, 337), 395, 2)
    win.blit(sun_image, (580, 312))
    win.blit(planet1_image, (650, 320))
    win.blit(planet2_image, (730, 320))
    win.blit(planet3_image, (840, 320))
    win.blit(planet4_image, (980, 320))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
