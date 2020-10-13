import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n','--number', type=int)
    # '?' -- either 1 or absent
    # 1 -- list of len 1
    # 2 -- list of len 2 and so on

    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

def fib(n):
    print(n)
    print(type(n))
    n=int(n)
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(namespace.number))


