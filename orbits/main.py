import pygame
import os


width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Orbital Resonance V0.1")



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
