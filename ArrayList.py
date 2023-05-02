from Window import Window


class PlanetList:
    def __init__(self):
        self.array = []
        self.temp = None

    def add_planet(self, p):
        self.array.append(p)

    def del_planet_index(self, index):
        temp_name = self.array[index].get_name()
        self.array.pop(index)
        print("IN ARRAYLIST|PlanetList|-del_planet_index: Planet {}, deleted!".format(temp_name))

    def del_planet_name(self, name):
        for i in range(len(self.array)):
            if self.array[i].get_name() == name:
                self.array.pop(i)
                print("IN ARRAYLIST|PlanetList|-del_planet_name: Planet {}, deleted!".format(name))
                break

    def del_planet_object(self, planet):
        for i in range(len(self.array)):
            if self.array[i] == planet:
                temp_name = self.array[i].get_name()
                self.array.pop(i)
                print("IN ARRAYLIST|PlanetList|-del_planet_object: Planet {}, deleted!".format(temp_name))
                break


class MoonList:
    def __init__(self):
        self.array = []
        self.temp = None

    def add_moon(self, m):
        self.array.append(m)

    def del_moon_index(self, index):
        temp_name = self.array[index].name
        self.array.pop(index)
        print("IN ARRAYLIST|MoonList|-del_moon_index: Moon {}, deleted!".format(temp_name))

    def del_moon_name(self, name):
        for i in range(len(self.array)):
            if self.array[i].name == name:
                self.array.pop(i)
                print("IN ARRAYLIST|MoonList|-del_moon_name: Moon {}, deleted!".format(name))
                break

    def del_moon_object(self, moon):
        for i in range(len(self.array)):
            if self.array[i] == moon:
                temp_name = self.array[i].name
                self.array.pop(i)
                print("IN ARRAYLIST|MoonList|-del_moon_object: Moon {}, deleted!".format(temp_name))
                break


class WindowList:
    def __init__(self):
        self.array = []
        self.temp = None

    def create_and_append_window(self, pos, size, origin, name):
        temp = Window(pos, size, origin, name)
        self.array.append(temp)

    def create_and_insert_window(self, pos, size, origin, name):
        temp = Window(pos, size, origin, name)
        self.array.insert(0, temp)

    def add_window(self, w):
        self.array.append(w)

    def insert_window(self, w):
        self.array.insert(0, w)

    def del_window_index(self, index):
        temp_name = self.array[index].get_name()
        self.array.pop(index)
        print("IN ARRAYLIST|WindowList|-del_window_index: Window {}, deleted".format(temp_name))

    def del_window_name(self, name):
        for i in range(len(self.array)):
            if self.array[i].get_name() == name:
                self.array.pop(i)
                print("IN ARRAYLIST|WindowList|-del_window_name: Window {}, deleted!".format(name))
                break

    def del_window_object(self, window):
        for i in range(len(self.array)):
            if self.array[i] == window:
                temp_name = self.array[i].get_name()
                self.array.pop(i)
                print("IN ARRAYLIST|WindowList|-del_window_object: Window {}, deleted!".format(temp_name))
                break
