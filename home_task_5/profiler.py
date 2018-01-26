import sys
import time
import functools

def profiler(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        decorator.recursion_calls += 1
        decorator.recursion += 1
        start_time = time.time()
        result = func(*args, **kwargs)
        decorator.recursion -= 1
        if decorator.recursion == 0:
            decorator.calls = decorator.recursion_calls
            decorator.recursion_calls = 0
            decorator.last_time_taken = time.time() - start_time
        return result

    decorator.recursion = 0
    decorator.recursion_calls = 0
    decorator.calls = 0
    decorator.last_time_taken = 0
    return decorator

exec(sys.stdin.read())
