# BOJ 11022. A+B - 8

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{tc}: {A} + {B} = {A+B}')