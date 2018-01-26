import sys
import time
import functools

def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            i = 0
            for arg in args:
                if type(arg) is not types[i]:
                    raise TypeError
                i += 1
            for k, v in kwargs:
                if type(v) is not types[i]:
                    raise TypeError
                i += 1
            val = func(*args, **kwargs)
            return val
        return decorated
    return decorator

exec(sys.stdin.read())
