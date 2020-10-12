def write_array(array, file_name):
    array = map(lambda x : x + ' ',array)
    file_name.writelines(array)

a = ['avf', 'hello']
with open('output.txt', 'w') as file:
   write_array(a, file)

