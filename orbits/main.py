import pygame
import random
import math

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Orbital Resonance Cosmic Sounds")

white = (255, 255, 255)
red = (247, 12, 36)
blue = (12, 224, 247)
yellow = (247, 224, 12)
green = (12, 247, 32)
grey = (200, 200, 200)
black = (0, 0, 0)

star_radius = 30
center = (640, 360)

planet1_x = 0
planet1_y = 0
planet2_x = 0
planet2_y = 0
planet3_x = 0
planet3_y = 0
planet4_x = 0
planet4_y = 0

planet1_orbit = 0
planet2_orbit = 0
planet3_orbit = 0
planet4_orbit = 0
sat1_orbit = 0
sat2_orbit = 0

stars = [(random.randint(0, 1279), random.randint(0, 719)) for x in range(140)]
clock = pygame.time.Clock()
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    planet1_x = math.cos(planet1_orbit) * 75 + 640
    planet1_y = -math.sin(planet1_orbit) * 75 + 360
    planet2_x = math.cos(planet2_orbit) * 125 + 640
    planet2_y = -math.sin(planet2_orbit) * 125 + 360
    planet3_x = math.cos(planet3_orbit) * 200 + 640
    planet3_y = -math.sin(planet3_orbit) * 200 + 360
    planet4_x = math.cos(planet4_orbit) * 275 + 640
    planet4_y = -math.sin(planet4_orbit) * 275 + 360
    sat1_x = math.cos(sat1_orbit) * 25 + planet4_x
    sat1_y = -math.sin(sat1_orbit) * 25 + planet4_y
    sat2_x = math.cos(sat2_orbit) * 50 + planet4_x
    sat2_y = -math.sin(sat2_orbit) * 50 + planet4_y

    planet1_orbit += .08
    planet2_orbit += .04
    planet3_orbit += .02
    planet4_orbit += .01
    sat1_orbit += .06
    sat2_orbit += .03

    screen.fill(black)

    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, white, (x, y), (x, y))

    pygame.draw.circle(screen, white, center, star_radius)

    pygame.draw.circle(screen, blue, (int(planet1_x), int(planet1_y)), 7)
    pygame.draw.circle(screen, red, (int(planet2_x), int(planet2_y)), 10)
    pygame.draw.circle(screen, green, (int(planet3_x), int(planet3_y)), 7)
    pygame.draw.circle(screen, yellow, (int(planet4_x), int(planet4_y)), 12)
    pygame.draw.circle(screen, grey, (int(sat1_x), int(sat1_y)), 3)
    pygame.draw.circle(screen, grey, (int(sat2_x), int(sat2_y)), 4)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
