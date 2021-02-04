# 튜플 자료형

# 튜플명 = (요소1, 요소2, 요소3, …)
# TupleName = (1, 2, 3, …)

a = ()
b = (1,)
c = (1, 2, 3)
d = 1, 2, "this", "Python"
e = ((1, 2), "this", (3, "Python"))
f = 2,

print(b)                            # (1,)
print(b[0])                         # 1
print(c)                            # (1, 2, 3)
print(c[0], c[1], c[2])             # 1 2 3
print(d)                            # (1, 2, 'this', 'Python')
print(d[0], d[1], d[2], d[3])       # 1 2 this Python
print(e)                            # ((1, 2), 'this', (3, 'Python'))
print(e[0], e[1], e[2])             # (1, 2) this (3, 'Python')
print(e[0][0], e[0][1])             # 1 2
print(e[2][0], e[2][1])             # 3 Python
print(f)                            # (2,)

print(b[0:1])                       # (1,)
print(c[0:])                        # (1, 2, 3)
print(c[:-1])                       # (1, 2)
print(d[2:])                        # ('this', 'Python')
print(d[:2])                        # (1, 2)
print(e[0:2])                       # ((1, 2), 'this')

f = c + b
print(f)                            # (1, 2, 3, 1)
g = d * 2
print(g)                            # (1, 2, 'this', 'Python', 1, 2, 'this', 'Python')
print(len(e))                       # 3