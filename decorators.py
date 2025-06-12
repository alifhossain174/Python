import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Before Hello")
        func()
        print("After Hello")

    return wrapper

@decorator
def sayHello():
    print(sayHello.__name__)


sayHello()