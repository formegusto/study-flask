def outer_func():
    print("call outer func")

    # define inner func
    def inner_func():
        return "call inner func"

    # call inner func
    print(inner_func())


# outer_func()
# inner_func() # NameError: name 'inner_func' is not defined
# 중첩 함수도 로컬 변수처럼 동작한다.

def outer_rtn_func():
    print("call outer rtn func()")

    def inner_rtn_func(number):
        print(number)
        return "complex"

    return inner_rtn_func


irf = outer_rtn_func()
print(irf(10))
