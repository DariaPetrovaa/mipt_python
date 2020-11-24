import numpy as np

class PrintAverage(Exception):
    pass

class PrintDispersion(Exception):
    pass

class PrintNumber(Exception):
    pass

def the_coroutine():
    print("Starting coroutine")
    data = []
    try:
        while True:
            try:
                x = yield
                data.append(x)
            except PrintDispersion:
                yield np.var(data)
            except PrintAverage:
                yield np.mean(data)
            except PrintNumber:
                yield len(data)
    finally:
        print("Stop coroutine")

coroutine = the_coroutine()
next(coroutine)
for i in range(12):
    coroutine.send(i)
    if i%2 == 0:
        print("Average:", coroutine.throw(PrintAverage))
        next(coroutine)
    if i%3 == 0:
        print("Dispersion:", coroutine.throw(PrintDispersion))
        next(coroutine)
    if i%4 == 0:
        print("Number of data:", coroutine.throw(PrintNumber))
        next(coroutine)


