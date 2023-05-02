import math
import pygame
from math import sqrt


class Moon:
    G = (6.674 * 10 ** (-11))

    def __init__(self, pos, radius, mass, colour, name):
        self.pos = pos
        self.true_pos = pos
        self.radius = radius
        self.mass = mass
        self.colour = colour
        self.name = name
        self.main_planet_true_pos = [0, 0]

        self.starting_pos = [0, 0, False]
        self.planet = None
        self.scalar = 0
        self.angle = 0
        self.x = 0
        self.y = 0

    def main_planet(self, planet):
        self.planet = planet
        self.pos[0] = self.pos[0] + self.planet.pos[0]
        self.pos[1] = self.pos[1] + self.planet.pos[1]

    def update_main_planet_true_pos(self):
        self.main_planet_true_pos = [(self.planet.true_pos[0] - self.planet.previous_pos[0]),
                                     (self.planet.true_pos[1] - self.planet.previous_pos[1])]

    def move(self, paused):
        self.pos[0] += self.main_planet_true_pos[0]
        self.pos[1] += self.main_planet_true_pos[1]
        self.true_pos = [(self.pos[0] - self.planet.true_pos[0]) * math.cos(.1*self.angle*self.scalar) +
                         self.planet.true_pos[0],
                         (self.pos[1] - self.planet.true_pos[1]) * math.sin(.1*self.angle*self.scalar) +
                         self.planet.true_pos[1]]
        if self.starting_pos[2] is False:
            self.starting_pos[0] = self.true_pos[0]
            self.starting_pos[1] = self.true_pos[1]
            self.starting_pos[2] = True
        self.starting_pos[0] += self.main_planet_true_pos[0]
        self.starting_pos[1] += self.main_planet_true_pos[1]
        if paused is False:
            self.angle += 2
        if self.angle > 1000:
            if 0.9999 < math.cos(.1 * self.scalar * self.angle) < 1.0001:
                self.angle = 0
                print("{} has successfully orbited the planet!".format(self.name))

    def gravity_to_planet(self):
        self.scalar = (self.mass * self.planet.mass * 1/750)/sqrt((self.true_pos[0] - self.planet.true_pos[0]) ** 2 +
                                                                  (self.true_pos[1] - self.planet.true_pos[1]) ** 2)

    def change_rel_pos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw_me(self, s):
        pygame.draw.circle(s, self.colour, self.true_pos, self.radius, width=self.radius - 1)
        pygame.draw.rect(s, self.colour, (self.true_pos[0] - 1, self.true_pos[1] - 1, 2, 2))

    def draw_my_orbit(self, s):
        temp_pos = ((self.planet.true_pos[0] - (self.pos[0] - self.planet.true_pos[0])),
                    (self.planet.true_pos[1] - (self.pos[1] - self.planet.true_pos[1])))
        temp_radius = (2 * (self.pos[0] - self.planet.true_pos[0]), 2 * (self.pos[1] - self.planet.true_pos[1]))
        temp_rect = (temp_pos, temp_radius)
        pygame.draw.ellipse(s, '#ffffff', temp_rect, width=1)
