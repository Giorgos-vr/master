# import libraries

import pygame
from pygame import mixer
import random
import math

pygame.init()
pygame.mixer.init()
# setup screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Orbital Resonance Cosmic Sounds (sounds coming soon)")

# colour variables
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

# star basic parameters, default X,Y used for object position calculation, super important, do not change!
star_radius = 30
center = (640, 360)
defaultX = 640
defaultY = 360

# object basic parameters, angle_inc defines rotation speed
# angle change per frame, the lower the value=the slower the rotation speed relative to orbit radius
distance1 = 75
planet1_orbit = 0
angle1_inc = .08
size1 = 6
planet1_sound = mixer.Sound('f-major-3rd.wav')
distance2 = 125
planet2_orbit = 0
angle2_inc = .04
size2 = 10
planet2_sound = mixer.Sound('f-minor-3rd.wav')
distance3 = 225
planet3_orbit = 0
angle3_inc = .02
size3 = 9
planet3_sound = mixer.Sound('f-minor-4th.wav')
distance4 = 325
planet4_orbit = 0
angle4_inc = .01
size4 = 14
planet4_sound = mixer.Sound('f-major-4th.wav')
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

# background stars and clock variable
stars = [(random.randint(0, 1279), random.randint(0, 719)) for x in range(140)]
clock = pygame.time.Clock()

# heart of the beast, X and Y are a function of distance (orbit radius) + X or Y
# where X and Y are either the default (central) X and Y for planets or the parent planet's X and Y for satellites


class PlanetMove:
    def planetX(planet_orbit, distance, X):
        # changing this to a negative value will move the starting point
        # to the left instead of the right where it is at the moment
        x = math.cos(planet_orbit) * distance + X
        return x

    def planetY(planet_orbit, distance, Y):
        # changing this to a positive value (removing the minus sign) will change the output to a clockwise rotation
        # instead of the counter-clockwise rotation we are currently implementing
        y = -math.sin(planet_orbit) * distance + Y
        return y

    def tone(sound):
        sound.play(0)


run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # coordinates calculations
    X1 = PlanetMove.planetX(planet1_orbit, distance1, defaultX)
    Y1 = PlanetMove.planetY(planet1_orbit, distance1, defaultY)
    if pygame.Rect(710, 355, 10, 10).collidepoint(X1, Y1):
        PlanetMove.tone(planet1_sound)
    # changing the angle is what makes it move
    planet1_orbit += angle1_inc
    X2 = PlanetMove.planetX(planet2_orbit, distance2, defaultX)
    Y2 = PlanetMove.planetY(planet2_orbit, distance2, defaultY)
    if pygame.Rect(760, 355, 10, 10).collidepoint(X2, Y2):
        PlanetMove.tone(planet2_sound)
    planet2_orbit += angle2_inc
    X3 = PlanetMove.planetX(planet3_orbit, distance3, defaultX)
    Y3 = PlanetMove.planetY(planet3_orbit, distance3, defaultY)
    if pygame.Rect(860, 355, 10, 10).collidepoint(X3, Y3):
        PlanetMove.tone(planet3_sound)
    planet3_orbit += angle3_inc
    X4 = PlanetMove.planetX(planet4_orbit, distance4, defaultX)
    Y4 = PlanetMove.planetY(planet4_orbit, distance4, defaultY)
    if pygame.Rect(960, 355, 10, 10).collidepoint(X4, Y4):
        PlanetMove.tone(planet4_sound)
    planet4_orbit += angle4_inc

    # here we assign X4 and Y4 instead of the default ones in order
    # to assign object to planet 4 as a satellite instead of assigning it to the central star as yet another planet
    sat_X1 = PlanetMove.planetX(sat_orb1, sat_dist1, X4)
    sat_Y1 = PlanetMove.planetY(sat_orb1, sat_dist1, Y4)
    sat_orb1 += sat_angle_inc1
    sat_X2 = PlanetMove.planetX(sat_orb2, sat_dist2, X4)
    sat_Y2 = PlanetMove.planetY(sat_orb2, sat_dist2, Y4)
    sat_orb2 += sat_angle_inc2

    # same for the satellites of planet 3
    sat_X3 = PlanetMove.planetX(sat_orb3, sat_dist3, X3)
    sat_Y3 = PlanetMove.planetY(sat_orb3, sat_dist3, Y3)
    sat_orb3 += sat_angle_inc3
    sat_X4 = PlanetMove.planetX(sat_orb4, sat_dist4, X3)
    sat_Y4 = PlanetMove.planetY(sat_orb4, sat_dist4, Y3)
    sat_orb4 += sat_angle_inc4

    # here we start drawing by first resetting the screen to black
    screen.fill(black)

    # then we add the stars
    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, white, (x, y), (x, y))

    # and then we add everything else starting with our stationary central star
    pygame.draw.circle(screen, yellow, center, star_radius)
    pygame.draw.circle(screen, red, (X1, Y1), size1)
    pygame.draw.circle(screen, green, (X2, Y2), size2)
    pygame.draw.circle(screen, white, (X3, Y3), size3)
    pygame.draw.circle(screen, blue, (X4, Y4), size4)
    pygame.draw.circle(screen, pink, (sat_X1, sat_Y1), sat_size1)
    pygame.draw.circle(screen, orange, (sat_X2, sat_Y2), sat_size2)
    pygame.draw.circle(screen, cyan, (sat_X3, sat_Y3), sat_size3)
    pygame.draw.circle(screen, light_blue, (sat_X4, sat_Y4), sat_size4)

    # flip, tick, repeat!
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
