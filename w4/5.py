def my_decorator(function):
    def the_wrapper(*args, *kwargs):
        ans=function(*args, **kwargs)
        if ans==0:
            return 'Нет('
        if ans>10:
            return 'Очень много'
        else:
            return ans
    return the_wrapper

@my_decorator
def even_number(a):
    count=0
    for i in range(len(a)):
        if a[i]%2==0:
            count+=1
    return count

print(even_number([1,2,3,4,5,6,9,8]))
print(even_number([2,4,6,8,2,4,6,8,2,5,4,10,12]))
print(even_number([1,3,5,7,5]))
