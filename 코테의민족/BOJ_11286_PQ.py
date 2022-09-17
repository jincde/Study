# 절댓값 힙
# PriorityQueue 사용

from queue import PriorityQueue
# import sys 적용 필요

N = int(input())
arr = PriorityQueue()

for i in range(N):
  number = int(input())

  if number == 0:
    if arr.empty():
      print(0)
    else:
      temp = arr.get()
      print((temp[1]))
  
  else:
    arr.put((abs(number), number))