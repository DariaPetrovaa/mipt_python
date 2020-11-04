import itertools

def get_combinations_with_r(s,k):
    try:
        return sorted(list(''.join(sorted(x)) for x in itertools.combinations_with_replacement(s,k)))
    except:
        raise RuntimeError('Not Implemented')



