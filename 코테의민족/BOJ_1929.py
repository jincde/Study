# 소수 구하기

N = 10 ** 6
x, y = map(int, input().split())

arr = [True] * (N+1)
arr[0] = False
arr[1] = False

def isPrime():
  for i in range(N+1):
    if arr[i] == True:
      for j in range(i*2, N+1, i):
        arr[j] = False

isPrime()

result = []

for k in range(x, y+1):
  if arr[k] == True:
    print(k)