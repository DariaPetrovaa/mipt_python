def merge (a,b):
    i=j=0
    n, m = len(a), len(b)
    c=[]
    while i<n and j<m:
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    c+= a[i:] + b[j:]
    return c
def merge_sort(a):
    if len(a)==1:
        return a
    m=len(a)//2
    x=merge_sort(a[:m])
    y=merge_sort(a[m:])
    return merge(x,y)

a=[1,6,2]
print(merge_sort(a))
