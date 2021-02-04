# 딕셔너리 자료형

# 딕셔너리명 = {키1:요소1, 키2:요소2, 키3:요소3, …}
# DictName = {'name':'Narin', 'age':'20', 'birth':'0101'}

a = {}
b = {1: 'hi'}
c = {'a': [1, 2, 3]}
d = {'abc': 2, 'def': 5, 'ghi': 1}

b[2] = 'my'
print(b)                            # {1: 'hi', 2: 'my'}
c['b'] = [4, 5, 6]
print(c)                            # {'a': [1, 2, 3], 'b': [4, 5, 6]}
d['jkl'] = 8
print(d)                            # {'abc': 2, 'def': 5, 'ghi': 1, 'jkl': 8}

del b[1]
print(b)                            # {2: 'my'}
del d['abc']
print(d)                            # {'def': 5, 'ghi': 1, 'jkl': 8}

print(b[2])                         # my
print(c['a'])                       # [1, 2, 3]
print(d['def'])                     # 5

DictName = {'name': 'Narin', 'age': '20', 'birth': '0101'}
print(list(DictName.keys()))        # ['name', 'age', 'birth']
for i in DictName.keys():           # name
    print(i)                        # age
                                    # birth

print(list(DictName.values()))      # ['Narin', '20', '0101']
for i in DictName.values():         # Narin
    print(i)                        # 20
                                    # 0101

print((list(DictName.items())))     # [('name', 'Narin'), ('age', '20'), ('birth', '0101')]
for i in DictName.items():          # ('name', 'Narin')
    print(i)                        # ('age', '20')
                                    # ('birth', '0101')


