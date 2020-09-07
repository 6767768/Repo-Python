'''
# decorator requires argument to be a callable object
def foo():
    pass

callable(foo)

# callable class
class Foo:
    def __call__(self):
        print("------------")

foo = Foo()
foo()
'''

import time
import functools

class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"wait for {self.duration} seconds...")
        time.sleep(self.duration)

        print(self.func(1, 2))
        
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print("Call without delay")
        return self.func(*args, **kwargs)

def delay(duration):
    return functools.partial(DelayFunc, duration)


@delay(duration = 2)
def add(a, b):
    return a+b


add(1, 2)
add.eager_call(1, 2)

