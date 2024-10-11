# write a decorator that measures the time a function takes to execute.

import time


def time_calculation(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)  # function get executed.
        end = time.time()
        return f" {func.__name__} execution time was {end-start}"

    return wrapper


@time_calculation
def examplefunction(n):
    time.sleep(n)


print(examplefunction(2))
