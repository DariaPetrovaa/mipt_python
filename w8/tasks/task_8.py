import itertools

def compress_string(s):
    try:
        a=[]
        b=[]
        for key,value in itertools.groupby(s):
            a.append(int(key))
            b.append(len(list(value)))
        return list(zip(b,a))
    except:
        raise RuntimeError('Not Implemented')



