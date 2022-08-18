# BOJ 11021. A+B - 7

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{tc}: {A+B}')