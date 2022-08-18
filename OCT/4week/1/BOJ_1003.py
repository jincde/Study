# BOJ 1003. 피보나치 함수
# 0 = (1, 0), 1 = (0, 1) 2 = (1, 1), 3 = (1, 2)
# N = (N-1) + (N-2)
 
T = int(input())

for _ in range(T):
    p = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    
    for i in range(3, p+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    print(zero[p], one[p])