def print_map(function, iterable):
    n = len(iterable)
    iterator = iter(iterable)
    k=0
    while k<n:
        print(function(next(iterator)))
        k+=1

def my_func(b):
    return b**2

print_map(my_func, [0,1,2,3,4,5])
