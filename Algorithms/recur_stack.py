# call stack using recursion


def fact(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


fact(5)
