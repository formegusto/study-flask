def calc_square(digit):
    return digit ** 2


def calc_plus(digit):
    return digit + digit


def calc_quad(digit):
    return digit ** 4


def list_square(function, digit_list):
    result = []
    for digit in digit_list:
        result.append(function(digit))
    return result


# 1. 다른 변수에 할당 가능
fn = calc_square
print(fn(10))  # 100

# 2. 인자로 전달 가능
num_list = [1, 2, 3, 4, 5]
print(list_square(calc_square, num_list))  # [1, 4, 9, 16, 25]
print(list_square(calc_plus, num_list))  # [2, 4, 6, 8, 10]
print(list_square(calc_quad, num_list))  # [1, 16, 81, 256, 625]

# 3. 함수의 결과값으로 함수를 리턴할 수 있다.


def logger(msg):
    message = msg

    def msg_creator():
        print("[DEBEG LEVEL] : {}".format(message))
    return msg_creator


log = logger("TH Logged In")
log()  # [DEBEG LEVEL] : TH Logged In


def html_creator(tag):
    def text_wrapper(text=None):
        return "<{0}>{1}</{0}>".format(tag, "" if text == None else text)
    return text_wrapper


h1_html_creator = html_creator("h1")
print(h1_html_creator("Hello Flask!"))


def index_creator(index):
    def prefix_data(list):
        for string in list:
            yield "{0} {1}".format(index, string)
    return prefix_data


fn = index_creator("●")
todo_list = [todo for todo in fn(["밥 먹기", "양치질 하기", "개발 공부하기"])]
for todo in todo_list:
    print(todo)
