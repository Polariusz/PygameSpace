import pygame


class Window:

    def __init__(self, pos, size, origin, name):
        self.pos = pos
        self.size = size
        self.origin = origin
        self.name = name

        self.changing_name = False
        self.rect_exit_button = []
        self.rect_title_bar = []
        self.rect_rename = []
        self.delete_me = False
        self.holds_the_bar = False
        self.clicked_me = False
        self.current_text_colour = '#000000'

    def draw_me(self, s):
        pygame.draw.rect(s, '#7777ff', (self.pos, self.size))   # Window itself
        self.rect_title_bar = pygame.Rect(self.pos, (self.size[0] - 20, 20))
        pygame.draw.rect(s, '#ffffff', self.rect_title_bar)  # title bar
        self.rect_exit_button = pygame.Rect((self.pos[0] + self.size[0] - 20), self.pos[1], 20, 20)
        pygame.draw.rect(s, '#ff0000', self.rect_exit_button)  # exit button
        self.rect_rename = pygame.Rect(self.pos, (20, 20))
        pygame.draw.rect(s, "#00ff00", self.rect_rename)  # rename rectangle

        pygame.draw.rect(s, '#5555ff', ((self.pos[0] + 5, self.pos[1] + 25), (self.size[0] - 10, 20)))

        pygame.draw.rect(s, '#888888', (self.pos, self.size), width=2)  # frame
        font = pygame.font.SysFont(None, 24)
        img = font.render("Window of " + self.name, True, self.current_text_colour)  # name
        s.blit(img, (self.pos[0]+23, self.pos[1]+3))

        img = font.render("Size: " + str(self.origin.radius), True, 'black')
        s.blit(img, (self.pos[0] + 8, self.pos[1]+28))
        size_of_planet_size = img.get_size()

        img = font.render("Habitability: " + str(self.origin.habitability) + "%", True, 'black')
        s.blit(img, (self.pos[0] + size_of_planet_size[0] + 20, self.pos[1] + 28))

    def update_pos(self, new_pos):
        self.pos = new_pos

    def update_size(self, new_size):
        self.size = new_size

    def get_name(self):
        return self.name

    def clicked(self, mouse_pos, mouse_rel_pos):
        if self.rect_exit_button.collidepoint(mouse_pos) and self.holds_the_bar is False:
            self.clicked_close()
        elif self.rect_rename.collidepoint(mouse_pos) and self.holds_the_bar is False:
            self.changing_name = True
            self.current_text_colour = '#444444'
        elif self.rect_title_bar.collidepoint(mouse_pos) or self.holds_the_bar:
            self.holds_the_bar = True
            self.clicked_title_bar(mouse_rel_pos)

    def clicked_close(self):
        self.delete_me = True

    def clicked_title_bar(self, mrp):
        temp_new_pos_x = self.pos[0] + mrp[0]
        temp_new_pos_y = self.pos[1] + mrp[1]
        temp_new_pos = [temp_new_pos_x, temp_new_pos_y]
        self.update_pos(temp_new_pos)

    def get_holds_the_bar(self):
        return self.holds_the_bar

    def change_name(self, n):
        if self.changing_name is True:
            self.name = n
