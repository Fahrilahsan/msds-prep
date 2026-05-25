import functools
from os import name
import time
from turtle import up
import math
import random

def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")


    first_child() #tidak bisa dipanggil di luar parent() karena berada di dalam parent()
    second_child() 

def parent_dua(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1: #mengakali dengan if untuk menentukan fungsi mana yang akan dijalankan
        return first_child
    else:
        return second_child
    

# parent() #memanggil parent() untuk menjalankan fungsi di dalamnya, jika tidak dipanggil maka tidak akan ada output yang muncul
# print(parent_dua(1)()) #memanggil parent_dua() dengan argumen 1 untuk mendapatkan fungsi first_child, lalu menambahkan () untuk menjalankan fungsi tersebut

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)


# say_whee()


# ...

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


# waste_some_time(999)


# ...

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"

# make_greeting("Benjamin")

# make_greeting("Juan", age=114)

# make_greeting(name="Maria", age=116)



# ...

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# approximate_e(terms=10)




# ...

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

# countdown(3)



# ...


# ...

PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

# print(PLUGINS)
# print(PLUGINS['say_hello']('Alice'))

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(randomly_greet("Alice"))

# print(globals())
globals()