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


distance1 = 75
planet1_orbit = 0
angle1_inc = .08
size1 = 6
distance2 = 125
planet2_orbit = 0
angle2_inc = .04
size2 = 10
distance3 = 225
planet3_orbit = 0
angle3_inc = .02
size3 = 8
distance4 = 325
planet4_orbit = 0
angle4_inc = .01
size4 = 12
sat_dist1 = 25
sat_orb1 = 0
sat_angle_inc1 = .06
sat_size1 = 2
sat_dist2 = 50
sat_orb2 = 0
sat_angle_inc2 = .03
sat_size2 = 5


class PlanetMove:
    def planet_coors(planet_orbit, distance):

        planet_x = math.cos(planet_orbit) * distance + 640
        planet_y = -math.sin(planet_orbit) * distance + 360
        return planet_x, planet_y
    

stars = [(random.randint(0, 1279), random.randint(0, 719)) for x in range(140)]
clock = pygame.time.Clock()
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    PlanetMove.planet_coors(planet1_orbit, distance1)
    planet1_orbit += angle1_inc
    PlanetMove.planet_coors(planet2_orbit, distance2)
    planet2_orbit += angle2_inc
    PlanetMove.planet_coors(planet3_orbit, distance3)
    planet3_orbit += angle3_inc
    PlanetMove.planet_coors(planet4_orbit, distance4)
    planet4_orbit += angle4_inc


    screen.fill(black)

    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, white, (x, y), (x, y))

    pygame.draw.circle(screen, white, center, star_radius)
    pygame.draw.circle(screen, yellow, (PlanetMove.planet_coors(planet1_orbit, distance1)), size1)
    pygame.draw.circle(screen, blue, (PlanetMove.planet_coors(planet2_orbit, distance2)), size2)
    pygame.draw.circle(screen, red, (PlanetMove.planet_coors(planet3_orbit, distance3)), size3)
    pygame.draw.circle(screen, green, (PlanetMove.planet_coors(planet4_orbit, distance4)), size4)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
