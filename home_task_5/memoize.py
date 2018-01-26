import sys
import time
import functools

def memoize(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        key = ''
        for arg in args:
            key += str(arg) + ' '
        for k, v in kwargs.iteritems():
            key += k + ':' + str(v) + ' '

        if key not in decorator.cache:
            result = func(*args, **kwargs)
            decorator.cache[key] = result
        else:
            result = decorator.cache[key]
        return result

    decorator.cache = {}
    return decorator

exec(sys.stdin.read())
