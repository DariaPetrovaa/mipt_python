def c():
    raise ValueError('exception')
    
def b():
    c()

def a():
    b()

a()
