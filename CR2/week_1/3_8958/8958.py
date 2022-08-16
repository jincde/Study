# 백준 8958. OX 퀴즈

T = int(input())

for _ in range(T):
    s = list(input())

    cnt = 1
    sum_ = 0
    for i in s:
        if i == 'O':
            sum_ += cnt
            cnt += 1
        else:
            cnt = 1

    
    print(sum_)