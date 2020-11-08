import itertools

def get_permutations(s,n):
    return sorted(list(''.join(x) for x in itertools.permutations(s,n)))



