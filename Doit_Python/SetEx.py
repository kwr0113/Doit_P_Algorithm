# 집합 자료형

# 집합명 = {요소1, 요소2, 요소3, …}
# SetName = {1, 2, 3}

a = set()
b = {1, 2, 3}
c = {1, 'hi', (2, 5)}
print(c)                            # {1, (2, 5), 'hi'}
# d = {[1, 2, 3, 4]}                  # 오류 TypeError: unhashable type: 'list'
d = set([1, 2, 3, 4])
print(d)                            # {1, 2, 3, 4}
e = set("hello")
print(e)                            # {'o', 'e', 'h', 'l'}

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 & s2)                      # {3, 4, 5}
print(s1.intersection(s2))          # {3, 4, 5}
print(s2 & s1)                      # {3, 4, 5}
print(s2.intersection(s1))          # {3, 4, 5}

print(s1 | s2)                      # {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2))                 # {1, 2, 3, 4, 5, 6, 7}
print(s2 | s1)                      # {1, 2, 3, 4, 5, 6, 7}
print(s2.union(s1))                 # {1, 2, 3, 4, 5, 6, 7}

print(s1 - s2)                      # {1, 2}
print(s1.difference(s2))            # {1, 2}
print(s2 - s1)                      # {6, 7}
print(s2.difference(s1))            # {6, 7}
