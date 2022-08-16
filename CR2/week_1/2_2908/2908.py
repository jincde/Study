# 백준 2908. 상수

A, B = input().split()

if int(A[::-1]) > int(B[::-1]):
    print(int(A[::-1]))
else:
    print(int(B[::-1]))