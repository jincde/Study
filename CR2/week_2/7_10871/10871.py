# BOJ 10871. X보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))

result = []
for i in A:
    if i < X:
        result.append(i)
    else:
        pass

print(*result)