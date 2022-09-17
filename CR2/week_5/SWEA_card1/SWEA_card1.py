T = int(input())

for i in range(1, T+1):
    nums = input().split()
    result = 0

    for j in range(15):
        if j % 2 == 0:
            result += int(nums[j]) * 2 # 홀수 자리
        else:
            result += int(nums[j]) # 짝수 자리

    N = result % 10 # 전체 결과를 10으로 나눈 나머지 값

    if N  == 0: # 10으로 나눠졌으면 그대로 출력
        print(f'#{i} {N}')
    else: # 10 - (10으로 나눠준 나머지)
        print(f'#{i} {10-N}')