def outer_func(num):
    def inner_func():
        print(num)
        return 'hi!'

    return inner_func


closure_func = outer_func(10)
closure_func()


def calc_power(n):
    def power(digit):
        return digit ** n
    return power


print(calc_power(2)(2))  # 4
print(calc_power(3)(2))  # 8
print(calc_power(4)(2))  # 16

list_data = [calc_power(n) for n in range(1, 6)]
print(list_data[0](2))
print(list_data[1](2))
print(list_data[4](2))
