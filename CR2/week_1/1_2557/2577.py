# 백준 2577. 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

result = A * B * C

for i in range(10):
    print(str(result).count(str(i)))