import sys
import argparse

def eratosthenes_sieve(k):
    n=k*20
    prime = [True] *(n+1)
    prime[0]=prime[1]=False
    for i in range(2, n+1):
        if prime[i] and i*i<=n:
            for j in range(i*i, n+1, i):
                prime[j]=False
    return [i for i,j in enumerate(prime) if j]


def find_prime(k):
    if k==1:
        return 2
    else:
        return eratosthenes_sieve(k)[k-1]


def show(k):
    if k==1:
        return "There is no revious prime number"
    else:
        return eratosthenes_sieve(k)[:k]


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('number', type=int)
    parser.add_argument('-a' , '--show-all',action = 'store_true', default=False)
    parser.add_argument('-f', '--file', type = argparse.FileType('w'))
    
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

a=find_prime(namespace.number)
print(a)
if namespace.file is not None:
    print(a, file = namespace.file)
if namespace.show_all:
    b=show(namespace.number)
    print(b)
    if namespace.file is not None:
        print(b, file = namespace.file)


