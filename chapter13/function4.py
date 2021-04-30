def debug(function):
    def _debug(*args, **kwargs):
        result = function(*args, **kwargs)
        print(function.__name__, args, kwargs, result)
        return result
    return _debug


@debug
def say_hello(num):
    return num + 10


def decorator(function):
    print('decorator')
    return function


@decorator
def say_good():
    print('Good!')


say_hello(5)
say_good()
