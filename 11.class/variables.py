class Figure:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

        # class variable
        Figure.count += 1

    def __del__(self):
        Figure.count -= 1

    def calc_area(self):
        return self.width * self.height


figure_1 = Figure(2, 3)
print(Figure.count)  # 1

figure_2 = Figure(3, 4)
print(Figure.count)  # 2

del figure_1
print(Figure.count)  # 1

del figure_2
print(Figure.count)  # 0
