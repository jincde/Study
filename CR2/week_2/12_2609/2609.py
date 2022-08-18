# BOJ 2609. 최대공약수와 최소공배수

# 같은 수로 나눠지면 공약수, 그 중 가장 큰 값이 최대 공약수
# 두 개의 숫자 중 더 큰 숫자까지만 반복
# 내림차순으로 계산하면 max값을 뽑을 필요가 없을 듯

a = list(map(int, input().split()))
value = max(a)

while True:
    if a[0] % value == 0 and a[1] % value == 0:
        print(value) # 최대공약수
        print(a[0] * a[1] // value) # 최소공배수
        break
    else:
        value -= 1