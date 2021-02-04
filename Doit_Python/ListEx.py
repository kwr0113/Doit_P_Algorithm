# 리스트 자료형

# 리스트명 = [요소1, 요소2, 요소3, …]
# ListName = [1, 2, 3, …]

a = []
b = [1, 2, 3]
c = ["this", "is", "Python"]
d = [1, 2, "this", "Python"]
e = [[1, 2], "this", [3, "Python"]]

print(b)                            # [1, 2, 3]
print(b[0], b[1], b[2])             # 1 2 3
print(c)                            # ['this', 'is', 'Python']
print(c[0], c[1], c[2])             # this is Python
print(d)                            # [1, 2, 'this', 'Python']
print(d[0], d[1], d[2], d[3])       # 1 2 this Python
print(e)                            # [[1, 2], 'this', [3, 'Python']]
print(e[0], e[1], e[2])             # [1, 2] this [3, 'Python']
print(e[0][0], e[0][1])             # 1 2
print(e[2][0], e[2][1])             # 3 Python

print(b[0:1])                       # [1]
print(b[1:3])                       # [2, 3]
print(c[0:])                        # ['this', 'is', 'Python']
print(c[:-1])                       # ['this', 'is']
print(d[2:])                        # ['this', 'Python']
print(d[:2])                        # [1, 2]
print(e[0:2])                       # [[1, 2], 'this']

f = c + b
print(f)                            # ['this', 'is', 'Python', 1, 2, 3]
g = d * 2
print(g)                            # [1, 2, 'this', 'Python', 1, 2, 'this', 'Python']
print(len(e))                       # 3

g[3] = "is"
g[4] = "Java"
print(g)                            # [1, 2, 'this', 'Python', 1, 2, 'this', 'Python']
del g[0], g[0]
del g[3:]
print(g)                            # ['this', 'is', 'Java']
del g
print(g)                            # 오류 NameError: name 'g' is not defined
