# 오른쪽 아래가 직각인 이등변삼각형 모양의 * 출력하기

n = int(input('변의 길이를 입력하세요 : '))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()