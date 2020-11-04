import itertools

def get_permutations(s,n):
    try:
        return sorted(list(''.join(x) for x in itertools.permutations(s,n)))
    except:
        raise RuntimeError('Not Implemented')



