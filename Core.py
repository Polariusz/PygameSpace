from math import sqrt

import pygame
from pygame import Rect, K_BACKSPACE, K_RETURN

from Star import Star
from Planet import Planet
from Moon import Moon
from Asteroid import Asteroid
from ArrayList import PlanetList
from ArrayList import MoonList
from ArrayList import AsteroidList
from ArrayList import WindowList
from ArrayList import ButtonList

# classes


class Button:
    def __init__(self, pos, size, colour_calm, colour_clicked, name, image_calm, image_clicked):
        self.pos = pos
        self.size = size
        self.colour_calm = colour_calm
        self.colour_clicked = colour_clicked
        self.name = name
        self.image_calm = image_calm
        self.image_clicked = image_clicked
        self.current_image = image_calm[0]
        self.current_colour = self.colour_calm
        self.rectangle = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        self.clicked = False
        self.image_index = 0

    def mouse_clicked(self, event):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rectangle.collidepoint(x, y):
                # self.current_colour = self.colour_clicked
                self.current_image = self.image_clicked[self.image_index]
                self.clicked = True
            else:
                # self.current_colour = self.colour_calm
                pass

    def mouse_released(self):

        if self.clicked is True:
            self.clicked = False
            if self.name != "pause":
                self.current_image = self.image_calm[self.image_index]

            if self.name == 'pause':
                if self.image_index == 0:
                    self.image_index = 1
                elif self.image_index == 1:
                    self.image_index = 0
                self.current_image = self.image_calm[self.image_index]
            key_clicked(self.name)

    def show_button(self):
        # pygame.draw.rect(screen, self.current_colour, self.rectangle)
        screen.blit(self.current_image, self.pos)


# methods


def key_clicked(name):
    global button_pause_bool
    global button_plus_bool
    global button_minus_bool
    if name == 'pause' and button_pause_bool is False:
        button_pause_bool = True
    elif name == 'pause' and button_pause_bool is True:
        button_pause_bool = False
    if name == 'plus':
        button_plus_bool = True
        # button_plus.current_image = button_plus.image_clicked
    if name == 'minus':
        button_minus_bool = True
        # button_minus.current_image = button_minus.image_clicked


def distance_from_mouse_to_rocks():
    global mouse_pos
    global distances
    temp_distances = []
    for i in range(len(planets.array)):
        temp_distance = sqrt((mouse_pos[0] - planets.array[i].true_pos[0]) ** 2 +
                             (mouse_pos[1] - planets.array[i].true_pos[1]) ** 2)
        temp_distances.append(temp_distance)
    for j in range(len(moons.array)):
        temp_distance = sqrt((mouse_pos[0] - moons.array[j].true_pos[0]) ** 2 +
                             (mouse_pos[1] - moons.array[j].true_pos[1]) ** 2)
        temp_distances.append(temp_distance)
    for k in range(len(asteroids.array)):
        temp_distance = sqrt((mouse_pos[0] - asteroids.array[k].true_pos[0]) ** 2 +
                             (mouse_pos[1] - asteroids.array[k].true_pos[1]) ** 2)
        temp_distances.append(temp_distance)
    distances = temp_distances


def rock_clicked():
    global move_window
    flag_range_planet_index = None   # range_planet_index is saved here when the method wants to create a window.
    flag_to_make_a_window = True    # It is set to false when this method recognises that a window is already there.

    for delete in range(len(planets.array)):
        planets.array[delete].unselect_it()
    for delete_moon_select in range(len(moons.array)):
        moons.array[delete_moon_select].unselect_it()
    for delete_asteroid_select in range(len(asteroids.array)):
        asteroids.array[delete_asteroid_select].unselect_it()

    for range_planet_index in range(len(planets.array)):
        if planets.array[range_planet_index].radius > distances[range_planet_index]:
            # if planet radius is smaller than the one of the distance between mouse and a planet
            if range(len(windows.array)) == range(0, 0):
                flag_range_planet_index = range_planet_index  # if no window was created, set it to the planet index
            else:
                # If there is already a window, check if the user is clicking on a planet that already is showing a
                # window. If not, set the flag to planet's index. If true, then set the flag_to_make_a_window to False.
                for check_windows in range(len(windows.array)):
                    if planets.array[range_planet_index].name != windows.array[check_windows].name:
                        flag_range_planet_index = range_planet_index
                    else:
                        flag_to_make_a_window = False
            if flag_to_make_a_window:   # if flag is true, go to the create_window method to make one!
                create_window(flag_range_planet_index)

    for range_moon_index in range(len(moons.array)):
        if moons.array[range_moon_index].radius > distances[range_moon_index + len(planets.array)]:
            if range(len(windows.array)) == range(0, 0):
                flag_range_planet_index = range_moon_index + len(planets.array)
            else:
                for check_windows in range(len(windows.array)):
                    if moons.array[range_moon_index].name != windows.array[check_windows].name:
                        flag_range_planet_index = range_moon_index + len(planets.array)
                    else:
                        flag_to_make_a_window = False
            if flag_to_make_a_window:
                create_window(flag_range_planet_index)

    for range_asteroid_index in range(len(asteroids.array)):
        if moons.array[range_asteroid_index].radius > distances[range_asteroid_index + len(planets.array) + len(moons.array)]:
            if range(len(windows.array)) == range(0, 0):
                flag_range_planet_index = range_asteroid_index + len(planets.array) + len(moons.array)
            else:
                for check_windows in range(len(windows.array)):
                    if asteroids.array[range_asteroid_index].name != windows.array[check_windows].name:
                        flag_range_planet_index = range_asteroid_index + len(planets.array) + len(moons.array)
                    else:
                        flag_to_make_a_window = False
            if flag_to_make_a_window:
                create_window(flag_range_planet_index)

    if flag_to_make_a_window:   # move the window a bit (50 pixels) to the right and down
        if move_window[0] != 400:
            move_window[0] += 50
            move_window[1] += 50
        else:
            move_window[0] = 0
            move_window[1] = 0


def create_window(range_and_rocks):
    if range_and_rocks < len(planets.array):
        planets.array[range_and_rocks].select_it()
        windows.create_and_insert_window((200 + move_window[0], 50 + move_window[1]), (250, 400),
                                         planets.array[range_and_rocks],
                                         (planets.array[range_and_rocks].get_name()))
    elif len(planets.array) <= range_and_rocks < len(planets.array) + len(moons.array):
        moon_index = range_and_rocks - len(planets.array)
        moons.array[moon_index].select_it()
        windows.create_and_insert_window((200 + move_window[0], 50 + move_window[1]), (250, 400),
                                         moons.array[moon_index],
                                         (moons.array[moon_index].get_name()))
    else:
        asteroid_index = range_and_rocks - len(planets.array) - len(moons.array)
        asteroids.array[asteroid_index].select_it()
        windows.create_and_insert_window((200 + move_window[0], 50 + move_window[1]), (250, 400),
                                         asteroids.array[asteroid_index],
                                         asteroids.array[asteroid_index].get_name())


def move_clicked_window_index_forward(clicked_window_index):
    global windows
    temp_window = windows.array[clicked_window_index]
    windows.del_window_index(clicked_window_index)
    windows.insert_window(temp_window)


def update_date(time):
    global date
    global date_string
    global date_five_hours
    hour = None
    month = None
    day = None
    date[3] = time
    if date[3] >= 24*5:
        date[3] -= 24*5
        date[2] += 1
        if date_five_hours - 24*5 >= 0:
            date_five_hours = date_five_hours - 24 * 5
    if date[2] == 31:
        date[2] = 1
        date[1] += 1
        month_passed()
    if date[1] == 13:
        date[1] = 1
        date[0] += 1
    if date[3]/5 < 10:
        hour = "0{}".format(date[3]/5)
    else:
        hour = "{}".format(date[3]/5)
    if date[1] < 10:
        month = "0{}".format(date[1])
    else:
        month = "{}".format(date[1])
    if date[2] < 10:
        day = "0{}".format(date[2])
    else:
        day = "{}".format(date[2])

    date_string = "{}.{}.{}.{}".format(date[0], month, day, hour)


def month_passed():
    for amount_of_planets in range(len(planets.array)):
        planets.array[amount_of_planets].update_stored_resources()
    for amount_of_moons in range(len(moons.array)):
        moons.array[amount_of_moons].update_stored_resources()
    for amount_of_asteroids in range(len(asteroids.array)):
        asteroids.array[amount_of_asteroids].update_stored_resources()

# --- main methode ---


def mainloop():
    global accelerate_time_bool
    global accelerate_time
    global date_five_hours
    global date_rectangle
    global time_forward
    global key_left_control
    global shortest_distance
    global clicked_up
    global clicked_down_at_planet
    global mouse_pos
    global mouse_x
    global mouse_y
    global planets
    global moons
    global button_plus_bool
    global button_minus_bool
    global tick_now
    global TICK_MAX
    global running
    global button_plus
    global button_minus
    global tick_add
    global UI_top
    global move_window_once
    global distances

    for amount_of_moons in range(len(moons.array)):
        moons.array[amount_of_moons].gravity_to_planet()
    for amount_of_planets in range(len(planets.array)):
        planets.array[amount_of_planets].gravity_to_star()
    for amount_of_asteroids in range(len(asteroids.array)):
        asteroids.array[amount_of_asteroids].gravity_to_star()

    while running:

        clicked_down_at_planet = False
        shortest_distance = None

        # keyboard listener

        # mouse listener
        mouse_pos = pygame.mouse.get_pos()
        mouse_rel_pos = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[2]:
            mouse_x, mouse_y = mouse_rel_pos

        if pygame.mouse.get_pressed()[0]:
            for i in range(len(windows.array)):
                windows.array[i].clicked(mouse_pos, mouse_rel_pos)
                if windows.array[i].holds_the_bar is True and move_window_once is not True:
                    print(windows.array[i].name)
                    move_window_once = True
                    move_clicked_window_index_forward(i)
                if move_window_once is True:
                    break

        # if pygame.mouse.get_pressed()[0] is not True:
        #     for i in range(len(windows.array)):
        #         windows.array[i].holds_the_bar = False
        #         move_window_once = False

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                for amount_of_buttons in range(len(buttons.array)):
                    buttons.array[amount_of_buttons].mouse_clicked(event)
                clicked_down_at_planet = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(windows.array)):
                    windows.array[i].holds_the_bar = False
                    move_window_once = False
                for amount_of_buttons in range(len(buttons.array)):
                    buttons.array[amount_of_buttons].mouse_released()
                mouse_x = 0
                mouse_y = 0
            elif event.type == pygame.KEYDOWN:
                for i in range(len(windows.array)):
                    if windows.array[i].changing_name is not False:
                        if event.key == K_RETURN:
                            windows.array[i].changing_name = False
                            windows.array[i].current_text_colour = '#000000'
                            for check_true_origin in range(len(planets.array)):
                                if planets.array[check_true_origin] is windows.array[i].origin:
                                    planets.array[check_true_origin].name = windows.array[i].name
                            for check_true_origin_moon in range(len(moons.array)):
                                if moons.array[check_true_origin_moon] is windows.array[i].origin:
                                    moons.array[check_true_origin_moon].name = windows.array[i].name
                                    # This is terrible but it works ;c
                        elif event.key == K_BACKSPACE:
                            if len(windows.array[i].name) > 0:
                                windows.array[i].name = windows.array[i].name[:-1]
                        else:
                            windows.array[i].name += event.unicode
                if event.key == pygame.K_LCTRL:
                    key_left_control = True
            elif event.type == pygame.KEYUP:
                key_left_control = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(background_colour)

        # RENDER YOUR GAME HERE

        # --- Orbit ---

        for amount_of_moons in range(len(moons.array)):
            moons.array[amount_of_moons].draw_my_orbit(screen)

        for i in range(len(planets.array)):
            planets.array[i].draw_my_orbit(screen)

        # for i in range(len(asteroids.array)):
        #     asteroids.array[i].draw_my_orbit(screen)

        # --- StarPlanetMoonAsteroid ---
        s1.draw_me(screen)

        for i in range(len(planets.array)):
            planets.array[i].draw_me(screen)

        for amount_of_moons in range(len(moons.array)):
            moons.array[amount_of_moons].draw_me(screen)

        for i in range(len(asteroids.array)):
            asteroids.array[i].draw_me(screen)

        distance_from_mouse_to_rocks()

        if pygame.mouse.get_pressed()[0] and clicked_down_at_planet is True:
            rock_clicked()

        # --- Windows ---

        for i in reversed(range(len(windows.array))):
            windows.array[i].draw_me(screen)

        # --- UI ---

        screen.blit(UI_top, (0, 0))
        pygame.draw.rect(screen, '#ffffff', date_rectangle)
        font = pygame.font.SysFont(None, 24)
        img = font.render(date_string, True, 'black')
        screen.blit(img, date_rectangle)
        font = None
        img = None

        # --- Buttons ---

        for amount_of_buttons in range(len(buttons.array)):
            buttons.array[amount_of_buttons].show_button()

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        s1.change_rel_pos(mouse_x/2, mouse_y/2)
        for amount_of_moons in range(len(moons.array)):
            moons.array[amount_of_moons].change_rel_pos(mouse_x/2, mouse_y/2)
        for i in range(len(planets.array)):
            planets.array[i].change_rel_pos(mouse_x/2, mouse_y/2)
        for i in range(len(asteroids.array)):
            asteroids.array[i].change_rel_pos(mouse_x / 2, mouse_y / 2)

        # do some calculations here
        if time_forward is True:
            for j in range(move_time_forward+1):
                if j < move_time_forward:
                    for i in range(len(planets.array)):
                        planets.array[i].move(button_pause_bool)
                    for amount_of_asteroids in range(len(asteroids.array)):
                        asteroids.array[amount_of_asteroids].move(button_pause_bool)
                    for amount_of_moons in range(len(moons.array)):
                        moons.array[amount_of_moons].move(button_pause_bool)
                        moons.array[amount_of_moons].update_main_planet_true_pos()
                    date_five_hours += 1
                    update_date(date_five_hours)
                else:
                    time_forward = False

        if tick_now == 0:
            if accelerate_time_bool is True:
                for j in range(accelerate_time):
                    if j < accelerate_time:
                        for i in range(len(planets.array)):
                            planets.array[i].move(button_pause_bool)
                        for amount_of_asteroids in range(len(asteroids.array)):
                            asteroids.array[amount_of_asteroids].move(button_pause_bool)
                        for amount_of_moons in range(len(moons.array)):
                            moons.array[amount_of_moons].move(button_pause_bool)
                            moons.array[amount_of_moons].update_main_planet_true_pos()
                    if button_pause_bool is False:
                        date_five_hours += 1

            else:
                for i in range(len(planets.array)):
                    planets.array[i].move(button_pause_bool)
                for amount_of_asteroids in range(len(asteroids.array)):
                    asteroids.array[amount_of_asteroids].move(button_pause_bool)
                for amount_of_moons in range(len(moons.array)):
                    moons.array[amount_of_moons].move(button_pause_bool)
                    moons.array[amount_of_moons].update_main_planet_true_pos()
                if button_pause_bool is False:
                    date_five_hours += 1

        if button_pause_bool is False:
            tick_now += tick_add

        if tick_now >= TICK_MAX:
            tick_now = 0

        if button_plus_bool and tick_add != 20:
            tick_add = tick_add * 2
        button_plus_bool = False
        if button_minus_bool and tick_add != 5:
            tick_add = tick_add / 2
        button_minus_bool = False

        for i in range(len(windows.array)):
            if windows.array[i].delete_me is True:
                windows.del_window_index(i)
                break
        if planets.array[2].completed_orbital_cycle is True:
            planets.array[2].completed_orbital_cycle = False

        update_date(date_five_hours)

# Variables outside the main loop

# --- Star ; Planet ; Moon ; Asteroids ---


s1 = Star([500, 500], 80, 1989000000, '#ffff00')

p1 = Planet([166, 166], 10, 20, '#333333', "p1", 0, 0, 0, False)
p1.main_star(s1)
p2 = Planet([224, 224], 15, 30, '#a0b43a', "p2", 0, 0, 0, False)
p2.main_star(s1)
p3 = Planet([359, 359], 20, 40, '#00ff44', "p3", 100, 0, 0, True)
p3.main_star(s1)
p4 = Planet([466, 466], 16, 32, '#dd4403', "p4", 0, 0, 0, False)
p4.main_star(s1)
p5 = Planet([712, 712], 37, 74, '#ffff44', "p5", 0, 0, 0, False)
p5.main_star(s1)
p6 = Planet([853, 853], 30, 60, '#f0f0aa', "p6", 0, 0, 0, False)
p6.main_star(s1)
p7 = Planet([980, 980], 32, 64, '#0ff0ff', "p7", 0, 0, 0, False)
p7.main_star(s1)
p8 = Planet([1147, 1147], 33, 66, '#a389be', "p8", 0, 0, 0, False)
p8.main_star(s1)
m1 = Moon([30, 30], 4, 8, '#a0a0a0', "m1", 0, False)
m1.main_planet(p3)
m2 = Moon([50, 50], 6, 12, "#a4a4a4", "m2", 0, False)
m2.main_planet(p4)
m3 = Moon([68, 68], 5, 10, '#a8a8a8', "m3", 0, False)
m3.main_planet(p5)
m4 = Moon([57, 57], 6, 12, '#a8a8a8', "m4", 0, False)
m4.main_planet(p5)
m5 = Moon([51, 51], 5, 10, '#a3a3a3', "m5", 0, False)
m5.main_planet(p5)
m6 = Moon([45, 45], 4, 8, '#f8a8a8', "m6", 0, False)
m6.main_planet(p5)
a1 = Asteroid([550, 550], 2, 4, '#a0a0a0', 'a1', 0, 0, 0, 0, False)
a1.main_star(s1)
a2 = Asteroid([560, 560], 3, 6, '#a0a0a0', 'a2', 0, 0, 0, 69696969, False)
a2.main_star(s1)
a3 = Asteroid([570, 570], 2, 4, '#a0a0a0', 'a3', 0, 0, 0, 4562, False)
a3.main_star(s1)
a4 = Asteroid([580, 580], 4, 8, '#a0a0a0', 'a4', 0, 0, 0, 8899, False)
a4.main_star(s1)

planets = PlanetList()
planets.add_planet(p1)
planets.add_planet(p2)
planets.add_planet(p3)
planets.add_planet(p4)
planets.add_planet(p5)
planets.add_planet(p6)
planets.add_planet(p7)
planets.add_planet(p8)

moons = MoonList()
moons.add_moon(m1)
moons.add_moon(m2)
moons.add_moon(m3)
moons.add_moon(m4)
moons.add_moon(m5)
moons.add_moon(m6)

asteroids = AsteroidList()
asteroids.add_asteroid(a1)
asteroids.add_asteroid(a2)
asteroids.add_asteroid(a3)
asteroids.add_asteroid(a4)


# --- Images ---

pause_image = pygame.image.load('Pause_Button.png')                     # shown when the game is not paused
pause_image_clicked = pygame.image.load('Pause_Button_Clicked.png')
play_image = pygame.image.load('Play_Button.png')                   # shown when the game is paused
play_image_clicked = pygame.image.load('Play_Button_Clicked.png')
plus_image = pygame.image.load('Plus_Button.png')                   # always shown except when the button is clicked
plus_image_clicked = pygame.image.load('Plus_Button_Clicked.png')       # shown when the plus button is clicked
minus_image = pygame.image.load('Minus_Button.png')                 # always shown except when the button is clicked
minus_image_clicked = pygame.image.load('Minus_Button_Clicked.png')     # shown when the minus button is clicked
ships_image = pygame.image.load('Ships_Button.png')
ships_image_clicked = pygame.image.load('Ships_Clicked_Button.png')
planets_image = pygame.image.load('Planets_Button.png')
planets_image_clicked = pygame.image.load('Planets_Clicked_Button.png')
science_image = pygame.image.load('Science_Button.png')
science_image_clicked = pygame.image.load('Science_Clicked_Button.png')
UI_top = pygame.image.load('Blue.png')                                  # always shown on the top

# --- Buttons ---

button_science = Button((600, 0), (50, 50), None, None, 'ships', [science_image, None], [science_image_clicked, None])

button_ships = Button((650, 0), (50, 50), None, None, 'ships', [ships_image, None], [ships_image_clicked, None])

button_planets = Button((700, 0), (50, 50), None, None, 'planets', [planets_image, None], [planets_image_clicked, None])

button_pause = Button((850, 0), (50, 50), '#00ff00', '#00aa00', "pause", [pause_image, play_image],
                      [pause_image_clicked, play_image_clicked])
# used to pause or resume the game
button_plus = Button((900, 0), (50, 50), '#0000ff', '#0000aa', "plus", [plus_image, None],
                     [plus_image_clicked, None])
# used to speed the game up
button_minus = Button((950, 0), (50, 50), '#ff0000', '#aa0000', "minus", [minus_image, None],
                      [minus_image_clicked, None])
# used to slow the game down

buttons = ButtonList()
buttons.add_button(button_ships)
buttons.add_button(button_planets)
buttons.add_button(button_pause)
buttons.add_button(button_plus)
buttons.add_button(button_minus)
buttons.add_button(button_science)

# --- UI things ---

date_rectangle = Rect(750, 0, 100, 50)

# --- Variables ---

key_left_control = False        # used to select multiple planets when holding left_control
selected_planets = []           # should be used to save indexes of planets that are highlighted (clicked)
clicked_down_at_planet = False  # currently used in clicking at a planet or outside of it
clicked_up = False              # currently used for nothing
shortest_distance = None        # currently used to know the shortest distance between mouse loc and a planet's centre
planet_index = None             # currently used for knowing which planet is being clicked
mouse_pos = None                # currently used for knowing where the mouse is, it's used for calculating shortest_distance
tick_add = 20                   # game speed, can be changed in game between 20, 10 and 5. 20 tick is the fastest
tick_now = 0                    # current tick
TICK_MAX = 20                   # max tick, if higher than the game will run slower
button_plus_bool = False        # used for knowing if the plus button was clicked
button_minus_bool = False       # used for knowing if the minus button was clicked
button_pause_bool = False       # used for knowing if the pause button was clicked
mouse_x = 0                     # relative mouse_x location
mouse_y = 0                     # relative mouse_y location
move_time_forward = 100000      # Moves the timer forward to make the planets start in a different position than on the right side
time_forward = False            # If true, then move_time_forward is accepted
accelerate_time = 16            # The greater the number, the faster the game progresses
accelerate_time_bool = True    # If true, then the game uses accelerate_time to... accelerate the game
date_five_hours = 0             # The current displayed time measured in five hours per tick
move_window_once = False        # Used to move clicked window in windows.array to the front only once
background_colour = '#050550'   # Used as a background colour for the game
date = [0, 1, 1, 0]             # it will be used to measure how long certain things happen. YY.MM.DD.HH
date_string = None              # it displays date. Pog
distances = []                  # saves all distances from mouse to planets//moons
move_window = [0, 0]            # used to create newer windows a little to the side

# --- Windows ---

windows = WindowList()

# --- Player Resources ---


# Game Initialisation

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('Space')

mainloop()

pygame.quit()
