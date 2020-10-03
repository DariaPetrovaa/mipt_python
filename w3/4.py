import json
with open('1.json','r') as out:
    data=json.load(out)
    print(json.dumps(data, indent=4, sort_keys = True))
    b = data['glossary']['GlossDiv']['GlossList']['GlossEntry']
    b['week']=3
#with open ('1.json', 'w') as out:
#   json.dump(data, out, indent = 4)
with open ('1.json','w') as out:
    out.write(json.dumps(data, indent = 4))
with open('1.json','r') as out:
    data_n=json.load(out)
    print(json.dumps(data_n, indent=4, sort_keys=True))
            


    



