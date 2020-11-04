def analogue_zip(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

def analogue_map(function, iterable):
    for i in iterable:
        yield function(i)

def analogue_enumerate(iterable, start=0):
    n=start
    for _ in iterable:
        yield n, _
        n+=1



