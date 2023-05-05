from math import sqrt

import pygame
from pygame import Rect, K_BACKSPACE, K_RETURN

from Star import Star
from Planet import Planet
from Moon import Moon
from ArrayList import PlanetList
from ArrayList import MoonList
from ArrayList import WindowList
from ResourceList import PlayerResources


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
        self.current_image = image_calm
        self.current_colour = self.colour_calm
        self.rectangle = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def mouse_clicked(self, event):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rectangle.collidepoint(x, y):
                # self.current_colour = self.colour_clicked
                self.current_image = self.image_clicked
                key_clicked(self.name)
            else:
                # self.current_colour = self.colour_calm
                pass

    def mouse_released(self):
        if self.name != "pause":
            self.current_image = self.image_calm

    def show_button(self):
        # pygame.draw.rect(screen, self.current_colour, self.rectangle)
        screen.blit(self.current_image, self.pos)


# methods


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
    distances = temp_distances


def rock_clicked():
    global move_window
    flag_range_planet_index = None   # range_planet_index is saved here when the method wants to create a window.
    flag_to_make_a_window = True    # It is set to false when this method recognises that a window is already there.
    for delete in range(len(planets.array)):
        planets.array[delete].unselect_it()
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
    if flag_to_make_a_window:   # move the window a bit (50 pixels) to the right and down
        if move_window[0] != 400:
            move_window[0] += 50
            move_window[1] += 50
        else:
            move_window[0] = 0
            move_window[1] = 0


def create_window(range_and_planets):
    planets.array[range_and_planets].select_it()
    windows.create_and_insert_window((200 + move_window[0], 50 + move_window[1]), (250, 400),
                                     planets.array[range_and_planets],
                                     (planets.array[range_and_planets].get_name()))


def key_clicked(name):
    global button_pause_bool
    global button_plus_bool
    global button_minus_bool
    if name == 'pause' and button_pause_bool is False:
        button_pause_bool = True
        button_pause.current_image = button_pause.image_clicked
    elif name == 'pause' and button_pause_bool:
        button_pause_bool = False
        button_pause.current_image = button_pause.image_calm
    if name == 'plus':
        button_plus_bool = True
        # button_plus.current_image = button_plus.image_clicked
    if name == 'minus':
        button_minus_bool = True
        # button_minus.current_image = button_minus.image_clicked


def move_clicked_window_index_forward(clicked_window_index):
    global windows
    temp_window = windows.array[clicked_window_index]
    windows.del_window_index(clicked_window_index)
    windows.insert_window(temp_window)


def update_date(time):
    global date
    global date_string
    global date_five_hours
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
    if date[1] == 13:
        date[1] = 1
        date[0] += 1
    if date[1] < 10:
        month = "0{}".format(date[1])
    else:
        month = "{}".format(date[1])
    if date[2] < 10:
        day = "0{}".format(date[2])
    else:
        day = "{}".format(date[2])

    date_string = "{}.{}.{}.{}".format(date[0], month, day, date[3]/5)

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
                button_plus.mouse_clicked(event)
                button_minus.mouse_clicked(event)
                button_pause.mouse_clicked(event)
                clicked_down_at_planet = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(windows.array)):
                    windows.array[i].holds_the_bar = False
                    move_window_once = False
                button_plus.mouse_released()
                button_minus.mouse_released()
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

        # --- StarPlanetMoonAsteroid ---

        # pygame.draw.circle(screen, s1.colour, s1.pos, s1.radius, width=s1.radius-1)
        s1.draw_me(screen)

        for i in range(len(planets.array)):
            planets.array[i].draw_me(screen)

        for amount_of_moons in range(len(moons.array)):
            moons.array[amount_of_moons].draw_me(screen)

        distance_from_mouse_to_rocks()
        #distance()

        if pygame.mouse.get_pressed()[0] and clicked_down_at_planet is True:
            # planet_clicked()
            rock_clicked()

        # --- Windows ---

        for i in reversed(range(len(windows.array))):
            windows.array[i].draw_me(screen)

        # --- UI ---

        screen.blit(UI_top, (0, 0))
        pygame.draw.rect(screen, '#ffffff', date_rectangle)
        font = pygame.font.SysFont(None, 24)
        img = font.render(date_string, True, 'black')
        #img = font.render(str(date_five_hours/5), True, 'black')
        screen.blit(img, date_rectangle)
        font = None
        img = None

        # --- Buttons ---

        button_plus.show_button()
        button_minus.show_button()
        button_pause.show_button()

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

        s1.change_rel_pos(mouse_x/2, mouse_y/2)
        for amount_of_moons in range(len(moons.array)):
            moons.array[amount_of_moons].change_rel_pos(mouse_x/2, mouse_y/2)
        for i in range(len(planets.array)):
            planets.array[i].change_rel_pos(mouse_x/2, mouse_y/2)

        # do some calculations here
        if time_forward is True:
            for j in range(move_time_forward+1):
                if j < move_time_forward:
                    for i in range(len(planets.array)):
                        planets.array[i].move(button_pause_bool)
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
                        for amount_of_moons in range(len(moons.array)):
                            moons.array[amount_of_moons].move(button_pause_bool)
                            moons.array[amount_of_moons].update_main_planet_true_pos()
                    if button_pause_bool is False:
                        date_five_hours += 1

            else:
                for i in range(len(planets.array)):
                    planets.array[i].move(button_pause_bool)
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

p1 = Planet([166, 166], 10, 20, '#333333', "p1", 0, 0, 0)
p1.main_star(s1)
p2 = Planet([224, 224], 15, 30, '#a0b43a', "p2", 0, 0, 0)
p2.main_star(s1)
p3 = Planet([359, 359], 20, 40, '#00ff44', "p3", 100, 0, 0)
p3.main_star(s1)
p4 = Planet([466, 466], 16, 32, '#dd4403', "p4", 0, 0, 0)
p4.main_star(s1)
p5 = Planet([712, 712], 37, 74, '#ffff44', "p5", 0, 0, 0)
p5.main_star(s1)
p6 = Planet([853, 853], 30, 60, '#f0f0aa', "p6", 0, 0, 0)
p6.main_star(s1)
p7 = Planet([980, 980], 32, 64, '#0ff0ff', "p7", 0, 0, 0)
p7.main_star(s1)
p8 = Planet([1147, 1147], 33, 66, '#a389be', "p8", 0, 0, 0)
p8.main_star(s1)
m1 = Moon([30, 30], 4, 8, '#a0a0a0', "m1")
m1.main_planet(p3)
m2 = Moon([50, 50], 6, 12, "#a4a4a4", "m2")
m2.main_planet(p4)
m3 = Moon([68, 68], 5, 10, '#a8a8a8', "m3")
m3.main_planet(p5)
m4 = Moon([57, 57], 6, 12, '#a8a8a8', "m4")
m4.main_planet(p5)
m5 = Moon([51, 51], 5, 10, '#a3a3a3', "m5")
m5.main_planet(p5)
m6 = Moon([45, 45], 4, 8, '#f8a8a8', "m6")
m6.main_planet(p5)

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


# --- Images ---

pause_image = pygame.image.load('Pause.png')                    # shown when the game is not paused
play_image = pygame.image.load('Play.png')                      # shown when the game is paused
plus_image = pygame.image.load('Plus.png')                      # always shown except when the button is clicked
plus_clicked_image = pygame.image.load('Plus_Clicked.png')      # shown when the plus button is clicked
minus_image = pygame.image.load('Minus.png')                    # always shown except when the button is clicked
minus_clicked_image = pygame.image.load('Minus_Clicked.png')    # shown when the minus button is clicked
UI_top = pygame.image.load('Blue.png')                          # always shown on the top

# --- Buttons ---

button_pause = Button((850, 0), (50, 50), '#00ff00', '#00aa00', "pause", pause_image, play_image)
# used to pause or resume the game
button_plus = Button((900, 0), (50, 50), '#0000ff', '#0000aa', "plus", plus_image, plus_clicked_image)
# used to speed the game up
button_minus = Button((950, 0), (50, 50), '#ff0000', '#aa0000', "minus", minus_image, minus_clicked_image)
# used to slow the game down

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
accelerate_time_bool = True     # If true, then the game uses accelerate_time to... accelerate the game
date_five_hours = 0             # The current displayed time measured in five hours per tick
move_window_once = False        # Used to move clicked window in windows.array to the front only once
background_colour = '#050550'   # Used as a background colour for the game
date = [0, 1, 1, 0]             # it will be used to measure how long certain things happen. YYMMDDHH
date_string = None              # it displays date. Pog
distances = []                  # saves all distances from mouse to planets//moons
move_window = [0, 0]            # used to create newer windows a little to the side

# --- Windows ---

windows = WindowList()

# --- Player Resources ---

player_resources = PlayerResources(energy=0, minerals=0, metals=0, retail_goods=0, food=0, water=0, fossil_fuels=0,
                                   rare_elements=0, chemicals=0, bio_resources=0, science=0, population=0, labour=0)

# Game Initialisation

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('Space')

mainloop()

pygame.quit()
