from math import sqrt
from pygame import Rect


class Rock:
    def __init__(self, x_pos, y_pos, radius, mass, colour, array):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.mass = mass
        self.colour = colour
        self.vector = [0, 0]
        self.scalar = 0
        self.array = array
        self.x_vel = 0
        self.y_vel = 0
        self.x_tan = None
        self.y_tan = None
        self.x_acc = 0
        self.y_acc = 0

        self.rect = Rect(x_pos, y_pos, radius, radius)

    def stop(self):
        self.x_vel = 0
        self.y_vel = 0

    def add_x_pos(self, x):
        self.x_acc += x

    def add_y_pos(self, y):
        self.y_acc += y

    def change_x_pos(self, x):
        self.x_pos = x

    def change_y_pos(self, y):
        self.y_pos = y

    def change_width(self, r):
        self.radius = r

    def update_rect(self):
        self.rect.update(self.x_pos, self.y_pos, self.radius, self.radius)

    def gravity_relative_to_other_rocks(self):
        for i in range(len(self.array.array)):
            if self.array.array[i] is not self:
                self.scalar = self.array.array[i].mass / sqrt(((self.x_pos - self.array.array[i].x_pos)**2 +
                                                                  (self.y_pos - self.array.array[i].y_pos)**2)*1)

    def vector_relative_to_other_rocks(self):
        for i in range(len(self.array.array)):
            if self.array.array[i] is not self:
                self.vector[0] = self.array.array[i].x_pos - self.x_pos
                self.vector[1] = self.array.array[i].y_pos - self.y_pos

    def move(self):
        self.x_pos += self.scalar * self.vector[0]
        self.y_pos += self.scalar * self.vector[1]

    def set_tangent(self):
        for i in range(len(self.array.array)):
            if self.array.array[i] is not self:
                self.x_tan = self.vector[1] * -1
                self.y_tan = self.vector[0]

    def move_tangential(self):
        self.x_pos += (self.x_acc/10)*self.scalar * self.x_tan
        self.y_pos += (self.y_acc/10)*self.scalar * self.y_tan
