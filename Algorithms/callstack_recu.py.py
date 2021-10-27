def fact_x(x):
    if x == 1:
        return 1
    else:
        return x * fact_x(x-1)


print(fact_x(5))
