def print_map(function, iterable):
    print(*(map(function,iterable)))

def my_func(b):
    return b**2

print_map(my_func, [0,1,2,3,4,5])
