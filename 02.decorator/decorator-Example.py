def type_check(func):
    def _func(digit1, digit2):
        if (type(digit1) != int) or (type(digit2) != int):
            print("only integer support!")
        else:
            func(digit1, digit2)

    return _func


@type_check
def multiply(digit1, digit2):
    print(digit1 * digit2)


multiply("1", "2")
multiply(1, 3)

# 파라미터와 관계없이 모든 함수에 적용가능한 Decorator
# 파라미터는 어떤 형태이든 결국 (args, **kwargs)로 표현가능


def general_decorator(func):
    def _func(*args, **kwargs):
        print("hello is func decorated")
        return func(*args, **kwargs)
    return _func


@general_decorator
def calc_square(digit):
    return digit * digit


@general_decorator
def calc_plus(digit1, digit2):
    return digit1 + digit2


print(calc_square(6))
print(calc_plus(1, 3))


# 한 함수에 데코레이터 여러 개 지정하기
def deco1(func):
    def _func():
        print('deco1')
        func()
    return _func


def deco2(func):
    def _func():
        print('deco2')
        func()
    return _func


@deco1
@deco2
def isLast():
    print("iamog!")


isLast()


def mark_bold(func):
    def _func(text):
        return func(text)

    return _func


def mark_italic(func):
    def _func(text):
        return func(text)

    return _func


print()


@mark_bold
def bold(text):
    return "<b>{}</>".format(text)


print(bold("hello!"))
