class Figure:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

        # class variable
        Figure.count += 1

    @staticmethod
    def is_square(rect_width, rect_height):
        if rect_width == rect_height:
            print("정사각형이 될 수 있습니다.")
        else:
            print("정사각형이 되기 힘든 너비와 높이 입니다.")

    @classmethod
    def print_count(cls):
        print(cls.count)


Figure.is_square(2, 3)
Figure.is_square(3, 3)
Figure.print_count()
