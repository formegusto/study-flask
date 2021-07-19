class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1

    def decrease(self):
        self.value -= 1

    def print_value(self):
        print("Now, Counter is {}".format(self.value))


if __name__ == "__main__":
    counter = Counter(0)

    counter.increase()
    counter.print_value()

    counter.decrease()
    counter.print_value()
