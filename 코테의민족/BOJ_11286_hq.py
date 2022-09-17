# 절댓값 힙
# heapq 사용

import heapq
# import sys 사용 필요

N = int(input())
arr = []

for i in range(N):
  number = int(input())
  if number != 0:
    heapq.heappush(arr, (abs(number), number))
  else:
    if not arr:
      print(0)
    else:
      print(heapq.heappop(arr)[1])