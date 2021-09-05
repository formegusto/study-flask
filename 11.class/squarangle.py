class Squarangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        return self.width * self.height

    def set_area(self, width, height):
        self.width = width
        self.height = height


square_1 = Squarangle(10, 5, "red")
square_2 = Squarangle(7, 7, "blue")

print(square_1.width, square_1.height, square_1.color)
print(square_2.width, square_2.height, square_2.color)
