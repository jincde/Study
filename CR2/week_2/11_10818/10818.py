# BOJ 10818. 최소, 최대

N = int(input())
a = list(map(int, input().split()))

a.sort()
print(a[0], a[-1])