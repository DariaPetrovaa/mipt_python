def gen_fib():
    a,b = 1,1
    while True:
        yield a
        a,b = b, a+b 

def my_fib(n):
    f = gen_fib()
    a = []
    for i in range(n):
        a.append(next(f))
    return a

#print(my_fib(1))
#print(*my_fib(10))



