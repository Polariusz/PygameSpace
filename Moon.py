import math
import pygame
from math import sqrt
from ResourceList import RockFiniteResources


class Moon:
    G = (6.674 * 10 ** (-11))

    def __init__(self, pos, radius, mass, colour, name, habitability, colonised):
        self.pos = pos
        self.true_pos = pos
        self.radius = radius
        self.mass = mass
        self.colour = colour
        self.name = name
        self.main_planet_true_pos = [0, 0]
        self.habitability = habitability
        self.colonised = colonised

        self.selected = False
        self.starting_pos = [0, 0, False]
        self.planet = None
        self.scalar = 0
        self.angle = 0
        self.x = 0
        self.y = 0

        self.stored_resources = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0, 0, 0, 0],
                                 [0, 0, 0]]
        self.produced_resources = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0]]
        self.finite_resources = None

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

    def gravity_to_planet(self):
        self.scalar = (self.mass * self.planet.mass * 1/750)/sqrt((self.true_pos[0] - self.planet.true_pos[0]) ** 2 +
                                                                  (self.true_pos[1] - self.planet.true_pos[1]) ** 2)

    def change_rel_pos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw_me(self, s):
        pygame.draw.circle(s, self.colour, self.true_pos, self.radius, width=self.radius - 1)
        pygame.draw.rect(s, self.colour, (self.true_pos[0] - 1, self.true_pos[1] - 1, 2, 2))

        if self.selected is True:
            pygame.draw.circle(s, 'white', self.true_pos, self.radius + 10, width=5)

    def draw_my_orbit(self, s):
        temp_pos = ((self.planet.true_pos[0] - (self.pos[0] - self.planet.true_pos[0])),
                    (self.planet.true_pos[1] - (self.pos[1] - self.planet.true_pos[1])))
        temp_radius = (2 * (self.pos[0] - self.planet.true_pos[0]), 2 * (self.pos[1] - self.planet.true_pos[1]))
        temp_rect = (temp_pos, temp_radius)
        pygame.draw.ellipse(s, '#ffffff', temp_rect, width=1)

    def select_it(self):
        self.selected = True

    def unselect_it(self):
        self.selected = False

    def get_name(self):
        return self.name

    def set_finite_resources(self, raw_metal, uranium, limestone, granite, liquid_fossil, solid_fossil, water):
        self.finite_resources = RockFiniteResources(raw_metal=raw_metal, uranium=uranium, limestone=limestone,
                                                    granite=granite, liquid_fossil=liquid_fossil,
                                                    solid_fossil=solid_fossil, water=water)

    def update_stored_resources(self):
        for zero in range(len(self.stored_resources[0])):
            self.stored_resources[0][zero] = self.stored_resources[0][zero] + self.produced_resources[0][zero]

        for one in range(len(self.stored_resources[1])):
            self.stored_resources[1][one] = self.stored_resources[1][one] + self.produced_resources[1][one]

        for two in range(len(self.stored_resources[2])):
            self.stored_resources[2][two] = self.stored_resources[2][two] + self.produced_resources[2][two]

        for three in range(len(self.stored_resources[3])):
            self.stored_resources[3][three] = self.stored_resources[3][three] + self.produced_resources[3][three]

        for four in range(len(self.stored_resources[4])):
            self.stored_resources[4][four] = self.stored_resources[4][four] + self.produced_resources[4][four]

        for five in range(len(self.stored_resources[5])):
            self.stored_resources[5][five] = self.stored_resources[5][five] + self.produced_resources[5][five]
