## BOJ 1003. 피보나치 함수
### 풀이법

![IMG_0261](README.assets/IMG_0261.PNG)

```sql
# BOJ 1003. 피보나치 함수
# 인덱스를 이용한 문제풀이
# Dynamic Programming

T = int(input()) # 테스트케이스 개수

for _ in range(T): # 반복
    p = int(input()) # 입력값 (변수명 p라고 선언한 이유는 pibonacci)

    # 인덱스마다 개수를 미리 입력해놔도 풀 수 있다. 
    # but, 4개부터는 1이 넘어가서 컴퓨터에 맡긴다.
    zero = [1, 0, 1] # 인덱스0은 p가 0일때 0의 출력 개수, 인덱스 1은 p가 1일때 0의 출력 개수
    one = [0, 1, 1]  # 인덱스0은 p가 0일때 1의 출력 개수, 인덱스 1은 p가 1일때 1의 출력 개수
    
    for i in range(3, p+1): # 인덱스 2까지는 입력해놨으니, 3부터 입력값까지 반복
        zero.append(zero[i-1]+zero[i-2]) # 피보나치 패턴 N = (N-1) + (N-2)를 이용
        one.append(one[i-1]+one[i-2])
    print(zero[p], one[p]) # 입력값에 해당하는 인덱스를 출력
```

