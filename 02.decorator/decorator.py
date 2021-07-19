from datetime import datetime as dt


def datetime_decorator(func):
    def wrapper():
        print("time: {}".format(dt.now()))
        func()
        print("time: {}".format(dt.now()))
    return wrapper


@datetime_decorator
def login_th():
    print("th logged in")


@datetime_decorator
def login_forme():
    print("forme logged in")


login_th()
login_forme()


def i_am_john():
    print("john logged in")


login_john = datetime_decorator(i_am_john)
login_john()


def divider(func):
    def _func(digit1, digit2):
        if digit2 == 0:
            print("Please Input Digit!")
            return
        return func(digit1, digit2)
    return _func


@divider
def plus_divider(digit1, digit2):
    return digit1 + digit2


@divider
def multi_divider(digit1, digit2):
    return digit1 * digit2


print(plus_divider(10, 20))
print(multi_divider(10, 20))
