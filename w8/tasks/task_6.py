import itertools

def get_combinations(s,k):
    try:
        a = sorted(list(''.join(sorted(x)) for i in range (1,k+1) for x in itertools.combinations(s,i)))
        a.sort(key = lambda x: len(x))
        return a
    except:
        raise RuntimeError('Not Implemented')






