"""Count down with recursion"""


def countdown(i):
    """Count down function"""
    print(i)
    if i <= 1:
        return
    countdown(i - 1)


countdown(9)
