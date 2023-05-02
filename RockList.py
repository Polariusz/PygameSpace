from Rock import Rock


class Array:
    def __init__(self):
        self.array = []
        self.temp = None

    def add_rock(self, r):
        self.array.append(r)
        print("IN ROCKLIST!!!: Rock appended")

    def remove_rock(self, r, i):
        if r is not None:
            for j in range(len(self.array)):
                if self.array[j] == r:
                    self.array.pop(j)
                    print("IN ROCKLIST!!!: Rock removed!")
                    break
                else:
                    print("IN ROCKLIST!!!: This rock does not exist")
        elif i is not None and r is None:
            self.array.pop(i)

    def create_rock(self, x_pos, y_pos, radius, mass, colour, array):
        self.temp = Rock(x_pos, y_pos, radius, mass, colour, array)
        self.add_rock(self.temp)
        self.temp = None
        print("IN ROCKLIST!!!: Rock created!")
