k=input()
try:
   k= int(k)
except ValueError:
    print('Это не число')
#print(k)
finally:
    print('hello')
