import zipfile
with zipfile.ZipFile('main.zip','r') as zip_ref:
    zip_ref.extractall('given files')

import os
w=list()
for root, dirs, files in os.walk("given files"):
    for file in files:
        if file.endswith(".py"):
            p=os.path.join(root)
            p=p[::-1]
            for i in range(len(p)):
                if p[i]=='/':
                    p=p[:i]
                    p=p[::-1]
                    break
            w.append(p)
w.sort()
for i in range(1,len(w)):
    if w[i]!=w[i-1]:
        print(w[i-1])
print(w[i])
#a=list()
#for name in w:
#    a.append(name[-2])
#print(a)
