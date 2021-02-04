# 세 정수를 입력받아 최댓값 구하기

def max3(a, b, c):
    maximun = a
    if b > maximun:
        maximun = b
    if c > maximun:
        maximun = c
    return maximun


print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 1)}')
print(f'max3(3, 1, 2) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 3) = {max3(3, 2, 1)}')
print(f'max3(2, 1, 3) = {max3(3, 2, 1)}')
print(f'max3(3, 3, 2) = {max3(3, 2, 1)}')
print(f'max3(3, 3, 3) = {max3(3, 2, 1)}')
print(f'max3(2, 2, 3) = {max3(3, 2, 1)}')
print(f'max3(2, 3, 1) = {max3(3, 2, 1)}')
print(f'max3(2, 3, 2) = {max3(3, 2, 1)}')
print(f'max3(1, 3, 2) = {max3(3, 2, 1)}')
print(f'max3(2, 3, 1) = {max3(3, 2, 1)}')
print(f'max3(1, 2, 1) = {max3(3, 2, 1)}')