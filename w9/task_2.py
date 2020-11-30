import zipfile
import os
import re
import pathlib

class TextLoader:

    def __init__(self,address):
        with zipfile.ZipFile('sample.zip','r') as zip_ref:
            zip_ref.extractall(address)
        self.path = pathlib.Path('sample')
        files_path = [name for name in list(self.path.glob('**/*')) if name.is_file()]
        self.files = files_path
        self.iterable = iter(self.files)

    def __len__(self):
        return len(self.files)

    def __next__(self):
        text_path = next(self.iterable)
        with text_path.open('r') as f:
            reading = f.read()
        with text_path.open('w') as f:
            normalized = self.normal(reading)
            f.write(normalized)
        f= text_path.open('r') 
        return f

    def __iter__(self):
        return self

    def normal(self,s):
        s = re.sub(r',.:;-', ' ',s)
        s = s.lower()
        return s

address = '.'
example = TextLoader(address)
print(len(example))
for i in range(len(example)):
    try:
        a = next(example)
        print(a.read()[:30])
        print('------')
    except StopIteration:
        print('That is all')

