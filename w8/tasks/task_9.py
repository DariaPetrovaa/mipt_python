import itertools


def maximize(lists, m):
    a = list(max(i)**2 for i in lists)
    b = list(x for x in itertools.accumulate(a))
    ans = max(x % m for x in b)
    return ans

lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
#print(maximize(lists,1000))
