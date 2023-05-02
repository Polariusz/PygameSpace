import pygame


class Star:
    def __init__(self, pos, radius, mass, colour):
        self.pos = pos
        self.true_pos = pos
        self.radius = radius
        self.mass = mass
        self.colour = colour

    def change_rel_pos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw_me(self, s):
        pygame.draw.circle(s, self.colour, self.pos, self.radius, width=self.radius - 1)
        pygame.draw.rect(s, self.colour, (self.pos[0] - 1, self.pos[1] - 1, 2, 2))
        # This stupid trick with width being smaller than radius by 1 and drawing rectangle to replace missing pixels
        # completely removes a bug that was drawing a bar that had same height as the radius when the circle was at
        # -1 x position
        self.draw_me_when_outside_of_window(s)

    def draw_me_when_outside_of_window(self, s):

        if self.pos[1] < 120-20 - self.radius and self.pos[0] < 100-20-self.radius:
            pygame.draw.circle(s, self.colour, (0, 20), 10)

        elif self.pos[1] < 120-20 - self.radius and self.pos[0] > 900+20 + self.radius:
            pygame.draw.circle(s, self.colour, (1000, 20), 10)

        elif self.pos[1] > 900+20 + self.radius and self.pos[0] < 100-20 - self.radius:
            pygame.draw.circle(s, self.colour, (0, 1000), 10)

        elif self.pos[1] > 900+20 + self.radius and self.pos[0] > 900+20 + self.radius:
            pygame.draw.circle(s, self.colour, (1000, 1000), 10)

        elif self.pos[1] < 20-self.radius:
            pygame.draw.circle(s, self.colour, (self.pos[0], 20), 10)

        elif self.pos[1] > 1000+self.radius:
            pygame.draw.circle(s, self.colour, (self.pos[0], 1000), 10)

        elif self.pos[0] < 0-self.radius:
            pygame.draw.circle(s, self.colour, (0, self.pos[1]), 10)

        elif self.pos[0] > 1000+self.radius:
            pygame.draw.circle(s, self.colour, (1000, self.pos[1]), 10)
