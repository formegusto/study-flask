def h1_tag(func):
    def _func(self, *args, **kwargs):
        return "<h1>{}</h1>".format(func(self, *args, **kwargs))
    return _func


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @h1_tag
    def get_name(self):
        return self.first_name + " " + self.last_name


person = Person("no", "th")
print(person.get_name())

print("{aa}, {bb}".format(aa='hello', bb='bye'))
