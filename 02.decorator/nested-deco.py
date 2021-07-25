def decorator(num):
    def outer_wrapper(func):
        def _func(*args, **kwargs):
            print("decorator num: {}".format(num))
            return func(*args, **kwargs)
        return _func
    return outer_wrapper


def func():
    print("Last")


@decorator(1)
def test_1():
    print("Last!!")


test_1()
# 위 함수는 아래 실행과 같다.
test_2 = decorator(2)(func)
test_2()


def mark_html(tag):
    def outer_wrapper(func):
        def inner(*args, **kwargs):
            return "<{tag}>{result}</{tag}>".format(tag=tag, result=func(*args, **kwargs))
        return inner
    return outer_wrapper


@mark_html("h2")
def h2_tag(text):
    return text


print(h2_tag("Hello!!!!!!"))
