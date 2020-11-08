import itertools

def compress_string(s):
    a=[]
    b=[]
    for key,value in itertools.groupby(s):
        a.append(key)
        b.append(len(list(value)))
    return list(zip(b,a))

#print(compress_string('aaadtdcdcrnjkiu'))
#print(compress_string('123455'))

