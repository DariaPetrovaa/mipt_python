import itertools

def get_cartesian_product(a,b):
    try:
        return list(itertools.product(a,b,repeat=1))
    except:
        raise RuntimeError('Not Implemented')

