import pygame
import random
import math

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Orbital Resonance Cosmic Sounds (sounds coming soon)")

white = (255, 255, 255)
red = (247, 12, 36)
blue = (26, 9, 181)
light_blue = (12, 224, 247)
yellow = (247, 224, 12)
green = (12, 247, 32)
pink = (235, 63, 226)
orange = (235, 158, 63)
cyan = (52, 235, 204)
black = (0, 0, 0)

star_radius = 30
center = (640, 360)
defaultX = 640
defaultY = 360


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
size3 = 9
distance4 = 325
planet4_orbit = 0
angle4_inc = .01
size4 = 14
sat_dist1 = 30
sat_orb1 = 0
sat_angle_inc1 = .06
sat_size1 = 2
sat_dist2 = 60
sat_orb2 = 0
sat_angle_inc2 = .03
sat_size2 = 5
sat_dist3 = 22
sat_orb3 = 0
sat_angle_inc3 = .12
sat_size3 = 4
sat_dist4 = 45
sat_orb4 = 0
sat_angle_inc4 = .08
sat_size4 = 3


class PlanetMove:
    def planetX(planet_orbit, distance, X):
        x = math.cos(planet_orbit) * distance + X
        return x

    def planetY(planet_orbit, distance, Y):
        y = -math.sin(planet_orbit) * distance + Y
        return y
    

stars = [(random.randint(0, 1279), random.randint(0, 719)) for x in range(140)]
clock = pygame.time.Clock()
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    X1 = PlanetMove.planetX(planet1_orbit, distance1, defaultX)
    Y1 = PlanetMove.planetY(planet1_orbit, distance1, defaultY)
    planet1_orbit += angle1_inc
    X2 = PlanetMove.planetX(planet2_orbit, distance2, defaultX)
    Y2 = PlanetMove.planetY(planet2_orbit, distance2, defaultY)
    planet2_orbit += angle2_inc
    X3 = PlanetMove.planetX(planet3_orbit, distance3, defaultX)
    Y3 = PlanetMove.planetY(planet3_orbit, distance3, defaultY)
    planet3_orbit += angle3_inc
    X4 = PlanetMove.planetX(planet4_orbit, distance4, defaultX)
    Y4 = PlanetMove.planetY(planet4_orbit, distance4, defaultY)
    planet4_orbit += angle4_inc
    sat_X1 = PlanetMove.planetX(sat_orb1, sat_dist1, X4)
    sat_Y1 = PlanetMove.planetY(sat_orb1, sat_dist1, Y4)
    sat_orb1 += sat_angle_inc1
    sat_X2 = PlanetMove.planetX(sat_orb2, sat_dist2, X4)
    sat_Y2 = PlanetMove.planetY(sat_orb2, sat_dist2, Y4)
    sat_orb2 += sat_angle_inc2
    sat_X3 = PlanetMove.planetX(sat_orb3, sat_dist3, X3)
    sat_Y3 = PlanetMove.planetY(sat_orb3, sat_dist3, Y3)
    sat_orb3 += sat_angle_inc3
    sat_X4 = PlanetMove.planetX(sat_orb4, sat_dist4, X3)
    sat_Y4 = PlanetMove.planetY(sat_orb4, sat_dist4, Y3)
    sat_orb4 += sat_angle_inc4


    screen.fill(black)

    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, white, (x, y), (x, y))

    pygame.draw.circle(screen, yellow, center, star_radius)
    pygame.draw.circle(screen, red, (X1, Y1), size1)
    pygame.draw.circle(screen, green, (X2, Y2), size2)
    pygame.draw.circle(screen, white, (X3, Y3), size3)
    pygame.draw.circle(screen, blue, (X4, Y4), size4)
    pygame.draw.circle(screen, pink, (sat_X1, sat_Y1), sat_size1)
    pygame.draw.circle(screen, orange, (sat_X2, sat_Y2), sat_size2)
    pygame.draw.circle(screen, cyan, (sat_X3, sat_Y3), sat_size3)
    pygame.draw.circle(screen, light_blue, (sat_X4, sat_Y4), sat_size4)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
