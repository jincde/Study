# result = [(100, 0), (300, 1), (300, 2), (150, 3), (200, 1)]
# a = sorted(result, key = lambda x : (-x[1], x[0]))
# print(a)

T = int(input()) # 몇 개의 테스트케이스?

for i in range(1, T+1): # 1부터 T까지 반복
    tc = int(input()) # 몇 번째 테스트케이스?
    scores = list(map(int, input().split()))

    dic = {}
    for j in scores:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1


    result = sorted(dic.items(), key = lambda x : (-x[1], -x[0])) # 밸류값 큰 순으로 먼저 정렬, 키값 큰순으로 다음 정렬
    print(f'#{tc}', result[0][0])