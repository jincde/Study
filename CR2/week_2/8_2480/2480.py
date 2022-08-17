# BOJ 2480. 주사위 세개
# dictionary로 해결

dice = list(map(int, input().split()))
dict = {}

for i in dice:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

if len(dict) == 1:
    k, v = list(dict.items())[0]
    print(10000 + k * 1000)
elif len(dict) == 2:
    for k, v in dict.items():
        if v == 2:
            print(1000 + k * 100)
else:
    k = max(dict.keys()) # max or sorted 시간복잡도 비교해보기
    print(k * 100)