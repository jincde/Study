# BOJ 14681. 사분면 고르기
# Q1 +, +
# Q2 -, +
# Q3 -, -
# Q4 +, -

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)