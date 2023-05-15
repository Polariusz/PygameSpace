import math
import pygame
from math import sqrt

from ResourceList import BigRockResources


class Asteroid:
    G = (6.674 * 10 ** (-11))

    def __init__(self, pos, radius, mass, colour, name, habitability, x_deviation, y_deviation, set_angle, colonised):
        self.name = name
        self.pos = pos
        self.true_pos = self.pos
        self.radius = radius
        self.mass = mass
        self.colour = colour
        self.rectangle = ((self.true_pos[0] - self.radius, self.true_pos[1] - self.radius),
                          (self.radius * 2, self.radius * 2))
        self.x_deviation = x_deviation
        self.y_deviation = y_deviation
        self.habitability = habitability
        self.starting_angle = set_angle
        self.colonised = colonised

        self.starting_pos = [0, 0, False]
        self.resources = None
        self.previous_pos = [None, None]
        self.scalar = 0
        self.star = None
        self.selected = False
        self.angle = set_angle
        self.completed_orbital_cycle = False

    def main_star(self, star):
        self.star = star
        self.true_pos[0] = self.true_pos[0] + self.star.pos[0]
        self.true_pos[1] = self.true_pos[1] + self.star.pos[1]

    def move(self, paused):
        self.previous_pos = self.true_pos
        self.true_pos = [(self.pos[0] - self.star.pos[0]) * math.cos(.1 * self.angle * self.scalar) +
                         self.star.pos[0] + self.x_deviation,
                         (self.pos[1] - self.star.pos[1]) * math.sin(.1 * self.angle * self.scalar) +
                         self.star.pos[1] + self.y_deviation]
        if self.starting_pos[2] is False:
            self.starting_pos[0] = (self.true_pos[0] - self.star.pos[0]) * math.cos(0.1*0*self.scalar) + self.star.pos[0] + self.x_deviation
            self.starting_pos[1] = (self.true_pos[1] - self.star.pos[1]) * math.cos(0.1*0*self.scalar) + self.star.pos[1] + self.y_deviation
            self.starting_pos[2] = True
        if paused is False:
            self.angle += 2
        if self.angle > 1000:
            if 0.99999 < math.cos(.1 * self.scalar * self.angle) < 1.00001:
                self.angle = 0
                print("{} has successfully orbited the sun!".format(self.name))

    def gravity_to_star(self):
        self.scalar = sqrt(self.G * self.star.mass) / sqrt(((self.pos[0] - self.star.pos[0] - self.x_deviation) ** 2 +
                                                            (self.pos[1] - self.star.pos[1] - self.y_deviation) ** 2))

    def change_rel_pos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y
        self.true_pos[0] += x
        self.true_pos[1] += y
        self.starting_pos[0] += x
        self.starting_pos[1] += y

    def get_name(self):
        return self.name

    def select_it(self):
        self.selected = True

    def unselect_it(self):
        self.selected = False

    def draw_me(self, s):
        pygame.draw.circle(s, self.colour, self.true_pos, self.radius, width=self.radius - 1)
        pygame.draw.rect(s, self.colour, (self.true_pos[0] - 1, self.true_pos[1] - 1, 2, 2))
        # This stupid trick with width being smaller than radius by 1 and drawing rectangle to replace missing pixels
        # completely removes a bug that was drawing a bar that had same height as the radius when the circle was at
        # -1 x position

        if self.selected is True:
            pygame.draw.circle(s, 'white', self.true_pos, self.radius + 10, width=5)

    def draw_my_orbit(self, s):
        temp_pos = ((self.star.pos[0] - (self.pos[0] - self.star.pos[0]) + self.x_deviation),
                    (self.star.pos[1] - (self.pos[1] - self.star.pos[1]) + self.y_deviation))
        temp_radius = (2 * (self.pos[0] - self.star.pos[0]), 2 * (self.pos[1] - self.star.pos[1]))
        temp_rect = (temp_pos, temp_radius)
        pygame.draw.ellipse(s, '#ffffff', temp_rect, width=1)

    def create_resources(self, energy, minerals, metals, retail_goods, food, water, fossil_fuels, rare_elements,
                         chemicals, bio_resources, science, population, labour):
        self.resources = BigRockResources(
                    self.radius, energy, minerals, metals, retail_goods, food, water, fossil_fuels, rare_elements,
                    chemicals, bio_resources, science, population, labour)
