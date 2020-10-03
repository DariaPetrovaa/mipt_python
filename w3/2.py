def write_array(array, file_name):
    with open(array,"r") as input, open (file_name, "w") as output:
        output.write(input.read())
    pass

write_array('inp.txt', 'output.txt')
