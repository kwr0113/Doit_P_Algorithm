# 세 정수를 입력받아 중앙값 구하기 1

def med3_1(a, b, c):
    if a>= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


def med3_2(a, b, c):
    if (b >= a >= c) or (b <= a <= c):
        return a
    elif (a > b > c) or (a < b < c):
        return b
    return c


print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 A의 값을 입력하세요 : '))
b = int(input('정수 B의 값을 입력하세요 : '))
c = int(input('정수 C의 값을 입력하세요 : '))

print(f'중앙값은 {med3_2(a, b, c)} 입니다.')