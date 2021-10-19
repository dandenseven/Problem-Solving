"""Call stack with recursion"""


def fact(x):
    """Call stack using recursion"""
    print(x)
    if x == 1:
        return 1

    return x * fact(x-1)


fact(5)
