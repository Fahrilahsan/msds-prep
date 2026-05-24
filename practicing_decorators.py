import functools
import time

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


waste_some_time(999)



